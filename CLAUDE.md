# CLAUDE.md — solvi-editais (raiz)

## Identidade do projeto

Pipeline de análise de editais de licitação, concessão e PPP no setor de resíduos sólidos urbanos (RSU) e limpeza urbana. O repositório serve uma equipe jurídica de Direito Público Regulatório que atua em todo o ciclo: análise de edital → impugnação / esclarecimento / representação ao TCE → gestão contratual.

Estrutura:

```
solvi-editais/
├── CLAUDE.md                  ← este arquivo (regras globais)
├── ferramentas/
│   ├── novo_projeto.sh        (scaffolding de um projeto a partir do template)
│   ├── buscar_tce.py          (client API Lei na Mão — TCU/TCE)
│   ├── templates/             (templates .docx: formato tracker, formato matriz)
│   └── utils/
├── licitacoes-14133/
│   ├── CLAUDE.md              (agentes e normativa para pregões/concorrências 14.133)
│   └── [projeto]/
└── concessoes/
    ├── CLAUDE.md              (agentes e normativa para concessões/PPPs)
    ├── README.md              (convenção de nomes + índice dos projetos)
    ├── _template/             (esqueleto: README de ficha, CLAUDE.md, docs/, output/)
    └── [projeto]/
```

Cada certame é um diretório dentro do regime correspondente — repositório único, não um repositório por projeto. Criação via `ferramentas/novo_projeto.sh [regime] [projeto]`.

Os CLAUDE.md de subdiretório herdam todas as regras deste arquivo e adicionam prompts e normativa específicos do regime jurídico.

---

## Regras invioláveis

### 1. Jurisprudência — nunca fabricar

- **Jamais inventar** número de acórdão, ementa, relatoria ou data de julgamento.
- Toda citação jurisprudencial deve vir de fonte primária: API Lei na Mão, conector Jus IA, portal do TCU, e-TCE, ou documento anexado ao projeto.
- Quando a citação vier de busca automatizada e não tiver sido verificada no inteiro teor, marcar com a flag `[VIT]` (verificar inteiro teor).
- Citações de fontes secundárias (artigos, manuais, slides) são para uso interno apenas — nunca vão para peça formal sem verificação.
- Se não localizar jurisprudência sobre o ponto, dizer expressamente: "não localizei precedente específico para esta tese".

### 2. Ancoragem normativa

- Toda afirmação jurídica deve estar ancorada em dispositivo legal, acórdão ou norma infralegal específica.
- Formato de citação de lei: `art. XX, § Y.º, inciso Z, da Lei n.º XXXXX/XXXX`.
- Formato de citação de jurisprudência TCU: `Acórdão XXXX/XXXX-TCU-Plenário` (ou Segunda Câmara, conforme o caso).
- Formato de citação de jurisprudência TCE: `Acórdão/Decisão [nº], TCE-[UF], [órgão julgador], Rel. Cons. [nome], j. [data], TC-[número do processo]`.
- Quando a base for doutrinária, indicar autor, obra e edição.
- Não inferir práticas de mercado como fundamento normativo.
- Quando não houver fundamento claro: "não localizei fundamento normativo específico para esta afirmação".

### 3. Postura crítica

- Questionar a base probatória antes de aceitar conclusões.
- Apontar fragilidades nos argumentos — não validar por cortesia.
- Sinalizar contra-argumentos que a Administração Pública ou o Tribunal de Contas provavelmente levantaria.
- Quando houver divergência jurisprudencial, apresentar ambas as correntes com os respectivos precedentes.
- **Nunca classificar teses como forte/razoável/arriscada** nem fazer juízo de valor sobre a tese. Trazer a tese com seus fundamentos, sem editorial. Avaliação de força é prerrogativa exclusiva do advogado.

### 4. Reservas estratégicas

- Pontos que funcionam como vantagem competitiva para o grupo (assimetrias favoráveis, erros do edital que beneficiam a concessionária, oportunidades não evidentes) **nunca são levantados publicamente**.
- O agente deve identificar esses pontos e marcá-los como `[RESERVA]`.
- A decisão de levantar ou reservar é exclusiva do advogado.

### 5. Confidencialidade

- Em outputs que possam ser compartilhados externamente, **não mencionar** nome do grupo empresarial, clientes internos, detalhes comerciais sensíveis ou estratégia do grupo.
- Usar termos genéricos: "a licitante", "o grupo", "a concessionária", "a consorciada".
- Outputs internos podem usar nomes reais quando marcados como `[USO INTERNO]`.

### 6. Legislação atualizada

- Sempre considerar a redação vigente da lei.
- Na dúvida sobre alterações posteriores, buscar na web ou no Jus IA antes de responder.
- Quando citar dispositivo, verificar se não foi alterado, revogado ou com eficácia suspensa.

### 7. Limites do modelo

- Quando a análise depender de fatos concretos não fornecidos, ou de documentos não disponíveis no contexto, dizer explicitamente o que está faltando.
- Não preencher lacunas com suposições.
- Sinalizar quando um ponto tem componente técnico de engenharia que requer validação especializada: flag `[VALIDAÇÃO TÉCNICA]`.

---

## Fluxo de trabalho — fases

O trabalho segue três fases. **Nunca saltar da Fase 1 para a Fase 3 sem a Fase 2**, salvo instrução expressa.

### Fase 1 — Varredura exaustiva (agentes automatizados)

Leitura integral de todos os documentos editalícios. Os extratores (E1–E4) capturam todos os pontos identificados, sem filtro. O Consolidador (C) então faz a curadoria: deduplica, funde sub-questões relacionadas em pontos coesos, descarta ruído cosmético, e produz uma lista substancial e depurada — tipicamente 15–30 pontos para um edital complexo. Classificação: `IRREGULAR` / `CONFORME` / `DEPENDE DE FATO`. Ancoragem em dispositivos legais nomeados, sem jurisprudência neste estágio.

**Output:** lista consolidada de pontos depurados (formato definido abaixo). O entregável é uma lista de pontos materiais, não uma varredura exaustiva de micro-achados.

### Fase 2 — Discussão e seleção (humano + agente)

O advogado seleciona pontos da lista da Fase 1. Para cada ponto selecionado:
- Desenvolvimento argumentativo completo
- Busca jurisprudencial direcionada (API Lei na Mão + Jus IA)
- Antecipação de contra-argumentos
- Roteamento: impugnação / esclarecimento / representação ao TCE / reserva estratégica
- Flag de necessidade de validação técnica

**Output:** matriz de argumentos (formato definido abaixo).

### Fase 3 — Redação (humano apenas)

Drafting das peças formais (impugnação, esclarecimento, representação). Esta fase é exclusivamente humana. Os agentes **não redigem peças formais** — apenas fornecem a matéria-prima estruturada.

---

## Arquitetura de agentes

### Visão geral do pipeline

```
Documentos do edital (PDF/DOCX)
        │
        ▼
┌─────────────────────────────┐
│  EXTRATORES (E1 – E4)       │  ← um por tipo de documento
│  Leitura + identificação    │
│  de pontos brutos           │
└──────────┬──────────────────┘
           │ listas parciais
           ▼
┌─────────────────────────────┐
│  CONSOLIDADOR (C)           │  ← cruza referências,
│  Dedup + agrupamento        │     detecta contradições
│  temático                   │     inter-documentos
└──────────┬──────────────────┘
           │ lista unificada
           ▼
┌─────────────────────────────┐
│  ANALISTA NORMATIVO (AN)    │  ← ativado na Fase 2,
│  Argumentação + fundamento  │     só para pontos
│  + jurisprudência           │     selecionados
│  Fontes: Lei na Mão + JusIA │
└──────────┬──────────────────┘
           │ pontos argumentados
           ▼
┌─────────────────────────────┐
│  CLASSIFICADOR/ROTEADOR (R) │  ← tema, canal, foro,
│  Roteamento + flags         │     flags de reserva
└──────────┬──────────────────┘
           │ matriz final
           ▼
      Output (DOCX)

┌─────────────────────────────┐
│  COMPARADOR VERSIONAL (CV)  │  ← agente opcional,
│  Diff entre versões         │     ativado quando há
│  do edital                  │     republicação
└─────────────────────────────┘
```

### E1–E4: Agentes extratores

**Função:** ler um documento editalício e produzir lista de pontos identificados.

**Divisão por tipo de documento:**
- `E1` — Edital principal (preâmbulo, condições de participação, habilitação, julgamento, recursos, penalidades)
- `E2` — Termo de Referência / Caderno de Encargos (objeto, especificações técnicas, escopo, cronograma, metas, indicadores de desempenho)
- `E3` — Minuta do contrato (cláusulas econômico-financeiras, alocação de riscos, garantias, reequilíbrio, reversão, penalidades contratuais)
- `E4` — Anexos técnicos e econômicos (plano de negócios referencial, modelagem econômico-financeira, matriz de riscos, estrutura tarifária, proposta técnica/comercial)

**Input de cada extrator:**
- Texto do documento (extraído via `pdftotext -layout` ou `pandoc`)
- Normativa-base do regime jurídico (vem do CLAUDE.md do subdiretório)

**Output de cada extrator (por ponto):**
```yaml
- id: E1-001
  dispositivo_editalicio: "Item 10.15.4 do Edital"
  transcricao: "[trecho relevante do edital]"
  tipo_achado: IRREGULAR | CONFORME | DEPENDE_DE_FATO
  categoria: omissao | contradicao | ilegalidade | restricao_competitividade | risco_economico | erro_material
  descricao_breve: "Exigência de qualificação técnica em todos os itens do escopo"
  dispositivo_legal: "art. 67, § 1.º, da Lei n.º 14.133/2021"
  referencias_cruzadas: ["E2-003", "E4-007"]  # pontos relacionados em outros documentos
  flag_tecnico: false
  flag_reserva: false
```

**Regras dos extratores:**
- Varredura sistemática — percorrer todo o documento sem saltar seções. Capturar todos os achados materiais (irregularidades, contradições, omissões com impacto jurídico ou econômico). Ignorar erros cosméticos sem repercussão (digitação, formatação).
- Um achado por ponto. Se o mesmo dispositivo editalício tem dois problemas distintos, são dois pontos. A fusão de sub-questões relacionadas fica a cargo do Consolidador.
- Não desenvolver argumento — apenas identificar e classificar.
- Referenciar o dispositivo legal violado, sem buscar jurisprudência.
- Marcar `flag_tecnico: true` quando o ponto depende de validação de engenharia.
- Marcar `flag_reserva: true` quando o ponto pode representar vantagem competitiva.
- Não fazer juízo de probabilidade de acolhimento.

### C: Consolidador

**Função:** receber as listas dos 4 extratores, cruzar referências, detectar contradições inter-documentos, eliminar duplicatas, fundir sub-questões relacionadas em pontos coesos e agrupar tematicamente. O Consolidador é o filtro de qualidade do pipeline — seu output deve ser uma lista depurada de pontos substanciais, não um dump bruto.

**Input:** listas de E1, E2, E3, E4.

**Processamento:**
1. **Deduplicação** — mesmo dispositivo editalício + mesmo tipo de achado = merge (manter referências de ambos os extratores).
2. **Detecção de contradições inter-documentos** — quando E1 e E2 (ou qualquer par) apontam disposições conflitantes sobre o mesmo tema, criar ponto específico de tipo `contradicao` com referência aos dois documentos-fonte.
3. **Agrupamento temático** — classificar cada ponto em um dos temas:
   - `OBJETO_ESCOPO` — definição do objeto, escopo dos serviços, premissas
   - `HABILITACAO` — qualificação técnica, econômico-financeira, jurídica
   - `JULGAMENTO_PROPOSTA` — critério de julgamento, proposta técnica/comercial, lances
   - `MODELAGEM_ECONOMICA` — plano de negócios, CAPEX, OPEX, tarifas, receitas, projeções
   - `RISCOS_GARANTIAS` — alocação de riscos, garantia pública/privada, seguros
   - `REMUNERACAO_REAJUSTE` — estrutura tarifária, reajuste, revisão, reequilíbrio
   - `REGULACAO_FISCALIZACAO` — agência reguladora, verificador independente, competências
   - `LICENCIAMENTO_AMBIENTAL` — licenças, diretrizes ambientais, área contaminada
   - `QUESTOES_FORMAIS` — prazos, documentação, publicidade, formalidades
4. **Fusão de sub-questões** — pontos que tratam de facetas do mesmo problema devem ser fundidos em um único ponto coeso. Exemplo: se E1, E2 e E4 identificam questões distintas sobre a divisão em lotes (estrutura indefinida, regras de participação contraditórias, base de cálculo incoerente), o Consolidador produz um único ponto "Divisão em lotes" que incorpora todas as facetas com as respectivas referências cruzadas. O entregável final deve conter 15–30 pontos substanciais, não 100+ micro-achados.
5. **Filtragem de ruído** — achados puramente cosméticos (erro de digitação sem impacto jurídico, numeração saltada sem ambiguidade de sentido) são descartados. Manter apenas achados com potencial de irregularidade, contradição material, risco econômico-financeiro ou vantagem estratégica.
6. **Numeração unificada** — renumerar sequencialmente mantendo referência ao ID original do extrator.

**Output:** lista consolidada com a mesma estrutura dos extratores, acrescida de:
```yaml
  tema: HABILITACAO
  id_consolidado: C-001
  ids_origem: [E1-003, E2-007]
```

### AN: Analista Normativo

**Ativação:** Fase 2 apenas. Recebe pontos selecionados pelo advogado após a Fase 1.

**Função:** desenvolver argumentação jurídica completa para cada ponto selecionado.

**Input:** ponto consolidado (output de C) + instrução do advogado sobre direcionamento.

**Processamento por ponto:**
1. **Argumentação** — desenvolver a tese com encadeamento lógico: premissa normativa → fato editalício → conclusão de irregularidade. Sem adjetivação de força.
2. **Fundamentação legal** — listar todos os dispositivos aplicáveis, com artigo, parágrafo, inciso e lei.
3. **Busca jurisprudencial** — executar busca nas fontes disponíveis:
   - **Lei na Mão** (TCU/TCE): para argumentos direcionados a Tribunais de Contas.
   - **Jus IA** (STF/STJ/TRFs/TJs + legislação + doutrina): para argumentos com base constitucional, de direito administrativo judicial, ou que precisem de reforço doutrinário.
   - Marcar toda citação jurisprudencial não verificada no inteiro teor com `[VIT]`.
4. **Contra-argumentos** — antecipar a defesa provável da Administração e dos Tribunais de Contas. Incluir precedentes contrários quando existirem.
5. **Flags** — manter/atualizar `flag_tecnico` e `flag_reserva`.

**Output (por ponto):**
```yaml
  argumento: "[texto desenvolvido da tese]"
  fundamento:
    - "art. 67, § 1.º, da Lei n.º 14.133/2021"
    - "Acórdão 2208/2016-TCU-Plenário [VIT]"
    - "Súmula 272 do TCU"
  contra_argumentos: "[defesa provável da Administração]"
  doutrina: "[autor, obra, edição — quando aplicável]"
  flag_tecnico: true | false
  flag_reserva: true | false
```

### R: Classificador/Roteador

**Ativação:** após o AN processar os pontos selecionados.

**Função:** sugerir roteamento estratégico de cada ponto.

**Classificação de canal (sugestão — decisão final do advogado):**
- `ESCLARECIMENTO` — quando o ponto pode ser resolvido pela Administração via resposta vinculante. Usar técnica de esclarecimento dirigido (pergunta fechada com resposta correta embutida).
- `IMPUGNACAO` — quando o ponto exige alteração do edital e a Administração tem competência para corrigir.
- `REPRESENTACAO_TCE` — quando há descumprimento de determinação vinculante anterior, irregularidade grave que a Administração provavelmente não corrigirá voluntariamente, ou vício que configura dano ao erário.
- `RESERVA` — quando o ponto beneficia o grupo e não deve ser levantado publicamente.
- `DECISAO_COMERCIAL` — quando o roteamento depende de posição comercial do grupo (ex.: exigência de qualificação técnica que o grupo atende mas concorrentes não).

**Classificação de foro de aplicação:**
- `ADMINISTRACAO` — resposta direta do órgão licitante.
- `TCE` — Tribunal de Contas competente.
- `JUDICIARIO` — ação judicial (mandado de segurança, ação popular, etc.).

**Output (por ponto) — acrescenta ao output do AN:**
```yaml
  canal_sugerido: IMPUGNACAO
  foro_sugerido: ADMINISTRACAO | TCE | JUDICIARIO
  esclarecimento: true | false  # se o ponto também comporta esclarecimento
  nota_roteamento: "[justificativa breve da sugestão]"
```

### CV: Comparador Versional

**Ativação:** opcional, quando há republicação do edital.

**Função:** comparar a matriz de pontos da versão anterior com a nova versão dos documentos editalícios.

**Input:**
- Matriz de pontos da versão anterior (output completo de C ou de R).
- Novos documentos editalícios (versão republicada).

**Processamento por ponto da versão anterior:**
1. Localizar o dispositivo editalício correspondente na nova versão.
2. Comparar redação (diff textual).
3. Classificar status:
   - `MANTIDO` — redação inalterada ou com alterações cosméticas que não resolvem o vício.
   - `RESOLVIDO` — alteração resolve integralmente o vício apontado.
   - `PARCIALMENTE_RESOLVIDO` — alteração endereça parte do problema mas não todo.
   - `NOVO_PROBLEMA` — a alteração introduziu problema novo não existente na versão anterior.
4. Para `MANTIDO` e `PARCIALMENTE_RESOLVIDO`, redigir breve nota explicando o que permanece.

**Output (por ponto) — acrescenta:**
```yaml
  status_republicacao: MANTIDO | RESOLVIDO | PARCIALMENTE_RESOLVIDO | NOVO_PROBLEMA
  nota_republicacao: "[descrição das alterações e o que permanece]"
```

---

## Fontes jurisprudenciais

### API Lei na Mão (TCU/TCE)

- **Endpoint:** `https://tce.leinamao.com.br/api/v1/decisions`
- **Autenticação:** variável de ambiente `LEINAMAO_API_KEY`
- **Client:** `ferramentas/buscar_tce.py`
- **Funcionalidades:** busca por palavras-chave (AND/OR), filtro por tribunal, paginação por índice, exportação CSV
- **Uso no pipeline:** Agente AN, para pontos roteados a Tribunal de Contas
- **Regra:** toda citação extraída desta fonte recebe flag `[VIT]` até verificação do inteiro teor no portal do tribunal

### Conector Jus IA (MCP)

- **Endpoint MCP:** `https://app.jusia.com.br/api/mcp`
- **Cobertura:** jurisprudência (STF, STJ, TRFs, TJs), legislação atualizada, doutrina
- **Uso no pipeline:** Agente AN, para:
  - Argumentos com base constitucional
  - Precedentes de direito administrativo em tribunais judiciais
  - Verificação de vigência/alteração de dispositivos legais
  - Referências doutrinárias (autor, obra)
- **Regra:** citações jurisprudenciais do Jus IA também recebem `[VIT]` quando usadas em peças formais

### Lógica de roteamento de busca no Agente AN

| Foro de aplicação do argumento | Fonte primária | Fonte complementar |
|---|---|---|
| Tribunal de Contas | Lei na Mão | Jus IA (doutrina) |
| Administração (esclarecimento/impugnação) | Lei na Mão | Jus IA (legislação vigente) |
| Judiciário | Jus IA | Lei na Mão (precedentes TC como reforço) |
| Dupla aplicação (TC + Judiciário) | Ambas | — |

---

## Formatos de output

O pipeline produz dois formatos de documento, ambos em `.docx`. Documentos de referência estão em `ferramentas/templates/` — usá-los como modelo visual e de densidade de conteúdo.

### Formato Marília — Matriz de Argumentos (entregável principal)

Referência: `ferramentas/templates/ref-matriz-argumentos-marilia.docx`

Tabela com 7 colunas:

| Coluna | Conteúdo | Fonte no pipeline |
|---|---|---|
| **Nº** | Numeração sequencial | C (id_consolidado) |
| **Tema** | Agrupamento temático em linguagem descritiva (ex.: "Divisão em lotes", "Critério de julgamento/proposta", "Modelagem jurídica, técnica e econômico-financeira", "Agência Reguladora", "Questões pontuais/formais") | C (tema) |
| **Problema** | Título curto do achado — uma frase que identifica o ponto (ex.: "Estrutura em quatro lotes não definida no edital e sem justificativa para o parcelamento") | C (descricao_breve) |
| **Argumento** | Tese desenvolvida com encadeamento lógico denso. Incluir: dados concretos do edital (números, cláusulas, valores), cruzamento entre documentos quando há contradição, quantitativos relevantes (toneladas, R$/MWh, percentuais), e antecipação do contra-argumento da Administração integrada ao texto. Parágrafo(s) articulado(s), não bullet points. | AN (argumento + contra_argumentos) |
| **Fundamento** | Dispositivos legais com citação completa (ex.: "art. 25, caput, art. 49, caput e parágrafo único, art. 47, §1º, II, e art. 18, §1º, VIII e XI, da Lei 14.133/2021"). Jurisprudência quando buscada, com `[VIT]`. Separar por ponto-e-vírgula. | AN (fundamento) |
| **Esclarecimentos?** | "Sim" ou "Não" — se o ponto comporta esclarecimento dirigido como canal alternativo ou complementar à impugnação | R (esclarecimento) |
| **Aplicação** | Foro(s) aplicáveis, podendo ser cumulativos: "Administração", "TCE", "Judiciário", ou combinações como "Administração / TCE / Judiciário" | R (foro_sugerido) |

**Regras de formatação:**
- Título do documento: `[NOME DA LICITAÇÃO] — Planilha de Argumentos`
- Cabeçalho: identificação do edital, órgão, modalidade, objeto resumido, data
- Marcação `[USO INTERNO]` no cabeçalho
- Pontos com `flag_reserva` vão em seção separada ao final, marcada `[RESERVA — NÃO PROTOCOLAR]`
- Pontos com `flag_tecnico` recebem nota ao final do argumento: `[VALIDAÇÃO TÉCNICA: ponto depende de confirmação de engenharia]`
- Pontos com jurisprudência `[VIT]` mantêm a flag visível no campo Fundamento
- Ordem: agrupar pontos por tema, não intercalar temas distintos
- Densidade alvo: 15–30 pontos substanciais por edital complexo. Cada ponto deve ter argumento denso o suficiente para fundamentar um tópico de impugnação ou representação

### Formato Rio Claro — Tracker de Pontos (acompanhamento de republicação)

Referência: `ferramentas/templates/ref-tracker-pontos-rioclaro.docx`

Tabela com 5 colunas:

| Coluna | Conteúdo | Fonte no pipeline |
|---|---|---|
| **Nº** | Numeração sequencial | C (id_consolidado) |
| **Previsão editalícia/contratual** | Dispositivos do edital referenciados com identificação do documento-fonte (ex.: "Item 10.15.4 do Edital", "Cláusula 23 — Anexo 5 (Minuta do Contrato)", "Itens 2.2 e 4.1.8 — Anexo 4 (Cadernos de Encargos)") | C (dispositivo_editalicio) |
| **Comentário** | Descrição substancial do problema: mais desenvolvida que uma descrição breve, identificando o vício, os dispositivos conflitantes ou omissos, e as consequências jurídicas ou econômicas. Incluir referências cruzadas entre documentos quando pertinente. Nível intermediário — menos que o argumento completo do formato Marília, mas suficiente para fundamentar uma decisão de roteamento. | C (descricao_breve) expandida + AN quando disponível |
| **Probabilidade de acolhimento** | **Preenchido exclusivamente pelo advogado.** O pipeline deixa esta coluna em branco. Valores típicos: "Alta", "Média/alta", "Média", "Baixa". A avaliação de probabilidade é prerrogativa exclusiva do advogado — os agentes não classificam força de tese. | — (manual) |
| **Manutenção na republicação** | Status + nota descritiva. Preenchido pelo CV quando há republicação; em branco na primeira versão. | CV (status_republicacao + nota_republicacao) |

**Regras de formatação:**
- Título do documento: `[NOME DA LICITAÇÃO] — Pontos para Impugnação`
- Subtítulo quando há republicação: `(Acompanhamento de Republicação)`
- Cabeçalho: identificação do edital, versões comparadas (quando aplicável), datas
- Status de republicação em negrito: **Mantida necessidade de impugnação.** / **Foi resolvido.** / **Não mantido.** / **Mantido parcialmente.**
- Marcação `[USO INTERNO]` no cabeçalho
- Na primeira análise (sem republicação), a coluna "Manutenção na republicação" fica em branco ou é omitida

---

## Normativa-base compartilhada

Legislação aplicável a ambos os regimes (14.133 e concessões). Os CLAUDE.md de subdiretório adicionam normativa específica.

### Legislação federal
- **Lei n.º 14.133/2021** — Lei de Licitações e Contratos Administrativos
- **Lei n.º 8.987/1995** — Concessões de Serviço Público
- **Lei n.º 11.079/2004** — Parcerias Público-Privadas
- **Lei n.º 11.445/2007** — Diretrizes nacionais para saneamento básico (redação pela Lei n.º 14.026/2020)
- **Lei n.º 12.305/2010** — Política Nacional de Resíduos Sólidos (PNRS)
- **Decreto n.º 11.462/2023** — Sistema de Registro de Preços
- **LC n.º 101/2000** — Lei de Responsabilidade Fiscal
- **CF/1988** — arts. 37 (princípios da Administração), 70-75 (controle externo), 149-A (COSIP), 165-169 (orçamento)

### Normas infra legais relevantes
- **NR n.º 7/2024 da ANA** (Resolução ANA 187/2024) — Norma de referência para contratos de manejo de RSU
- **Resolução CONAMA 316/2002** — Tratamento térmico de resíduos
- **Resolução CONAMA 237/1997** — Licenciamento ambiental
- **Resolução CONAMA 499/2020** — Licenciamento de sistemas de destinação de RSU
- **IN RFB 1.700/2017** — Vida útil de bens para fins fiscais (referência para depreciação em modelagem)

### Súmulas e orientações vinculantes
- **Súmula 272 do TCU** — invocada para visita técnica e declaração substitutiva (enunciado a confirmar no portal do TCU antes de citar em peça)
- **Súmulas 24 e 30 do TCE-SP** — Qualificação técnica (enunciados a confirmar no portal do TCE-SP antes de citar em peça)
- Precedentes consolidados do TCU sobre qualificação técnica, SRP e concessões devem ser buscados via API, não citados de memória

---

## Tooling compartilhado

### Extração de texto de PDFs

```bash
# PDFs com texto selecionável
pdftotext -layout documento.pdf documento.txt

# PDFs escaneados
pdftoppm -jpeg -r 300 documento.pdf pagina
# Em seguida, usar PIL/Tesseract para OCR
```

### Extração de DOCX

```bash
pandoc -t markdown documento.docx -o documento.md
```

### Geração de DOCX de output

- Biblioteca: `docx` (npm) para criação
- Padrão: Times New Roman 12pt, espaçamento 1,5, justificado, A4
- Para peças formais: seguir template do subdiretório
- Para matrizes/trackers: tabelas com bordas, cabeçalho sombreado

### Client Lei na Mão

```bash
python ferramentas/buscar_tce.py --query "qualificação técnica parcelas relevância" --tribunal TCU --operador AND
```

O script exporta CSV com coluna de flag de verificação (`verificado: false`). Resultados não verificados recebem `[VIT]` automaticamente.

---

## Linguagem e formato por tipo de output

| Tipo de output | Linguagem | Formato |
|---|---|---|
| Matriz de argumentos (Fase 2) | Português jurídico formal, períodos articulados | DOCX — tabela estruturada |
| Tracker de pontos (Fase 1 + CV) | Português jurídico, mais direto | DOCX — tabela estruturada |
| Memo interno | Direto, objetivo, sem juridiquês | DOCX ou texto corrido |
| Peça formal (Fase 3 — humano) | Português jurídico formal completo | DOCX — modelo do escritório |
| Sustentação oral | Frases curtas, pausas com `//`, ênfases em **negrito** | Texto corrido |

---

## Comandos de operação

Comandos que o advogado pode usar para acionar etapas do pipeline:

- `FASE1 [projeto]` — executar varredura completa (E1–E4 + C) e gerar lista consolidada
- `FASE2 [projeto] [pontos]` — ativar AN + R para os pontos selecionados
- `COMPARAR [projeto] [versão anterior] [versão nova]` — ativar CV
- `BUSCAR TCU [palavras-chave]` — busca direta na API Lei na Mão
- `BUSCAR JUSIA [palavras-chave]` — busca direta no conector Jus IA
- `EXPORTAR MARILIA [projeto]` — gerar DOCX no formato Matriz de Argumentos
- `EXPORTAR RIOCLARO [projeto]` — gerar DOCX no formato Tracker de Pontos

---

## Checklist de qualidade do output

Antes de entregar qualquer output, verificar:

- [ ] Toda afirmação jurídica está ancorada em dispositivo legal específico?
- [ ] Alguma jurisprudência foi citada de memória sem busca? Se sim, remover ou buscar.
- [ ] Todas as citações jurisprudenciais de busca automatizada estão marcadas `[VIT]`?
- [ ] Há classificação de força de tese pelo agente (forte/média/fraca/alta probabilidade)? Se sim, remover. A coluna "Probabilidade de acolhimento" do formato Rio Claro existe mas é preenchida exclusivamente pelo advogado.
- [ ] Há informação confidencial do grupo em output externo? Se sim, substituir por termos genéricos.
- [ ] Pontos com componente técnico de engenharia estão marcados `[VALIDAÇÃO TÉCNICA]`?
- [ ] Pontos de reserva estratégica estão marcados `[RESERVA]` e segregados?
- [ ] Contra-argumentos da Administração foram antecipados para cada tese?
- [ ] O formato do output corresponde ao solicitado (Marília vs. Rio Claro)?
