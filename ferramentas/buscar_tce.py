#!/usr/bin/env python3
"""Client da API Lei na Mão (TCU/TCE).

Uso:
  python ferramentas/buscar_tce.py --query "qualificação técnica parcelas relevância" --tribunal TCU --operador AND
  python ferramentas/buscar_tce.py --query "aterro sanitário operação" --tribunal TCE-SP --paginas 2 --csv resultados.csv
  python ferramentas/buscar_tce.py --query "teste" --debug          # inspeciona a resposta bruta da API

Autenticação: variável de ambiente LEINAMAO_API_KEY.
Toda citação extraída desta fonte recebe flag [VIT] até verificação do inteiro teor.
"""
import argparse
import csv
import json
import os
import sys
from pathlib import Path

try:
    import requests
except ImportError:
    sys.exit("Instale requests: pip install requests")

ENDPOINT = "https://tce.leinamao.com.br/api/v1/decisions"
CA_BUNDLE = "/root/.ccr/ca-bundle.crt"


def montar_sessao(api_key: str, auth_header: str) -> requests.Session:
    s = requests.Session()
    if auth_header == "bearer":
        s.headers["Authorization"] = f"Bearer {api_key}"
    elif auth_header == "x-api-key":
        s.headers["X-API-Key"] = api_key
    elif auth_header == "api-key":
        s.headers["api-key"] = api_key
    s.headers["Accept"] = "application/json"
    if os.path.exists(CA_BUNDLE):
        s.verify = CA_BUNDLE
    return s


def buscar(sessao, query, tribunal, operador, pagina, tamanho, extra):
    params = {
        "query": query,
        "operator": operador,
        "page": pagina,
        "size": tamanho,
    }
    if tribunal:
        params["court"] = tribunal
    for kv in extra or []:
        k, _, v = kv.partition("=")
        params[k] = v
    r = sessao.get(ENDPOINT, params=params, timeout=60)
    return r


def extrair_itens(payload):
    """Aceita os formatos usuais de paginação: lista direta, {data|results|items|decisions: [...]}"""
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict):
        for k in ("data", "results", "items", "decisions", "content"):
            if isinstance(payload.get(k), list):
                return payload[k]
    return []


def campo(item, *nomes, default=""):
    for n in nomes:
        if isinstance(item, dict) and item.get(n) not in (None, ""):
            return item[n]
    return default


def main():
    ap = argparse.ArgumentParser(description="Busca decisões TCU/TCE na API Lei na Mão")
    ap.add_argument("--query", required=True, help="Palavras-chave da busca")
    ap.add_argument("--tribunal", default=None, help="Filtro de tribunal (ex.: TCU, TCE-SP)")
    ap.add_argument("--operador", default="AND", choices=["AND", "OR", "and", "or"], help="Operador entre palavras")
    ap.add_argument("--paginas", type=int, default=1, help="Quantas páginas buscar (default 1)")
    ap.add_argument("--tamanho", type=int, default=20, help="Resultados por página (default 20)")
    ap.add_argument("--pagina-inicial", type=int, default=1, help="Índice da primeira página (default 1)")
    ap.add_argument("--csv", default=None, help="Exportar resultados para CSV")
    ap.add_argument("--auth-header", default="bearer", choices=["bearer", "x-api-key", "api-key"],
                    help="Formato do header de autenticação (default bearer)")
    ap.add_argument("--param", action="append", metavar="CHAVE=VALOR",
                    help="Parâmetro extra de query string (repetível)")
    ap.add_argument("--debug", action="store_true", help="Imprime status e corpo bruto da primeira resposta e sai")
    args = ap.parse_args()

    api_key = os.environ.get("LEINAMAO_API_KEY")
    if not api_key:
        sys.exit("LEINAMAO_API_KEY não configurada no ambiente.")

    sessao = montar_sessao(api_key, args.auth_header)
    todos = []
    for i in range(args.paginas):
        pagina = args.pagina_inicial + i
        r = buscar(sessao, args.query, args.tribunal, args.operador.upper(), pagina, args.tamanho, args.param)
        if args.debug:
            print(f"HTTP {r.status_code}")
            print(dict(r.headers))
            print(r.text[:5000])
            return
        if r.status_code == 401 or r.status_code == 403:
            sys.exit(f"Autenticação recusada (HTTP {r.status_code}). Tente --auth-header x-api-key ou api-key. Corpo: {r.text[:300]}")
        if r.status_code != 200:
            sys.exit(f"Erro HTTP {r.status_code}: {r.text[:500]}")
        try:
            payload = r.json()
        except json.JSONDecodeError:
            sys.exit(f"Resposta não-JSON: {r.text[:500]}")
        itens = extrair_itens(payload)
        if not itens:
            if i == 0:
                print("Nenhum resultado. Payload bruto (primeiros 800 chars):")
                print(json.dumps(payload, ensure_ascii=False)[:800])
            break
        todos.extend(itens)

    print(f"{len(todos)} decisão(ões) encontradas para: {args.query!r}"
          + (f" [tribunal: {args.tribunal}]" if args.tribunal else ""))
    linhas = []
    for item in todos:
        linha = {
            "tribunal": campo(item, "court", "tribunal", "orgao"),
            "identificacao": campo(item, "identification", "acordao", "decision", "numero", "id"),
            "orgao_julgador": campo(item, "chamber", "orgao_julgador", "colegiado"),
            "relator": campo(item, "rapporteur", "relator"),
            "data_julgamento": campo(item, "judgment_date", "data_julgamento", "date", "data"),
            "processo": campo(item, "case_number", "processo", "tc"),
            "ementa_trecho": str(campo(item, "summary", "ementa", "excerpt", "text", "conteudo"))[:2000],
            "url": campo(item, "url", "link"),
            "verificado": "false",
            "flag": "[VIT]",
        }
        linhas.append(linha)
        print(f"\n[VIT] {linha['tribunal']} — {linha['identificacao']}"
              + (f" — Rel. {linha['relator']}" if linha['relator'] else "")
              + (f" — j. {linha['data_julgamento']}" if linha['data_julgamento'] else "")
              + (f" — {linha['processo']}" if linha['processo'] else ""))
        if linha["ementa_trecho"]:
            print(f"   {linha['ementa_trecho'][:400]}")

    if args.csv and linhas:
        destino = Path(args.csv)
        with open(destino, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(linhas[0].keys()))
            w.writeheader()
            w.writerows(linhas)
        print(f"\nCSV exportado: {destino} ({len(linhas)} linhas, todas verificado=false → [VIT])")


if __name__ == "__main__":
    main()
