#!/usr/bin/env python3
"""Consolida os YAML do Consolidador (C) por grupo temático na lista única da Fase 1.

Uso:
  python3 -I ferramentas/utils/consolidar_fase1.py <dir_projeto> <grupo1.yaml> [<grupo2.yaml> ...]

Lê de <dir_projeto>/output/:
  - fase1-meta.yaml         (identificação, nota metodológica, diligência externa, lacunas, pontos extras)
  - fase1-big-numbers.yaml  (big numbers curados)
Grava em <dir_projeto>/output/:
  - fase1-lista-consolidada.yaml  (numeração C-001..., formato do CLAUDE.md raiz)
  - fase1-docx.json               (insumo de ferramentas/utils/gerar_docx_fase1.js)
Imprime sobreposições de ids_origem entre pontos para revisão manual.
"""
import json
import sys
from collections import defaultdict
from pathlib import Path

import yaml

TEMAS = [
    "OBJETO_ESCOPO", "LICENCIAMENTO_AMBIENTAL", "MODELAGEM_ECONOMICA", "REMUNERACAO_REAJUSTE",
    "RISCOS_GARANTIAS", "REGULACAO_FISCALIZACAO", "HABILITACAO", "JULGAMENTO_PROPOSTA", "QUESTOES_FORMAIS",
]
TEMAS_NOMES = {
    "OBJETO_ESCOPO": "Objeto e escopo",
    "LICENCIAMENTO_AMBIENTAL": "Licenciamento e passivos ambientais",
    "MODELAGEM_ECONOMICA": "Modelagem econômico-financeira",
    "REMUNERACAO_REAJUSTE": "Remuneração, desempenho e reajuste",
    "RISCOS_GARANTIAS": "Riscos e garantias",
    "REGULACAO_FISCALIZACAO": "Regulação e fiscalização",
    "HABILITACAO": "Habilitação",
    "JULGAMENTO_PROPOSTA": "Julgamento e proposta",
    "QUESTOES_FORMAIS": "Questões formais e condições prévias",
}
TIPO_ORDEM = {"IRREGULAR": 0, "DEPENDE_DE_FATO": 1, "CONFORME": 2}
CAMPOS = [
    "id_consolidado", "tema", "ids_origem", "tipo_achado", "categoria", "descricao_breve",
    "dispositivo_editalicio", "transcricao", "comentario", "dispositivo_legal", "depende_de",
    "flag_tecnico", "flag_reserva", "reserva_tipo", "nota_reserva", "fonte_externa",
]


def main():
    proj = Path(sys.argv[1])
    out = proj / "output"
    meta = yaml.safe_load((out / "fase1-meta.yaml").read_text(encoding="utf-8"))
    big = yaml.safe_load((out / "fase1-big-numbers.yaml").read_text(encoding="utf-8"))

    pontos = []
    for f in sys.argv[2:]:
        d = yaml.safe_load(Path(f).read_text(encoding="utf-8"))
        pontos.extend(d["pontos"])
    pontos.extend(meta.get("pontos_extras", []))

    remover = set(meta.get("remover_id_tmp", []))
    pontos = [p for p in pontos if p.get("id_tmp") not in remover]
    for alvo, ajuste in (meta.get("ajustes", {}) or {}).items():
        for p in pontos:
            if p.get("id_tmp") == alvo:
                p.update(ajuste)

    for p in pontos:
        if p.get("tema") not in TEMAS:
            raise SystemExit(f"tema inválido em {p.get('id_tmp')}: {p.get('tema')}")

    pontos.sort(key=lambda p: (TEMAS.index(p["tema"]), TIPO_ORDEM[p["tipo_achado"]], p.get("id_tmp", "")))
    for i, p in enumerate(pontos, 1):
        p["id_consolidado"] = f"C-{i:03d}"

    # Sobreposições de origem (possíveis duplicatas entre grupos)
    por_origem = defaultdict(list)
    for p in pontos:
        for o in p.get("ids_origem") or []:
            por_origem[o].append(f"{p['id_consolidado']}({p.get('id_tmp')})")
    sobrepostos = {o: v for o, v in por_origem.items() if len(v) > 1}
    if sobrepostos:
        print(f"[revisar] {len(sobrepostos)} ids de origem aparecem em mais de um ponto:")
        for o, v in sorted(sobrepostos.items()):
            print(f"  {o}: {', '.join(v)}")

    lista = [{k: p.get(k) for k in CAMPOS if p.get(k) not in (None, "", [])} | {"id_tmp": p.get("id_tmp")} for p in pontos]
    (out / "fase1-lista-consolidada.yaml").write_text(
        "# [USO INTERNO] Fase 1 — lista consolidada (Consolidador C)\n"
        + yaml.safe_dump({"pontos": lista}, allow_unicode=True, sort_keys=False, width=120),
        encoding="utf-8",
    )

    docx = {
        "meta": meta["meta"],
        "nota_metodologica": meta["nota_metodologica"],
        "nota_resumo": meta["nota_resumo"],
        "big_numbers_intro": meta["big_numbers_intro"],
        "intro_irregular": meta["intro_irregular"],
        "intro_depende": meta["intro_depende"],
        "intro_reserva": meta["intro_reserva"],
        "dd": meta["dd"],
        "lacunas": meta["lacunas"],
        "big_numbers": big["big_numbers"],
        "temas": TEMAS,
        "temas_nomes": TEMAS_NOMES,
        "pontos": [
            {"id": p["id_consolidado"], **{k: p.get(k) for k in CAMPOS if k != "id_consolidado"}}
            for p in pontos
        ],
    }
    (out / "fase1-docx.json").write_text(json.dumps(docx, ensure_ascii=False, indent=1), encoding="utf-8")

    cont = defaultdict(int)
    for p in pontos:
        cont[(p["tipo_achado"], bool(p.get("flag_reserva")))] += 1
    print(f"{len(pontos)} pontos consolidados:", dict(cont))


if __name__ == "__main__":
    main()
