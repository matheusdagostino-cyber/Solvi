#!/usr/bin/env python3
"""
Client para a API Lei na Mão — busca de decisões em Tribunais de Contas.

Endpoint: https://tce.leinamao.com.br/api/v1/decisions
Autenticação: variável LEINAMAO_API_KEY (ou arquivo .env na raiz do repo)

Uso:
    python ferramentas/buscar_tce.py --query "qualificação técnica parcelas relevância"
    python ferramentas/buscar_tce.py --query '"parcela de maior relevância" concessão' --tribunal TCE-SP
    python ferramentas/buscar_tce.py --query "SRP serviço contínuo" --operador OR --limite 20
    python ferramentas/buscar_tce.py --query "PPP garantia pública FGP" --csv resultado.csv

Frases entre aspas são preservadas como termo único. Se a query já contém
AND/OR explícitos, é enviada como está (equivalente a --operador RAW).
"""

import argparse
import csv
import json
import os
import shlex
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

API_BASE = "https://tce.leinamao.com.br/api/v1/decisions"

# chaves conhecidas sob as quais a API pode aninhar a lista de resultados
_CHAVES_LISTA = ("data", "results", "decisions", "items")


def _load_api_key():
    key = os.environ.get("LEINAMAO_API_KEY")
    if key:
        return key
    env_path = Path(__file__).resolve().parent.parent / ".env"
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            line = line.strip()
            if line.startswith("LEINAMAO_API_KEY="):
                return line.split("=", 1)[1].strip().strip("'\"")
    print("ERRO: LEINAMAO_API_KEY não encontrada (env var ou .env).", file=sys.stderr)
    sys.exit(1)


def montar_query(query, operador):
    """Monta a expressão de busca preservando frases entre aspas.

    - tokens com espaço (frases citadas) são re-citados;
    - tokens que já são AND/OR não recebem operador duplicado;
    - query com AND/OR explícito ou operador RAW é enviada como está.
    """
    if operador == "RAW":
        return query

    try:
        tokens = shlex.split(query)
    except ValueError:
        # aspas desbalanceadas — enviar como está em vez de corromper
        return query

    if any(t.upper() in ("AND", "OR") for t in tokens):
        return query

    tokens = [f'"{t}"' if " " in t else t for t in tokens]
    return f" {operador} ".join(tokens)


def _extrair_items(resultados):
    """Extrai a lista de decisões da resposta, qualquer que seja o envelope.

    Aborta com erro explícito quando a estrutura é desconhecida — nunca
    devolve lista vazia silenciosamente para uma resposta com conteúdo.
    """
    if isinstance(resultados, list):
        return resultados
    if isinstance(resultados, dict):
        for chave in _CHAVES_LISTA:
            valor = resultados.get(chave)
            if isinstance(valor, list):
                return valor
            if isinstance(valor, dict):
                for subchave in _CHAVES_LISTA:
                    subvalor = valor.get(subchave)
                    if isinstance(subvalor, list):
                        return subvalor
        if not resultados:
            return []
        print(
            "ERRO: estrutura de resposta desconhecida — chaves recebidas: "
            + ", ".join(sorted(resultados.keys())),
            file=sys.stderr,
        )
        print("Use --json para inspecionar a resposta bruta.", file=sys.stderr)
        sys.exit(1)
    print(f"ERRO: resposta inesperada da API (tipo {type(resultados).__name__}).", file=sys.stderr)
    sys.exit(1)


def buscar(query, tribunal=None, operador="AND", limite=10, offset=0):
    """Busca decisões na API Lei na Mão. Retorna dict/list com resultados."""
    api_key = _load_api_key()

    q = montar_query(query, operador)

    params = {"q": q, "limit": limite, "offset": offset}
    if tribunal:
        params["tribunal"] = tribunal

    url = f"{API_BASE}?{urllib.parse.urlencode(params)}"

    req = urllib.request.Request(url, headers={
        "X-API-Key": api_key,
        "Accept": "application/json",
        "User-Agent": "solvi-editais/1.0",
    })

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            charset = resp.headers.get_content_charset() or "utf-8"
            corpo = resp.read().decode(charset, errors="replace")
    except urllib.error.HTTPError as e:
        body = ""
        if e.fp:
            body = e.read().decode("utf-8", errors="replace")[:500]
        print(f"ERRO HTTP {e.code}: {body}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"ERRO de conexão: {e.reason}", file=sys.stderr)
        sys.exit(1)
    except TimeoutError:
        print("ERRO: tempo de resposta excedido (30s).", file=sys.stderr)
        sys.exit(1)

    try:
        return json.loads(corpo)
    except json.JSONDecodeError:
        print("ERRO: resposta não é JSON válido. Início do corpo recebido:", file=sys.stderr)
        print(corpo[:300], file=sys.stderr)
        sys.exit(1)


def formatar_resultado(item, idx):
    """Formata um resultado para exibição no terminal."""
    linhas = [f"\n{'='*60}"]
    linhas.append(f"  [{idx}] {item.get('tribunal', '?')} — {item.get('numero', '?')}")
    if item.get("relator"):
        linhas.append(f"  Rel.: {item['relator']}")
    if item.get("data_julgamento"):
        linhas.append(f"  Data: {item['data_julgamento']}")
    if item.get("ementa"):
        ementa = item["ementa"][:500]
        if len(item["ementa"]) > 500:
            ementa += "..."
        linhas.append(f"  Ementa: {ementa}")
    if item.get("url"):
        linhas.append(f"  URL: {item['url']}")
    linhas.append(f"  [VIT] Verificar inteiro teor antes de citar em peça formal.")
    return "\n".join(linhas)


def exportar_csv(items, caminho):
    """Exporta resultados para CSV com flag [VIT] e coluna de verificação."""
    if not items:
        print("Nenhum resultado para exportar.", file=sys.stderr)
        return

    campos = ["flag", "tribunal", "numero", "relator", "data_julgamento", "ementa", "url", "verificado"]
    with open(caminho, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=campos, extrasaction="ignore")
        writer.writeheader()
        for item in items:
            row = {k: item.get(k, "") for k in campos}
            row["flag"] = "[VIT]"
            row["verificado"] = "false"
            writer.writerow(row)
    print(f"Exportado: {caminho} ({len(items)} registros, todos [VIT])", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(
        description="Busca decisões de Tribunais de Contas via API Lei na Mão."
    )
    parser.add_argument("--query", "-q", required=True, help="Termos de busca (frases entre aspas são preservadas)")
    parser.add_argument("--tribunal", "-t", help="Filtrar por tribunal (ex.: TCU, TCE-SP)")
    parser.add_argument("--operador", choices=["AND", "OR", "RAW"], default="AND",
                        help="Operador entre termos (default: AND; RAW envia a query como está)")
    parser.add_argument("--limite", "-l", type=int, default=10, help="Quantidade de resultados (default: 10)")
    parser.add_argument("--offset", type=int, default=0, help="Paginação por índice")
    parser.add_argument("--csv", dest="csv_path", help="Exportar para CSV")
    parser.add_argument("--json", action="store_true", help="Saída em JSON bruto")

    args = parser.parse_args()

    resultados = buscar(
        query=args.query,
        tribunal=args.tribunal,
        operador=args.operador,
        limite=args.limite,
        offset=args.offset,
    )

    if args.json:
        print(json.dumps(resultados, ensure_ascii=False, indent=2))
        return

    items = _extrair_items(resultados)

    if args.csv_path:
        exportar_csv(items, args.csv_path)

    if not items:
        print("Nenhum resultado encontrado.")
        return

    print(f"\n{len(items)} resultado(s) para: {args.query}")
    if args.tribunal:
        print(f"Tribunal: {args.tribunal}")
    for i, item in enumerate(items, 1):
        print(formatar_resultado(item, i))
    print(f"\n{'='*60}")
    if isinstance(resultados, dict):
        total = resultados.get("total") or resultados.get("count")
        if isinstance(total, int) and total > args.offset + len(items):
            print(f"Mostrando {args.offset + 1}-{args.offset + len(items)} de {total}; "
                  f"use --offset {args.offset + len(items)} para a próxima página.")
    if len(items) == args.limite:
        print(f"Pode haver mais resultados: use --offset {args.offset + args.limite}.")
    print("[VIT] = Verificar Inteiro Teor — citação não verificada no portal do tribunal.")


if __name__ == "__main__":
    main()
