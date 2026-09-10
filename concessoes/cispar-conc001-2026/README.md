# cispar-conc001-2026

Edital de Concessão n.º 001/2026 — CISPAR (Alto Paranaíba/MG) — concessão comum do serviço público de manejo de resíduos sólidos urbanos de 9 municípios. Versão original (jun/2026) e republicada (set/2026).

## Layout

```
cispar-conc001-2026/
├── CLAUDE.md                          contexto específico do certame
├── docs-originais/                    arquivos originais pequenos (MEF .xlsm das duas versões, planilhas e docx internos, ENC zip)
├── docs-texto/
│   ├── original/                      texto extraído (pdftotext -layout) — um arquivo por anexo
│   │   ├── documentos-auxiliares/     contribuições da consulta/audiências, agência reguladora, parecer final e respostas
│   │   ├── internos/                  documentos internos do grupo [USO INTERNO]
│   │   └── ocr/                       digitalizações passadas por OCR (estatuto, protocolo de intenções, termos aditivos, leis municipais, jornal)
│   ├── republicado/                   idem, versão republicada (+ documentos novos: protocolos SAAE, CE 167/2026)
│   │   └── ocr/
│   └── diff-original-republicado/     diffs por palavra (formato {- removido -} {+ inserido +}) para cada anexo alterado
├── mef/                               MEF exportado para texto, um arquivo por aba (original, republicado) + diffs por aba
├── resumos/                           resumos de leitura por documento e relatórios de diff (gerados por agentes)
└── output/                            INVENTARIO_DOCUMENTAL.md, ALTERACOES_REPUBLICACAO.md e futuros outputs de FASE1/FASE2
```

Os PDFs completos (231 MB) não estão no repositório; permanecem na pasta do Google Drive "Cispar" (Original.zip e Republicado.zip). A correspondência arquivo → anexo está no inventário.

## Nomenclatura dos textos

- `00_EDITAL` — edital
- `AE01`–`AE07` — Anexos do Edital (1 modelos de cartas; 2 habilitação; 3 manual B3; 4 projeto básico referencial; 5 plano de negócios referencial; 6 cronograma; 7 minuta de contrato)
- `AC01`–`AC16` — Anexos do Contrato (1 caderno de encargos; 2 indicadores; 3 catadores; 4 tarifa; 5 matriz de riscos; 6 indenização; 7 arrolamento; 8 proposta; 9 atos constitutivos; 10 garantia; 11 seguros; 12 interdependência; 13 plano intermunicipal; 14 convênio ARISB-MG; 15 unidades de triagem; 16 conta centralizadora)
- `DA02`–`DA08` — documentos auxiliares (só na versão original)
- `ES_` — estudos socioambientais; `TA_` — 2.º termo aditivo; `PI_` — protocolo de intenções SAAE; `CE167_` — manifestação sobre dados
