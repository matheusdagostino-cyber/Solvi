# solvi-editais

Pipeline de análise de editais de licitação, concessão e PPP no setor de resíduos sólidos urbanos (RSU) e limpeza urbana.

Automatiza a varredura de documentos editalícios (edital, TR, caderno de encargos, minuta de contrato, anexos) e produz matrizes estruturadas de pontos para impugnação, esclarecimento ou representação a Tribunais de Contas.

## Estrutura

```
solvi-editais/
├── CLAUDE.md                    # instruções do pipeline (lido pelo Claude Code)
├── README.md                    # este arquivo
├── ferramentas/
│   ├── buscar_tce.py            # client da API Lei na Mão (TCU/TCE)
│   ├── templates/               # templates .docx dos formatos de output
│   └── utils/
├── licitacoes-14133/
│   ├── CLAUDE.md                # agentes para pregões e concorrências (Lei 14.133)
│   └── [projeto]/               # um diretório por edital analisado
└── concessoes/
    ├── CLAUDE.md                # agentes para concessões e PPPs (Leis 8.987 / 11.079)
    └── [projeto]/
```

## Pré-requisitos

- Conta no [Claude Code](https://claude.ai/code) com acesso ao repositório via GitHub
- Variável de ambiente `LEINAMAO_API_KEY` configurada
- Conector Jus IA habilitado na conta Claude (MCP)
- Python 3.10+ (para `buscar_tce.py`)
- Pandoc e Poppler (`pdftotext`, `pdftoppm`) instalados no ambiente

## Fluxo de trabalho

O pipeline opera em três fases:

**Fase 1 — Varredura.** Os agentes extratores leem todos os documentos do edital e produzem uma lista bruta de pontos identificados, sem filtro. O consolidador agrupa, cruza referências entre documentos e elimina duplicatas. Output: lista consolidada.

**Fase 2 — Análise.** O advogado seleciona pontos da lista. Para cada ponto selecionado, o analista normativo desenvolve o argumento, busca jurisprudência (Lei na Mão + Jus IA) e antecipa contra-argumentos. O roteador sugere canal (impugnação / esclarecimento / representação TCE) e foro. Output: matriz de argumentos.

**Fase 3 — Redação.** Exclusivamente humana. As peças formais são redigidas pelo advogado com base na matriz da Fase 2.

## Uso rápido

Dentro do Claude Code, navegue até o diretório do projeto e use os comandos:

```
FASE1 [projeto]                              → varredura completa
FASE2 [projeto] [pontos]                     → análise dos pontos selecionados
COMPARAR [projeto] [versão anterior] [nova]  → comparar versões de edital republicado
EXPORTAR MARILIA [projeto]                   → gerar .docx no formato Matriz de Argumentos
EXPORTAR RIOCLARO [projeto]                  → gerar .docx no formato Tracker de Pontos
```

## Formatos de output

| Formato | Uso | Colunas |
|---|---|---|
| **Matriz de Argumentos** (Marília) | Entregável principal de análise | Nº, Tema, Problema, Argumento, Fundamento, Esclarecimentos?, Aplicação |
| **Tracker de Pontos** (Rio Claro) | Acompanhamento de republicação de edital | Nº, Previsão editalícia, Comentário, Manutenção na republicação |

## Criando um novo projeto

1. Identifique o regime jurídico: pregão/concorrência → `licitacoes-14133/`; concessão/PPP → `concessoes/`
2. Crie um subdiretório com nome padronizado: `[municipio]-[modalidade][numero]-[ano]` (ex.: `macaiba-pe023-2026`, `marilia-conc020-2025`)
3. Coloque os documentos do edital (PDF/DOCX) dentro do subdiretório
4. Abra o Claude Code nesse diretório e execute `FASE1`

## Regras de segurança

- **Jurisprudência:** nunca é citada de memória. Toda citação vem da API Lei na Mão ou do Jus IA e recebe flag `[VIT]` (verificar inteiro teor) até confirmação.
- **Confidencialidade:** outputs externos usam termos genéricos ("a licitante", "o grupo"). Nomes internos só em documentos marcados `[USO INTERNO]`.
- **Reservas estratégicas:** pontos que beneficiam o grupo são marcados `[RESERVA]` e segregados. A decisão de levantar ou não é do advogado.
