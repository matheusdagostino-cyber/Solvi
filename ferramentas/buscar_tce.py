#!/usr/bin/env python3
"""Client da API Lei na Mão (TCU/TCE).

Uso:
  python ferramentas/buscar_tce.py --query "qualificação técnica quantitativos mínimos" --tribunal TCU
  python ferramentas/buscar_tce.py --query "aterro sanitário operação" --tribunal TCE-SP --paginas 2 --csv resultados.csv

Autenticação: variável de ambiente LEINAMAO_API_KEY (Authorization: Bearer).
Observação: a API exige User-Agent de navegador (filtro anti-bot).
Parâmetros reais da API: q (palavras-chave), tribunal, type, limit, offset.
Resposta: {"data": [...], "total": N, "limit": N, "offset": N, "meta": {...}}
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
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")


def montar_sessao(api_key: str) -> requests.Session:
    s = requests.Session()
    s.headers["Authorization"] = f"Bearer {api_key}"
    s.headers["Accept"] = "application/json"
    s.headers["User-Agent"] = UA
    if os.path.exists(CA_BUNDLE):
        s.verify = CA_BUNDLE
    return s


def buscar(sessao, q, tribunal, tipo, limit, offset):
    params = {"q": q, "limit": limit, "offset": offset}
    if tribunal:
        params["tribunal"] = tribunal
    if tipo:
        params["type"] = tipo
    r = sessao.get(ENDPOINT, params=params, timeout=60)
    if r.status_code in (401, 403):
        sys.exit(f"Autenticação recusada (HTTP {r.status_code}): {r.text[:300]}")
    if r.status_code != 200:
        sys.exit(f"Erro HTTP {r.status_code}: {r.text[:500]}")
    return r.json()


def formatar_identificacao(item):
    numero = item.get("number") or item.get("id", "")
    ano = item.get("year") or ""
    colegiado = item.get("collegiate") or ""
    trib = (item.get("tribunals") or {}).get("name") or ""
    ident = f"{numero}/{ano}" if ano and "/" not in str(numero) else str(numero)
    partes = [p for p in [ident, trib, colegiado] if p]
    return " — ".join(partes)


def main():
    ap = argparse.ArgumentParser(description="Busca decisões TCU/TCE na API Lei na Mão")
    ap.add_argument("--query", required=True, help="Palavras-chave (parâmetro q da API)")
    ap.add_argument("--tribunal", default=None, help="Filtro de tribunal (ex.: TCU, TCE-SP)")
    ap.add_argument("--type", dest="tipo", default=None, help="Tipo de decisão (ex.: acordao)")
    ap.add_argument("--paginas", type=int, default=1, help="Quantas páginas (default 1)")
    ap.add_argument("--tamanho", type=int, default=20, help="Resultados por página (default 20)")
    ap.add_argument("--csv", default=None, help="Exportar resultados para CSV")
    ap.add_argument("--json", action="store_true", help="Imprimir itens em JSON bruto")
    # compatibilidade com a interface documentada no CLAUDE.md
    ap.add_argument("--operador", default=None, choices=["AND", "OR", "and", "or"],
                    help="(compatibilidade) a API usa busca por relevância; AND/OR não são parâmetros nativos")
    args = ap.parse_args()

    api_key = os.environ.get("LEINAMAO_API_KEY")
    if not api_key and os.path.exists("/root/.leinamao_key"):
        api_key = Path("/root/.leinamao_key").read_text().strip()
    if not api_key:
        sys.exit("LEINAMAO_API_KEY não configurada no ambiente.")

    sessao = montar_sessao(api_key)
    todos, total_api = [], None
    for i in range(args.paginas):
        payload = buscar(sessao, args.query, args.tribunal, args.tipo,
                         args.tamanho, i * args.tamanho)
        total_api = payload.get("total", total_api)
        itens = payload.get("data") or []
        todos.extend(itens)
        if len(todos) >= (total_api or 0):
            break

    print(f"{len(todos)} de {total_api} decisão(ões) para: {args.query!r}"
          + (f" [tribunal: {args.tribunal}]" if args.tribunal else ""))

    if args.json:
        print(json.dumps(todos, ensure_ascii=False, indent=1))

    linhas = []
    for item in todos:
        linha = {
            "tribunal": (item.get("tribunals") or {}).get("name", ""),
            "numero": item.get("number", ""),
            "ano": item.get("year", ""),
            "data_sessao": item.get("session_date", ""),
            "tipo": item.get("type", ""),
            "relator": item.get("rapporteur") or "",
            "colegiado": item.get("collegiate") or "",
            "assunto": str(item.get("subject") or "")[:500],
            "resumo_ia": str(item.get("ai_summary") or "")[:2000],
            "url": item.get("source_url") or "",
            "verificado": "false",
            "flag": "[VIT]",
        }
        linhas.append(linha)
        if not args.json:
            print(f"\n[VIT] {formatar_identificacao(item)}"
                  + (f" — Rel. {linha['relator']}" if linha["relator"] else "")
                  + (f" — sessão {linha['data_sessao']}" if linha["data_sessao"] else ""))
            if linha["resumo_ia"]:
                print(f"   {linha['resumo_ia'][:500]}")

    if args.csv and linhas:
        destino = Path(args.csv)
        with open(destino, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(linhas[0].keys()))
            w.writeheader()
            w.writerows(linhas)
        print(f"\nCSV exportado: {destino} ({len(linhas)} linhas, todas verificado=false → [VIT])")


if __name__ == "__main__":
    main()
