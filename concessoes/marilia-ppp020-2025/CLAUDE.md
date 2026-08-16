# CLAUDE.md — marilia-ppp020-2025

Herda o `CLAUDE.md` da raiz (regras invioláveis, fluxo de fases, arquitetura de agentes) e o `CLAUDE.md` de `concessoes/` (normativa concessória, checklists E1–E4, padrões recorrentes).

Contexto extra-editalício deste certame. Informação que está nos documentos do edital não é repetida aqui.

---

## Legislação estadual e municipal aplicável

| Diploma | Escopo | Relevância para a análise |
|---|---|---|
| Dec. Estadual 8.468/1976 (SP) | Padrões ambientais | Emissões do tratamento térmico |
| Lei Estadual 13.577/2009 (SP) | Áreas contaminadas | Antiga área de disposição usada no empreendimento |
| Lei Estadual 12.300/2006 (SP) | PERS | Compatibilidade da rota tecnológica |
| PMGIRS de Marília | `[não levantado]` — verificar se menciona gaseificação/pirólise | Padrão Marília ponto 17 da matriz de 2026 |

## Autorização legislativa e instrumentos de planejamento

- Lei municipal autorizativa da PPP: `[não levantado]` — **verificar**: concessão administrativa; se contraprestação >70% paga pela Administração, exige lei específica (art. 10, §3º, Lei 11.079/2004)
- Lei do FGP ou fundo garantidor municipal: `[não levantado]` — padrão recorrente: FGP "a ser criado por lei"
- Inclusão no PPA / LDO / LOA: `[não levantado]`
- Consulta/audiência pública (art. 10, VI): `[não levantado]`

## Determinações anteriores do TCE sobre o mesmo município/objeto

**Fonte primária disponível**: `docs/subsidios/706644.pdf` — inteiro teor do Exame Prévio de Edital, **TC-001718.989.19-7**, TCE-SP, Tribunal Pleno, sessão de 13/03/2019, Rel. Cons. Dimas Ramalho. Representante: Revita Engenharia S.A. Objeto: Concorrência 009/2018 da Prefeitura de Marília — mesmo objeto do certame atual (tratamento e aproveitamento energético de RSU, gaseificação/pirólise, 30 anos).

**Julgamento: PROCEDÊNCIA PARCIAL**, com determinação de retificação do edital para:

| # | Determinação | Cumprida no edital atual? |
|---|---|---|
| 1 | Disponibilizar detalhamento dos custos, estudos e projetos, premissas e referências macroeconômicas que demonstrem as vantagens das tecnologias adotadas | `[verificar na FASE1]` |
| 2 | Detalhar os critérios do teor de umidade dos resíduos em cada fase do processo | `[verificar na FASE1]` |
| 3 | Informar a previsão das receitas acessórias | `[verificar na FASE1]` |
| 4 | Prever especificações e tipos de licenças ambientais necessárias | `[verificar na FASE1]` |
| 5 | Definir responsabilidades sobre entrega/segregação dos resíduos e cada etapa da coleta à destinação final | `[verificar na FASE1]` |
| 6 | Disponibilizar descritivo técnico de efluentes líquidos e rejeitos (m³/dia) tratados por terceiros | `[verificar na FASE1]` |
| 7 | Informar especificações de desempenho, inclusive do sistema de conversão energética acoplado à gaseificação | `[verificar na FASE1]` |

Os extratores devem verificar item a item o cumprimento dessas determinações no edital atual — descumprimento é registrado como fato autônomo com referência ao TC-001718.989.19-7 (citação verificada no inteiro teor: **sem flag [VIT]**, fonte em mãos).

## Histórico de impugnações e esclarecimentos

| Data | Autor | Objeto | Resposta da Administração | Efeito no edital |
|---|---|---|---|---|
| 2019 | Revita Engenharia S.A. | Representação TCE-SP contra a Concorrência 009/2018 | — | Procedência parcial (ver acima) |
| 12/08/2026 | Equipe interna | Planilha de argumentos, 27 pontos (CP 020/2025) | — | Matriz de referência do formato Marília |

A planilha de 12/08/2026 (`ferramentas/templates/ref-matriz-argumentos-marilia.docx`) é trabalho já curado da equipe sobre **este mesmo certame**. A FASE1 automatizada roda de forma independente; na consolidação, o C cruza a lista nova com os 27 pontos existentes e sinaliza convergências e achados inéditos.

## Subsídios técnicos disponíveis `[USO INTERNO]`

Em `docs/subsidios/` (não são documentos editalícios — não entram na varredura E1–E4; são insumo do AN na Fase 2 e da Fase 3):

| Arquivo | Conteúdo | Uso |
|---|---|---|
| `comentarios-eleusis-marilia.docx` | Análise técnica/ambiental (engenharia): falhas legais e ambientais das rotas de digestão anaeróbia e gaseificação/pirólise, com base nos próprios documentos do certame | Resolve pontos `[VALIDAÇÃO TÉCNICA]`; subsídio da Fase 2 |
| `anexo-i-ure-joinville.docx` | Estudo de caso URE Joinville | Anexo técnico para peça (Fase 3) |
| `anexo-ii-fontes-bibliograficas-digestao.docx` | Fontes bibliográficas — digestão anaeróbia | Anexo de peça (Fase 3) |
| `anexo-iii-fontes-bibliograficas-gaseificacao.docx` | Fontes bibliográficas — gaseificação | Anexo de peça (Fase 3) |
| `706644.pdf` | Inteiro teor TCE-SP TC-001718.989.19-7 (2019) | Fonte primária das determinações anteriores |
| `civap/` | Base documental da CP 001/2021 do CIVAP (PPP análoga contratada a R$ 85/t em 2022) — edital, TR, contrato, impugnações Revita/Energy com julgamentos, dossiê societário da SPE | Benchmark fático de preço e paradigma de definição para o AN (ver `civap/README.md`); nunca citar como fundamento normativo |

## Pontos que dependem de validação de engenharia `[VALIDAÇÃO TÉCNICA]`

| Ponto | Questão técnica | Enviado em | Retorno |
|---|---|---|---|
| (a preencher na FASE1) | | | Parecer Eleusis já disponível em `docs/subsidios/` — cruzar antes de reenviar à engenharia |

## Notas de leitura

- Todos os 20 PDFs têm camada de texto (sem OCR necessário); extração em `docs/extraido/`.
- `CADERNO II - Anexo 1 - DRE.xlsx` tem **20 abas** (Índice, LOTE 1/2/3, Premissas, Apoio, VfM, OPERACIONAL, Receitas, Capex/CAPEX_Input, Opex/OPEX Input, MacroEco, Output BIO+GAS, DRE por rota, Tributação) — E4 deve ler todas, não só a primeira.
- O edital menciona LOTES na planilha (abas LOTE 1/2/3) — tema central da matriz de 2026 (pontos 1–4: divisão em lotes indefinida).
- Existem **duas versões do edital** no conjunto: `EDITAL -ASSINADO.pdf` (operativo) e `CADERNO III - ANEXO I - MINUTA DE EDITAL.pdf` (minuta do estudo). O E1 lê ambos e aponta divergências entre minuta e versão assinada.
