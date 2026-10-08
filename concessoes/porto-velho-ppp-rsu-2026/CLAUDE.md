# CLAUDE.md — PPP RSU Porto Velho/RO (Concorrência n.º [•]/2026) [USO INTERNO]

Notas do projeto. Herda o `CLAUDE.md` raiz e as regras de concessões (`concessoes-CLAUDE.md`).

## Certame
- PPP, concessão administrativa (Lei 11.079/2004), Município de Porto Velho/RO — SEINFRA. Concorrência eletrônica, menor contraprestação mensal. Prazo de 30 anos.
- Edital 2.ª versão de 08/09/2026; contraprestação mensal máxima R$ 6.505.697,97 (maio/2026); valor estimado R$ 2.311.927.627,53.
- Estudos (PMI/MIP 005/2025): Consórcio PEZCO – PSP Hub – Masterpro – Apparecido & Carvalho Pinto Advogados. O P5 (avaliação da indenização) não veio no pacote.
- Regulador: ARDPV (LC Municipal 1.013/2025). Licenciamento: municipal (SEMA) e estadual (SEDAM/RO).

## Histórico relevante
- TCE-RO, Processo 00421/2022: Acórdãos APL-TC 00068/24 e 00105/24 julgaram irregular a Concorrência 003/2021 e o Contrato 019/PGM/2024 (EcoRondônia/Marquise). O inteiro teor não está no pacote.
- A anulação segue em litígio (MS no TJRO, cautelar do TCE-RO de 25/09/2026, ACP) — fonte secundária, verificar.
- Destinação atual: aterro Ecoparque (CTR Porto Velho S.A., 51% Orizon desde 01/2023; minoritária Ecofort). Contrato 042/PGM/2023.

## Estado da análise
- Fase 1 concluída em 08/10/2026: `output/fase1-lista-consolidada.yaml` (409 pontos), `output/fase1-big-numbers.yaml`, `output/PVH-RSU_Fase1_BigNumbers_PontosImpugnaveis.docx`.
- Brutos dos extratores em `output/extratores/`; consolidação por grupo em `output/consolidacao/`.
- Para regerar: `python3 -I ferramentas/utils/consolidar_fase1.py concessoes/porto-velho-ppp-rsu-2026 concessoes/porto-velho-ppp-rsu-2026/output/consolidacao/G{1,2,3,4}_consolidado.yaml` e `node ferramentas/utils/gerar_docx_fase1.js <json> <docx>`.
- Pendente (Fase 2): seleção de pontos pelo advogado; definição da posição comercial do grupo frente ao Ecoparque (pontos DECISÃO COMERCIAL); busca jurisprudencial.
