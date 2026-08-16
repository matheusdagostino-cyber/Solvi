#!/usr/bin/env python3
"""Montagem determinística da lista consolidada (C) a partir do plano de consolidação.

Uso:
  python3 ferramentas_consolidacao.py [--validate-only]

Lê   docs/E{1..4}_pontos.yaml + docs/C_plano.json
Gera docs/C_consolidado.yaml + docs/C_sumario.md
"""
import json
import sys
from pathlib import Path

import yaml

DOCS = Path(__file__).parent / "docs"

TEMA_ORDEM = [
    "OBJETO_ESCOPO",
    "HABILITACAO",
    "JULGAMENTO_PROPOSTA",
    "MODELAGEM_ECONOMICA",
    "RISCOS_GARANTIAS",
    "REMUNERACAO_REAJUSTE",
    "REGULACAO_FISCALIZACAO",
    "LICENCIAMENTO_AMBIENTAL",
    "QUESTOES_FORMAIS",
]
SEVERIDADE = {"IRREGULAR": 0, "DEPENDE_DE_FATO": 1, "CONFORME": 2}
CATEGORIAS = {
    "omissao", "contradicao", "ilegalidade",
    "restricao_competitividade", "risco_economico", "erro_material",
}


def carregar_origens():
    pontos = {}
    for nome in ["E1_pontos.yaml", "E2_pontos.yaml", "E3_pontos.yaml", "E4_pontos.yaml"]:
        with open(DOCS / nome, encoding="utf-8") as fh:
            for p in yaml.safe_load(fh):
                pid = p["id"]
                if pid in pontos:
                    raise SystemExit(f"id duplicado entre arquivos de origem: {pid}")
                pontos[pid] = p
    return pontos


def validar(plano, origens):
    erros = []
    temas = plano.get("temas", {})
    for pid in origens:
        if pid not in temas:
            erros.append(f"id sem tema no plano: {pid}")
    for pid, tema in temas.items():
        if pid not in origens:
            erros.append(f"tema para id inexistente: {pid}")
        if tema not in TEMA_ORDEM:
            erros.append(f"tema inválido para {pid}: {tema}")

    vistos = set()
    for grupo in plano.get("merges", []):
        ids = grupo["ids"]
        if len(ids) < 2:
            erros.append(f"grupo de merge com menos de 2 ids: {ids}")
        for pid in ids:
            if pid not in origens:
                erros.append(f"merge referencia id inexistente: {pid}")
            if pid in vistos:
                erros.append(f"id em mais de um grupo de merge: {pid}")
            vistos.add(pid)

    for c in plano.get("contradicoes", []):
        for pid in c.get("ids_origem", []):
            if pid not in origens:
                erros.append(f"contradição {c.get('id_sugerido')} referencia id inexistente: {pid}")
        if c.get("tema") not in TEMA_ORDEM:
            erros.append(f"contradição {c.get('id_sugerido')} com tema inválido: {c.get('tema')}")
        if c.get("tipo_achado") not in SEVERIDADE:
            erros.append(f"contradição {c.get('id_sugerido')} com tipo_achado inválido: {c.get('tipo_achado')}")
    return erros


def _unicos(seq):
    vistos, out = set(), []
    for x in seq:
        if x and x not in vistos:
            vistos.add(x)
            out.append(x)
    return out


def montar_merge(ids, origens, temas, nota_plano):
    grupo = [origens[i] for i in ids]
    tipos = _unicos(p["tipo_achado"] for p in grupo)
    if len(tipos) == 1:
        tipo = tipos[0]
        nota_div = ""
    else:
        tipo = "DEPENDE_DE_FATO"
        nota_div = f"Divergência de classificação entre extratores ({', '.join(tipos)}); mantida a mais conservadora."

    categorias = _unicos(p["categoria"] for p in grupo)
    categoria = "contradicao" if "contradicao" in categorias else categorias[0]

    temas_grupo = _unicos(temas[i] for i in ids)
    tema = temas_grupo[0]
    nota_tema = "" if len(temas_grupo) == 1 else f"Temas divergentes no plano ({', '.join(temas_grupo)}); mantido o primeiro."

    refs = _unicos(r for p in grupo for r in (p.get("referencias_cruzadas") or []) if r not in ids)
    notas = [n for n in [nota_plano, nota_div, nota_tema] if n]

    return {
        "id_consolidado": None,
        "tema": tema,
        "ids_origem": list(ids),
        "dispositivo_editalicio": " / ".join(_unicos(p["dispositivo_editalicio"] for p in grupo)),
        "transcricao": max((p.get("transcricao") or "" for p in grupo), key=len),
        "tipo_achado": tipo,
        "categoria": categoria,
        "descricao_breve": max((p.get("descricao_breve") or "" for p in grupo), key=len),
        "dispositivo_legal": "; ".join(_unicos(p.get("dispositivo_legal") or "" for p in grupo)),
        "referencias_cruzadas": refs,
        "flag_tecnico": any(p.get("flag_tecnico") for p in grupo),
        "flag_reserva": any(p.get("flag_reserva") for p in grupo),
        "nota_consolidacao": " ".join(notas),
    }


def montar_individual(pid, origens, temas):
    p = origens[pid]
    return {
        "id_consolidado": None,
        "tema": temas[pid],
        "ids_origem": [pid],
        "dispositivo_editalicio": p["dispositivo_editalicio"],
        "transcricao": p.get("transcricao") or "",
        "tipo_achado": p["tipo_achado"],
        "categoria": p["categoria"],
        "descricao_breve": p.get("descricao_breve") or "",
        "dispositivo_legal": p.get("dispositivo_legal") or "",
        "referencias_cruzadas": list(p.get("referencias_cruzadas") or []),
        "flag_tecnico": bool(p.get("flag_tecnico")),
        "flag_reserva": bool(p.get("flag_reserva")),
        "nota_consolidacao": "",
    }


def montar_contradicao(c):
    return {
        "id_consolidado": None,
        "tema": c["tema"],
        "ids_origem": list(c.get("ids_origem") or []),
        "dispositivo_editalicio": c.get("dispositivo_editalicio") or "",
        "transcricao": c.get("transcricao") or "",
        "tipo_achado": c["tipo_achado"],
        "categoria": "contradicao",
        "descricao_breve": c.get("descricao_breve") or "",
        "dispositivo_legal": c.get("dispositivo_legal") or "",
        "referencias_cruzadas": [],
        "flag_tecnico": bool(c.get("flag_tecnico")),
        "flag_reserva": bool(c.get("flag_reserva")),
        "nota_consolidacao": "Contradição inter-documentos criada na consolidação"
        + (f" (plano: {c.get('id_sugerido')})" if c.get("id_sugerido") else ""),
    }


def chave_ordenacao(p):
    return (
        TEMA_ORDEM.index(p["tema"]),
        SEVERIDADE[p["tipo_achado"]],
        p["ids_origem"][0] if p["ids_origem"] else "ZZZ",
    )


def main():
    origens = carregar_origens()
    with open(DOCS / "C_plano.json", encoding="utf-8") as fh:
        plano = json.load(fh)

    erros = validar(plano, origens)
    if erros:
        print(f"PLANO INVÁLIDO — {len(erros)} erro(s):")
        for e in erros[:60]:
            print("  -", e)
        sys.exit(1)
    print(f"Plano válido: {len(origens)} origens, {len(plano.get('merges', []))} merges, "
          f"{len(plano.get('contradicoes', []))} contradições novas.")
    if "--validate-only" in sys.argv:
        return

    temas = plano["temas"]
    em_merge = {pid for g in plano.get("merges", []) for pid in g["ids"]}

    consolidados = []
    for g in plano.get("merges", []):
        consolidados.append(montar_merge(g["ids"], origens, temas, g.get("nota", "")))
    for pid in origens:
        if pid not in em_merge:
            consolidados.append(montar_individual(pid, origens, temas))
    for c in plano.get("contradicoes", []):
        consolidados.append(montar_contradicao(c))

    consolidados.sort(key=chave_ordenacao)
    for i, p in enumerate(consolidados, 1):
        p["id_consolidado"] = f"C-{i:03d}"

    with open(DOCS / "C_consolidado.yaml", "w", encoding="utf-8") as fh:
        fh.write("# Lista consolidada — Fase 1 — PE 30/2026 (REABERTURA) Porto Ferreira/SP [USO INTERNO]\n")
        fh.write(f"# {len(consolidados)} pontos consolidados a partir de {len(origens)} achados brutos (E1-E4)\n\n")
        yaml.safe_dump(consolidados, fh, allow_unicode=True, sort_keys=False, width=10000, default_flow_style=False)

    # Sumário
    por_tema, por_tipo = {}, {}
    for p in consolidados:
        por_tema.setdefault(p["tema"], {"IRREGULAR": 0, "DEPENDE_DE_FATO": 0, "CONFORME": 0})
        por_tema[p["tema"]][p["tipo_achado"]] += 1
        por_tipo[p["tipo_achado"]] = por_tipo.get(p["tipo_achado"], 0) + 1
    n_tec = sum(1 for p in consolidados if p["flag_tecnico"])
    n_res = sum(1 for p in consolidados if p["flag_reserva"])
    contras = [p for p in consolidados if p["nota_consolidacao"].startswith("Contradição inter-documentos")]
    n_merges = len(plano.get("merges", []))
    absorvidos = sum(len(g["ids"]) for g in plano.get("merges", []))

    with open(DOCS / "C_sumario.md", "w", encoding="utf-8") as fh:
        fh.write("# Sumário da consolidação — Fase 1 — PE 30/2026 (REABERTURA) [USO INTERNO]\n\n")
        fh.write(f"- Achados brutos (E1–E4): **{len(origens)}**\n")
        fh.write(f"- Pontos consolidados: **{len(consolidados)}** "
                 f"({n_merges} merges absorvendo {absorvidos} achados; {len(contras)} contradições novas)\n")
        fh.write(f"- Reconciliação: {len(origens)} origens = {len(consolidados) - len(contras)} pontos "
                 f"({absorvidos - n_merges} absorvidos por merge) + {len(contras)} pontos novos de contradição\n")
        fh.write(f"- Flags: {n_tec} com `flag_tecnico` (VALIDAÇÃO TÉCNICA), {n_res} com `flag_reserva` (RESERVA)\n\n")
        fh.write("## Por tipo de achado\n\n")
        for t in ["IRREGULAR", "DEPENDE_DE_FATO", "CONFORME"]:
            fh.write(f"- {t}: **{por_tipo.get(t, 0)}**\n")
        fh.write("\n## Por tema\n\n")
        fh.write("| Tema | IRREGULAR | DEPENDE_DE_FATO | CONFORME | Total |\n|---|---|---|---|---|\n")
        for t in TEMA_ORDEM:
            d = por_tema.get(t, {"IRREGULAR": 0, "DEPENDE_DE_FATO": 0, "CONFORME": 0})
            fh.write(f"| {t} | {d['IRREGULAR']} | {d['DEPENDE_DE_FATO']} | {d['CONFORME']} | {sum(d.values())} |\n")
        fh.write("\n## Contradições inter-documentos criadas na consolidação\n\n")
        for p in contras:
            fh.write(f"- **{p['id_consolidado']}** ({p['tema']}): {p['descricao_breve']} "
                     f"[origens: {', '.join(p['ids_origem'])}]\n")
        fh.write("\n## Pontos com flag de reserva estratégica [RESERVA]\n\n")
        for p in consolidados:
            if p["flag_reserva"]:
                fh.write(f"- **{p['id_consolidado']}** ({p['tema']}, {p['tipo_achado']}): {p['descricao_breve']}\n")

    print(f"Gravado: C_consolidado.yaml ({len(consolidados)} pontos) e C_sumario.md")
    print("Por tipo:", {t: por_tipo.get(t, 0) for t in ['IRREGULAR', 'DEPENDE_DE_FATO', 'CONFORME']})


if __name__ == "__main__":
    main()
