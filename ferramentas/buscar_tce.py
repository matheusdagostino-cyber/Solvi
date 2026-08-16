#!/usr/bin/env python3
"""
Client para a API Lei na Mão — busca de decisões em Tribunais de Contas.

Endpoint: https://tce.leinamao.com.br/api/v1/decisions
Autenticação: Authorization: Bearer <LEINAMAO_API_KEY> (env var ou .env na raiz)

Semântica de busca (comportamento verificado da API):
- termos separados por espaço = E implícito (todos devem ocorrer);
- NÃO usar AND/OR textuais — a API os trata como termos literais;
- a query é enviada como digitada (frases podem ir entre aspas).

Uso:
    python ferramentas/buscar_tce.py --query "qualificação técnica parcelas relevância"
    python ferramentas/buscar_tce.py --query "parcela de maior relevância" --tribunal TCE-SP
    python ferramentas/buscar_tce.py --query "PPP garantia pública" --csv resultado.csv

Nota: o campo de resumo retornado (ai_summary) é gerado por IA pela própria
plataforma — NÃO é a ementa oficial. Toda citação permanece [VIT] até
verificação do inteiro teor no portal do tribunal (source_url ajuda).
"""

import argparse
import csv
import json
import os
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


def validar_query(query):
    """Alerta sobre AND/OR textuais, que a API trata como termos literais."""
    tokens = query.split()
    if any(t.upper() in ("AND", "OR") for t in tokens):
        print(
            "AVISO: a API não entende AND/OR — serão buscados como palavras "
            "literais e provavelmente zeram o resultado. Termos separados por "
            "espaço já funcionam como E implícito.",
            file=sys.stderr,
        )
    return query


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


def buscar(query, tribunal=None, limite=10, offset=0):
    """Busca decisões na API Lei na Mão. Retorna dict/list com resultados."""
    api_key = _load_api_key()

    params = {"q": validar_query(query), "limit": limite, "offset": offset}
    if tribunal:
        params["tribunal"] = tribunal

    url = f"{API_BASE}?{urllib.parse.urlencode(params)}"

    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {api_key}",
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
        if e.code == 500:
            print(f"ERRO HTTP 500 do servidor da API: {body}", file=sys.stderr)
            print("(instabilidade conhecida em algumas buscas de termo único — "
                  "tente reformular com dois ou mais termos)", file=sys.stderr)
        else:
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


def _campo_tribunal(item):
    trib = item.get("tribunals") or {}
    if isinstance(trib, dict):
        return trib.get("name") or trib.get("code") or "?"
    return str(trib)


def _identificacao(item):
    """Ex.: 'Acórdão 447/2021' / 'Decisão Monocrática 6195/2020'."""
    tipos = {"acordao": "Acórdão", "decisao_monocratica": "Decisão Monocrática"}
    tipo = tipos.get(item.get("type", ""), (item.get("type") or "Decisão").replace("_", " ").title())
    numero = item.get("number", "?")
    ano = item.get("year", "?")
    return f"{tipo} {numero}/{ano}"


def formatar_resultado(item, idx):
    """Formata um resultado para exibição no terminal."""
    linhas = [f"\n{'='*60}"]
    linhas.append(f"  [{idx}] {_campo_tribunal(item)} — {_identificacao(item)}")
    if item.get("collegiate"):
        linhas.append(f"  Órgão: {item['collegiate']}")
    if item.get("rapporteur"):
        linhas.append(f"  Rel.: {item['rapporteur']}")
    if item.get("session_date"):
        linhas.append(f"  Sessão: {item['session_date']}")
    if item.get("subject"):
        linhas.append(f"  Assunto: {item['subject']}")
    if item.get("ai_summary"):
        resumo = item["ai_summary"][:500]
        if len(item["ai_summary"]) > 500:
            resumo += "..."
        linhas.append(f"  Resumo (gerado por IA — não é a ementa oficial): {resumo}")
    if item.get("cited_laws"):
        linhas.append(f"  Normas citadas: {'; '.join(item['cited_laws'])}")
    if item.get("source_url"):
        linhas.append(f"  Inteiro teor: {item['source_url']}")
    linhas.append(f"  [VIT] Verificar inteiro teor antes de citar em peça formal.")
    return "\n".join(linhas)


def exportar_csv(items, caminho):
    """Exporta resultados para CSV com flag [VIT] e coluna de verificação."""
    if not items:
        print("Nenhum resultado para exportar.", file=sys.stderr)
        return

    campos = ["flag", "tribunal", "identificacao", "orgao_julgador", "relator",
              "data_sessao", "assunto", "resumo_ia", "normas_citadas",
              "url_inteiro_teor", "verificado"]
    with open(caminho, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        for item in items:
            writer.writerow({
                "flag": "[VIT]",
                "tribunal": _campo_tribunal(item),
                "identificacao": _identificacao(item),
                "orgao_julgador": item.get("collegiate") or "",
                "relator": item.get("rapporteur") or "",
                "data_sessao": item.get("session_date") or "",
                "assunto": item.get("subject") or "",
                "resumo_ia": item.get("ai_summary") or "",
                "normas_citadas": "; ".join(item.get("cited_laws") or []),
                "url_inteiro_teor": item.get("source_url") or "",
                "verificado": "false",
            })
    print(f"Exportado: {caminho} ({len(items)} registros, todos [VIT]; "
          f"coluna resumo_ia NÃO é ementa oficial)", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(
        description="Busca decisões de Tribunais de Contas via API Lei na Mão. "
                    "Termos separados por espaço = E implícito; não usar AND/OR."
    )
    parser.add_argument("--query", "-q", required=True, help="Termos de busca (E implícito entre termos)")
    parser.add_argument("--tribunal", "-t", help="Filtrar por tribunal (ex.: TCU, TCE-SP, TCE-MS)")
    parser.add_argument("--limite", "-l", type=int, default=10, help="Quantidade de resultados (default: 10)")
    parser.add_argument("--offset", type=int, default=0, help="Paginação por índice")
    parser.add_argument("--csv", dest="csv_path", help="Exportar para CSV")
    parser.add_argument("--json", action="store_true", help="Saída em JSON bruto")

    args = parser.parse_args()

    resultados = buscar(
        query=args.query,
        tribunal=args.tribunal,
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
        elif len(items) == args.limite and total is None:
            print(f"Pode haver mais resultados: use --offset {args.offset + args.limite}.")
    print("[VIT] = Verificar Inteiro Teor — resumo gerado por IA, não é a ementa oficial.")


if __name__ == "__main__":
    main()
