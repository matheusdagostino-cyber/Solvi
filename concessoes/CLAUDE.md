# CLAUDE.md — concessoes/

Este arquivo herda todas as regras do `CLAUDE.md` raiz. O que está aqui são instruções específicas para análise de editais de **concessão comum** (Lei 8.987/1995), **concessão patrocinada** e **concessão administrativa** (Lei 11.079/2004) no setor de RSU e limpeza urbana.

---

## Normativa-base do regime de concessões

Além da legislação compartilhada definida no CLAUDE.md raiz, os agentes deste subdiretório devem considerar:

### Regime concessório

| Diploma | Escopo | Artigos-chave para extração |
|---|---|---|
| **Lei 8.987/1995** | Concessões comuns | arts. 2º (definições), 5º (justificativa prévia da outorga), 9º–13 (política tarifária), 14 (licitação obrigatória), 15 (critério de julgamento), 18 (edital), 19 (consórcios), 23 (cláusulas essenciais), 26 (subconcessão), 29 (encargos do poder concedente), 35–36 (extinção e reversão), 37 (encampação), 38 (caducidade) |
| **Lei 11.079/2004** | PPPs | arts. 2º (definições), 4º (diretrizes), 5º (cláusulas essenciais), 6º (contraprestação), 7º (condições para contraprestação), 8º (garantia das obrigações pecuniárias do parceiro público), 9º (SPE), 10 (condições prévias à licitação), 11 (edital), 12 (procedimento e julgamento), 16–21 (FGP), 22 (limite fiscal da União — 1% da RCL), 28 (limite de 5% da RCL para PPPs dos entes) |
| **Lei 14.133/2021** | Aplicação subsidiária | arts. 5º (publicidade e vinculação), 23 (orçamento estimado), 25 (conteúdo do edital), 37 (banca de especialistas), 63 (visita técnica), 67 (qualificação técnica), 96–97 (garantia de execução) |

### Saneamento e RSU

| Diploma | Escopo | Artigos-chave |
|---|---|---|
| **Lei 11.445/2007** (redação Lei 14.026/2020) | Saneamento básico | arts. 10 (licitação e contrato de concessão obrigatórios), 10-A (cláusulas essenciais dos contratos), 11 (condições de validade), 21–22 (entidade reguladora), 29 (estrutura tarifária), 35 (taxas e tarifas de RSU), 50 (condicionantes de acesso a recursos federais) |
| **Lei 12.305/2010** (PNRS) | Resíduos sólidos | arts. 3º (definições), 9º e §1º (ordem de prioridade vinculante), 13 (classificação), 19 (PMGIRS), 20 e 27 (responsabilidade do gerador; art. 27, §2º — remuneração ao poder público pelas etapas que realizar), 33 (logística reversa), 36 (deveres do titular do serviço público) |
| **NR n.º 7/2024 da ANA** (Resolução ANA 187/2024) | Contratos de manejo de RSU | arts. 2º (escopo), 8º (instalações licenciadas), 34–36 (tarifas/reajuste/revisão), 35 (reciclagem antes de tratamento), 40–41 (recuperação energética condicionada), 71/76/80/88 (entidade reguladora) — atribuições de artigo não conferidas em fonte primária; verificar no texto oficial da ANA antes de citar em peça |

### Ambiental

| Diploma | Escopo | Artigos-chave |
|---|---|---|
| **Resolução CONAMA 237/1997** | Licenciamento ambiental geral | arts. 2º, 3º, 8º (LP, LI, LO) |
| **Resolução CONAMA 316/2002** | Tratamento térmico de resíduos | parâmetros de incineração, monitoramento |
| **Resolução CONAMA 499/2020** | Destinação de RSU | licenciamento de aterros, CTRs |
| **Legislação estadual aplicável** | Varia por projeto | Verificar no CLAUDE.md do projeto específico (ex.: Dec. Estadual 8.468/76 em SP, Lei 13.577/2009-SP para áreas contaminadas) |

### Orçamento e planejamento

| Diploma | Escopo | Artigos-chave |
|---|---|---|
| **LC 101/2000** (LRF) | Responsabilidade fiscal | arts. 5º, 16–17 (adequação orçamentária) — o limite de despesa com PPP sobre a RCL não está na LRF: é o art. 28 da Lei 11.079/2004 |
| **CF/1988** | PPA, LDO, LOA | arts. 165–169; art. 149-A (COSIP); art. 167 IV (não vinculação de receitas) |

---

## Prompts dos agentes — especializados para concessões

Os agentes seguem a arquitetura definida no CLAUDE.md raiz (E1–E4, C, AN, R, CV). Abaixo estão as instruções específicas de cada agente para o regime concessório.

### E1: Extrator do Edital Principal

**Documento-alvo:** edital propriamente dito (preâmbulo, condições gerais, habilitação, julgamento, recursos).

**Checklist de extração — verificar cada item:**

**Modalidade e enquadramento:**
- Identificar se é concessão comum, patrocinada ou administrativa
- Verificar se a modalidade está correta para o objeto (art. 2º da Lei 11.079/2004 — PPP exige contraprestação pecuniária; concessão comum pressupõe tarifa ao usuário)
- Confirmar prazo: concessão comum sem limite fixo na lei, PPP entre 5 e 35 anos (art. 5º, I, da Lei 11.079/2004)

**Condições prévias à licitação (PPP — art. 10 da Lei 11.079/2004):**
- [ ] Autorização da autoridade competente, fundamentada em estudo técnico (art. 10, I)
- [ ] Estudo técnico que demonstre conveniência e oportunidade (art. 10, I, "a")
- [ ] Autorização legislativa específica — exigível apenas para concessão patrocinada com mais de 70% da remuneração paga pela Administração (art. 10, §3º)
- [ ] Estimativa de impacto orçamentário-financeiro nos exercícios de vigência (art. 10, II)
- [ ] Declaração do ordenador de despesas de compatibilidade com a LDO e previsão na LOA (art. 10, III)
- [ ] Licença ambiental prévia ou diretrizes para o licenciamento (art. 10, VII)
- [ ] Objeto previsto no PPA em vigor (art. 10, V, e CF art. 165, §1º)
- [ ] Submissão da minuta de edital e de contrato à consulta pública (art. 10, VI)
- [ ] Limite de 5% da RCL para despesas com PPPs de Estados/DF/Municípios (art. 28 da Lei 11.079/2004); para a União, 1% da RCL (art. 22 da mesma lei)

**Participação e consórcio:**
- Regras de participação: verificar se admite consórcio e em que condições
- SPE: verificar exigência de constituição antes da assinatura (art. 9º da Lei 11.079/2004, art. 20 da Lei 8.987/1995)
- Contradições entre consórcio e SPE (ver padrão Marília ponto 23: confusão entre consórcio-licitante e consórcio-parceiro-privado)

**Qualificação técnica:**
- Exigência restrita às parcelas de maior relevância (art. 67, §1º, da Lei 14.133/2021, aplicável subsidiariamente)
- Prazo mínimo de execução em atestados: cabível só para serviços contínuos, limitado a 3 anos, admitidos períodos sucessivos ou não (art. 67, §5º) — exigência editalícia de consecutividade dos atestados não tem amparo no dispositivo e é vício a capturar
- Quantitativos de atestados: verificar proporcionalidade e justificativa
- Exigência de experiência em tecnologias que o próprio edital admite não ter operação comercial no Brasil (contradição interna — ver padrão Marília ponto 16)

**Qualificação econômico-financeira:**
- Índices contábeis: verificar justificativa e compatibilidade setorial
- Grau de endividamento: parâmetro do TCE-SP é ≤ 1,00 como aceitável
- Capital social mínimo ou patrimônio líquido: verificar percentual sobre o valor estimado

**Critério de julgamento:**
- Menor tarifa, menor contraprestação, melhor combinação (art. 15 da Lei 8.987/1995, art. 12 da Lei 11.079/2004)
- Técnica e preço: verificar banca de especialistas (art. 37, II, da Lei 14.133/2021), critérios objetivos de pontuação, metodologia de execução vs. proposta técnica
- Fórmula de julgamento: verificar coerência interna (ver padrão Marília ponto 5 — fórmula escrita de quatro formas diferentes)

**Visita técnica:**
- Deve admitir substituição por declaração do responsável técnico (art. 63, §§2º a 4º, da Lei 14.133/2021; Súmula 272/TCU)
- Exigência antecipada de compromisso de consórcio para visita: restritiva (ver padrão Marília ponto 24)

**Garantias:**
- Garantia de proposta e de execução: modalidades admitidas (art. 96 da Lei 14.133/2021)
- Título de capitalização como garantia: verificar existência real no mercado (ver padrão Marília ponto 20)

**Prazos e formalidades:**
- Canal de protocolo de impugnação/esclarecimento: verificar coerência entre edital e portal eletrônico
- Prazo de impugnação: verificar dispositivo legal que fundamenta
- Exigências documentais: autenticação, consularização vs. apostilamento de Haia (Decreto 8.660/2016)

### E2: Extrator do Termo de Referência / Caderno de Encargos

**Documentos-alvo:** TR, cadernos de encargos, cadernos técnicos.

**Checklist de extração:**

**Objeto e escopo:**
- Definição precisa do objeto (quais serviços são obrigatórios, quais são condicionais)
- Contradições sobre obrigatoriedade de componentes (ver padrão Rio Claro ponto 1: URE obrigatória no item 4.1.8 mas ausente no item 2.2)
- Indefinição sobre premissas essenciais (regionalização de aterro, compartilhamento de infraestrutura)
- Divisão em lotes: justificativa técnica e econômica, definição do conteúdo de cada lote (ver padrão Marília pontos 1–4)

**Especificações técnicas:**
- Coerência de parâmetros técnicos entre documentos (umidade de CDR, composição gravimétrica, balanço de massa, dimensionamento de equipamentos)
- Exigências técnicas contratualmente vinculantes sem base no próprio projeto (ver padrão Marília ponto 15: teor de cloro sem separação óptica prevista)
- Idade e especificação de frota e equipamentos: coerência entre TR e caderno de encargos (ver padrão Rio Claro ponto 18)
- Metas contratuais: coerência de prazos entre documentos (ver padrão Rio Claro ponto 17)

**Indicadores de desempenho:**
- Base de avaliação coerente com o plano de negócios referencial
- Investimentos previstos no escopo mas ausentes do plano de negócios (ver padrão Rio Claro ponto 8: ETE, compostagem, URE sem previsão)
- Metas de desvio de aterro aritmeticamente possíveis (ver padrão Marília ponto 14: digestato sem desidratação aumenta massa aterrada)

**Remuneração e estrutura tarifária:**
- Modelo: tarifa ao usuário vs. contraprestação pública vs. misto
- Grandes geradores: responsabilidade do próprio gerador (arts. 20 e 27 da Lei 12.305/2010; art. 27, §2º — etapas realizadas pelo poder público são remuneradas pelo gerador), não do erário (ver padrão Rio Claro ponto 2)
- Preço público vs. tarifa: insegurança jurídica na nomenclatura (ver padrão Rio Claro ponto 2)
- Receitas acessórias futuras e incertas incluídas na proposta comercial: gera desigualdade (ver padrão Rio Claro ponto 9)

**Licenciamento ambiental:**
- LP, LI, LO: qual fase existe, qual é exigida, qual está em andamento
- Diretrizes para licenciamento vs. licença efetiva (art. 10, VII, da Lei 11.079/2004)
- Área potencialmente contaminada: existência de investigação confirmatória
- Coerência entre documentos sobre qual licença é referenciada (ver padrão Rio Claro ponto 12: LP no contrato, LI no caderno de encargos)

**Regulação e fiscalização:**
- Entidade reguladora designada: exigência da Lei 11.445/2007 (art. 21) e NR 7/2024 (arts. 71, 76, 80, 88)
- Independência decisória e autonomia da entidade
- Divisão de competências entre poder concedente, entidade reguladora e verificador independente: verificar coerência (ver padrão Rio Claro ponto 15)
- Funções indelegáveis da entidade reguladora segundo a NR 7/2024

**Compatibilidade com PNRS e PMGIRS:**
- Ordem de prioridade: não geração → redução → reutilização → reciclagem → tratamento → disposição final ambientalmente adequada dos rejeitos (art. 9º da Lei 12.305/2010)
- Rota térmica: verificar se reciclagem foi esgotada antes do tratamento (ver padrão Marília ponto 17)
- Coerência com o PMGIRS do município (ver padrão Marília ponto 17: PMGIRS não menciona gaseificação/pirólise)
- Condições da NR 7/2024 para recuperação energética: arts. 35, 40, 41

### E3: Extrator da Minuta do Contrato

**Documento-alvo:** minuta do contrato de concessão / contrato de PPP.

**Checklist de extração:**

**Cláusulas econômico-financeiras:**
- Estrutura tarifária e mecanismo de reajuste (índice, periodicidade, data-base)
- Revisão ordinária e extraordinária: competência (poder concedente vs. entidade reguladora)
- Fator de qualidade (Fator Q): quem calcula, base de dados, consequências
- Reequilíbrio econômico-financeiro: gatilhos, procedimento, prazo de resposta

**Alocação de riscos:**
- Matriz de riscos: verificar se existe e se está preenchida (caso já observado em certame anterior: anexo de matriz de riscos publicado em branco)
- Risco regulatório: edição ou modificação de normas da entidade reguladora não pode ser excluída de reequilíbrio — lógica do fato do príncipe; a norma de referência da ANA aplicável deve ser identificada com número e artigo no texto oficial antes de citar (não usar "NR 5" sem verificação) (ver padrão Rio Claro ponto 14)
- Risco de demanda
- Risco cambial e de taxa de juros
- Risco ambiental e de licenciamento
- Risco de força maior e caso fortuito

**Garantias:**
- Garantia pública (PPP): mecanismo definido e constituído, não apenas previsto para o futuro
- FGP municipal: verificar se existe lei criadora ou se depende de legislação futura (ver padrão Marília ponto 19)
- Contradições de montante (TR vs. contrato) e de momento (antes da assinatura vs. encaminhamento de PL)
- Vinculação de receitas: FPM, ICMS, COSIP têm destinação constitucional própria (art. 167, IV, CF)
- Garantia privada: modalidades admitidas, título de capitalização (ver padrão Marília ponto 20)

**SPE:**
- Exigência de constituição antes da assinatura (art. 9º da Lei 11.079/2004)
- Composição societária: coerência com regras de consórcio
- Subsidiária integral vs. participação plural (ver padrão Marília ponto 23)

**Bens reversíveis e extinção:**
- Lista de bens reversíveis: coerente com o escopo contratual
- Critério de indenização: valor residual contábil, reavaliação, fluxo de caixa descontado
- Risco de dupla remuneração: amortização na tarifa + indenização na reversão (ver padrão Marília ponto 6)

**Penalidades:**
- Proporcionalidade das penalidades
- Penalidades por descumprimento de obras: coerência com informações disponíveis sobre as obras (ver padrão Rio Claro ponto 12)

### E4: Extrator dos Anexos Técnicos e Econômicos

**Documentos-alvo:** plano de negócios referencial, modelagem econômico-financeira, DRE projetada, matriz de riscos, anexos de proposta comercial, estudos técnicos.

**Checklist de extração:**

**Plano de negócios referencial:**
- Data-base dos estudos: verificar atualidade (parâmetro TCE-SP: 6 meses) (ver padrão Rio Claro ponto 5, Marília ponto 12)
- Premissas macroeconômicas: compatíveis com a data da sessão
- CAPEX: verificar contra referências do próprio edital e de mercado (ver padrão Marília ponto 13)
- OPEX: idem
- Projeção de receitas: verificar premissas de geração de energia, preço de venda (ver padrão Marília ponto 13: R$ 682/MWh vs. R$ 549/MWh do leilão A-5/2021)
- Inconsistências internas: valores idênticos onde deveriam ser diferentes, cronologias incompatíveis (ver padrão Rio Claro ponto 13)
- Investimentos previstos no escopo mas ausentes do plano de negócios

**Proposta comercial:**
- Componentes da proposta: clareza sobre o que é precificado, o que é declaratório e o que é informativo
- Base de cálculo: verificar se o denominador é coerente com o objeto de cada lote (ver padrão Marília ponto 7)
- Teto: verificar memória de cálculo e adequação (ver padrão Marília pontos 7 e 13)
- Desempate: critério definido e objetivo

**Value for Money / PSC (PPP):**
- Comparação PSC × PPP: quantitativa com VPL, taxa de desconto, memória de cálculo — não apenas qualitativa com adjetivos (ver padrão Marília ponto 11)
- Custo evitado vs. economia líquida: verificar se a contraprestação da PPP foi abatida (ver padrão Marília ponto 11)

**Balanço de massa e parâmetros técnicos:**
- `[VALIDAÇÃO TÉCNICA]` — estes itens devem ser flagados para revisão de engenharia:
- Produção de biogás/biometano: coerência com composição e produção específica
- Volume de digestato: considerar diluição na via úmida
- Geração líquida de energia: descontar energia de secagem, considerar umidade de entrada
- Volume de rejeitos: comparar declarado vs. calculável pelo balanço
- Capacidade da caldeira vs. CDR produzido por dia
- Meta de desvio de aterro: aritmeticamente possível considerando o balanço completo

**Determinações anteriores do TCE:**
- Verificar se o município já foi objeto de determinações em certames anteriores sobre o mesmo objeto (ver padrão Marília ponto 10)
- Verificar cumprimento de cada determinação no novo edital
- Registrar descumprimento reiterado de decisão vinculante como fato autônomo, com identificação precisa da determinação descumprida (processo, acórdão, item) — a valoração do peso do argumento é do advogado

---

## Padrões recorrentes de irregularidade em concessões de RSU

Padrões extraídos de análises anteriores. Os agentes devem verificar a ocorrência de cada um:

### Contradição interna entre documentos
O edital de concessão tipicamente contém 10+ documentos (edital, TR, cadernos, minuta, anexos). Contradições entre eles são frequentes e configuram irregularidade autônoma (art. 5º da Lei 14.133/2021 — vinculação ao instrumento convocatório). O Consolidador (C) deve cruzar sistematicamente: edital × TR, TR × caderno de encargos, TR × minuta do contrato, caderno de encargos × plano de negócios, edital × anexo de proposta.

### Incineração proibida mas prevista
Editais de WtE frequentemente proíbem "incineração" textualmente mas descrevem processos que configuram incineração segundo a Resolução CONAMA 316/2002 (queima controlada de CDR em caldeira de grelha, 850–1.050°C, residência de gases ≥ 2 segundos). Formular a tese como contradição interna do edital, não como inadequação da tecnologia em si (o TCE-SP rejeitou a linha genérica da inadequação em 2019 — localizar o precedente via API antes de citar).

### Entidade reguladora ausente
A Lei 11.445/2007 (art. 21) e a NR 7/2024 exigem designação de entidade reguladora com independência decisória. Municípios pequenos e médios frequentemente omitem essa designação ou atribuem a função ao próprio poder concedente, sem autonomia. Condição de validade do contrato.

### Garantia pública inexistente
Em PPPs, a garantia de pagamento é o núcleo da bancabilidade. Padrão recorrente: o edital prevê FGP municipal "a ser criado por lei específica" — o fundo não existe e depende de ato legislativo futuro. Alternativas (cessão de recebíveis, vinculação de COSIP/FPM/ICMS) têm restrições constitucionais.

### Modelo econômico-financeiro defasado
Parâmetro do TCE-SP: 6 meses de atualidade para orçamentos de referência. Em concessões de 20–35 anos, a defasagem da data-base afeta CAPEX, OPEX, projeções de demanda, condições de financiamento, WACC e TIR. Não é sanável por simples aplicação de índice de correção.

### Teto derivado do custo atual de aterro
Padrão Marília: o preço máximo da PPP é igual ao custo atual de destinação em aterro. O parâmetro de vantajosidade passa a ser o próprio custo que a PPP deveria superar — circularidade lógica. Demonstrar ausência de economia líquida.

### SRP para serviço essencial contínuo
Quando aparece em concessões complementares ou contratos acessórios dentro do projeto: SRP é estruturalmente incompatível com demanda certa e permanente (art. 82 da Lei 14.133/2021). Eixo de impugnação consolidado.

### Exigência de experiência em tecnologia inexistente no país
O edital exige comprovação de operação comercial de rota tecnológica que o próprio caderno técnico reconhece não ter plantas em regime comercial no Brasil. A tese não é "a tecnologia é inadequada" — é "a exigência de habilitação é contraditória com o próprio objeto".

---

## Esclarecimento dirigido — técnica específica para concessões

Em concessões, o esclarecimento tem função estratégica adicional: a resposta vincula a Administração e pode ser usada como prova em eventual representação ao TCE ou ação judicial. A técnica é formular perguntas fechadas com a resposta juridicamente correta embutida, forçando a Administração a se posicionar.

**Modelo:**

> "Considerando que o item [X] do Edital prevê [transcrição], e que o item [Y] do [Caderno/TR/Contrato] dispõe [transcrição contrária], solicita-se esclarecimento sobre qual das disposições prevalece para fins de elaboração da proposta, tendo em vista que [princípio/dispositivo legal] exige [consequência normativa]."

O agente R, ao marcar `esclarecimento: true`, produz o esboço da pergunta dirigida no campo `esboco_esclarecimento`, seguindo o modelo acima. O esboço é matéria-prima (estrutura e elementos da pergunta); o texto protocolável é redigido pelo advogado na Fase 3. Os esboços são reunidos em seção própria ao final do DOCX Marília ("Esclarecimentos dirigidos — matéria-prima").

---

## Instruções para o Comparador Versional (CV) em concessões

Editais de concessão são frequentemente republicados após impugnações, esclarecimentos ou recomendações do TCE. A comparação versional deve:

1. **Não presumir resolução** — mesmo que a redação tenha mudado, verificar se a mudança resolve efetivamente o vício identificado. Alteração cosmética (reorganização de itens, mudança de numeração) sem alteração substantiva = `MANTIDO`.

2. **Verificar efeitos colaterais** — alterações em um documento podem criar contradições novas com outros documentos que não foram alterados. Classificar como `NOVO_PROBLEMA`.

3. **Atenção a retrocessos** — verificar se correções da versão anterior foram revertidas na republicação.

4. **Manter rastreabilidade** — para cada ponto, preencher `dispositivo_v_anterior`/`dispositivo_v_nova` e as transcrições correspondentes no output (campos definidos no CLAUDE.md raiz).

---

## Criando um projeto de concessão

```bash
# Exemplo: Concessão de RSU de Rio Claro, Edital 32/2026 (concorrência, concessão comum)
ferramentas/novo_projeto.sh concessao rio-claro-conc032-2026

# Colocar os documentos do edital em docs/
# O Claude Code lerá o CLAUDE.md raiz + este arquivo + o CLAUDE.md do projeto
```

O script copia `concessoes/_template/`. Convenção de nome e índice dos projetos em `concessoes/README.md`.

Estrutura do projeto:
```
concessoes/rio-claro-conc032-2026/
├── README.md          # ficha do certame: órgão, objeto, datas, versões, status
├── CLAUDE.md          # notas específicas do projeto (ver abaixo)
├── docs/
│   ├── edital.pdf
│   ├── termo-referencia.pdf
│   ├── caderno-encargos.pdf
│   ├── minuta-contrato.pdf
│   ├── plano-negocios.pdf
│   ├── matriz-riscos.pdf
│   ├── [demais anexos]
│   ├── extraido/      # saída de pdftotext/pandoc
│   └── v2/            # documentos da republicação, quando houver (input do agente CV)
└── output/
    ├── v1/
    │   ├── fase1-triagem.yaml            # tabela arquivo → extrator + pendências
    │   ├── fase1-extratores/             # listas parciais por documento (persistência incremental)
    │   ├── fase1-lista-consolidada.yaml
    │   ├── fase2-selecao.yaml            # pontos selecionados + direcionamento do advogado
    │   ├── fase2-matriz-argumentos.yaml
    │   └── [exports .docx]
    └── v2/                               # criado na republicação — espelha docs/v2/
        ├── cv-v1-v2.yaml                 # output do CV
        └── [exports .docx atualizados]
```

O `CLAUDE.md` do projeto individual é opcional e serve para registrar contexto que não está nos documentos: determinações anteriores do TCE sobre o mesmo município/objeto, legislação estadual aplicável, histórico de impugnações em versões anteriores, informações comerciais do grupo sobre atestados disponíveis.
