# CLAUDE.md — licitacoes-14133/

Este arquivo herda todas as regras do `CLAUDE.md` raiz. O que está aqui são instruções específicas para análise de editais de **pregão** e **concorrência** regidos pela **Lei n.º 14.133/2021** (contratação de serviços de limpeza urbana, coleta, transporte, destinação de RSU e correlatos), incluindo certames com **Sistema de Registro de Preços**.

---

## Normativa-base do regime 14.133

Além da legislação compartilhada definida no CLAUDE.md raiz, os agentes deste subdiretório devem considerar:

| Diploma | Escopo | Artigos-chave para extração |
|---|---|---|
| **Lei 14.133/2021** | Regime geral | arts. 6º (definições), 18 (fase preparatória e ETP), 23 (valor estimado compatível com mercado), 25 (conteúdo do edital), 28 (modalidades), 33 (critérios de julgamento), 55 (prazos mínimos de divulgação), 62–70 (habilitação), 67 (qualificação técnico-profissional e técnico-operacional), 69 (qualificação econômico-financeira), 82–86 (SRP), 92 (cláusulas necessárias do contrato), 96–102 (garantias), 124–136 (alteração e equilíbrio), 155–163 (infrações e sanções), 164 (impugnação e esclarecimento — 3 dias úteis), 165–168 (recursos) |
| **Decreto 11.462/2023** | SRP federal (referência) | disciplina do registro de preços; verificar o regulamento local aplicável ao órgão licitante |
| **LC 123/2006** | ME/EPP | arts. 42–49 (tratamento diferenciado, empate ficto, cota reservada) |
| **Lei 12.305/2010 (PNRS)** | Resíduos sólidos | mesmos artigos-chave da tabela de `concessoes/CLAUDE.md` |

> As atribuições de artigo desta tabela seguem a redação vigente conhecida, mas **antes de citar em peça formal, confirmar o dispositivo na redação atual via Jus IA** (regra inviolável 6). Prefeituras frequentemente aplicam regulamentos municipais próprios da 14.133 — verificar no CLAUDE.md do projeto.

---

## Checklists dos extratores — especializados para 14.133

Os agentes seguem a arquitetura definida no CLAUDE.md raiz (E1–E4, C, AN, R, CV). Checklists específicos:

### E1: Edital principal

**Modalidade e enquadramento:**
- Modalidade compatível com o objeto (pregão para serviços comuns; concorrência quando houver critério técnico)
- Critério de julgamento e modo de disputa definidos e coerentes entre preâmbulo, corpo e anexos
- Prazos mínimos de divulgação respeitados (art. 55) — contar da última republicação
- Prazo e canal de impugnação/esclarecimento coerentes com o art. 164 (3 dias úteis) e funcionais no portal indicado

**SRP (quando houver):**
- Compatibilidade estrutural do SRP com o objeto: serviço essencial contínuo com demanda certa e permanente é incompatível com a lógica do registro (arts. 82–86) — eixo de impugnação consolidado
- Quantitativos máximos e mínimos, órgãos participantes, carona: limites do regulamento aplicável
- Vigência da ata × vigência contratual

**Participação e habilitação:**
- Tratamento ME/EPP (LC 123/2006): aplicação ou afastamento justificado
- Consórcios: admissão e condições; vedação sem justificativa é restritiva
- Qualificação técnica restrita às parcelas de maior relevância e valor significativo (art. 67, §1º)
- Prazo mínimo em atestados: só para serviços contínuos, teto de 3 anos, períodos sucessivos ou não (art. 67, §5º)
- Quantitativos de atestados: proporcionalidade e justificativa no processo
- Índices econômico-financeiros justificados (art. 69)
- Visita técnica com alternativa de declaração (art. 63; verificar enunciado da Súmula 272/TCU no portal antes de citar)

**Garantias e sanções:**
- Modalidades de garantia admitidas (arts. 96–102); percentuais e proporcionalidade
- Sanções: tipicidade, proporcionalidade, bis in idem entre multas

### E2: Termo de Referência

- Definição do objeto e quantitativos: memória de cálculo presente e rastreável (frota, equipes, roteiros, gravimetria, geração per capita)
- ETP publicado ou referenciado (art. 18); ausência é achado de motivação
- Especificações restritivas sem justificativa (marca, modelo, idade de frota, tecnologia específica)
- Produtividades e dimensionamentos: coerência interna e com o orçamento — `[VALIDAÇÃO TÉCNICA]` quando depender de engenharia
- Compatibilidade com PNRS e PMGIRS municipal
- Obrigações trabalhistas e convenções coletivas da categoria consideradas no dimensionamento

### E3: Minuta do contrato

- Reajuste: índice, periodicidade, data-base — coerência com a data-base do orçamento
- Repactuação/reequilíbrio: procedimento e prazos definidos
- Matriz de riscos, quando adotada: alocação coerente com o regime de execução
- Prazo contratual e prorrogações: limites legais para serviços contínuos
- Pagamento: prazos, medição, glosas — critérios objetivos
- Penalidades contratuais: espelho das editalícias, sem inovação

### E4: Anexos técnicos e planilhas orçamentárias

- Orçamento estimado: data-base e atualidade (parâmetro TCE-SP: 6 meses); metodologia da pesquisa de preços
- Composição de custos unitários: CCT correta, encargos, BDI — verificar aritmética `[VALIDAÇÃO TÉCNICA]`
- Coerência quantitativos do TR × planilha orçamentária × modelo de proposta
- Exequibilidade: parâmetros de aferição definidos no edital

---

## Padrões recorrentes de irregularidade em contratações 14.133 de RSU

- **SRP para serviço contínuo essencial** — incompatibilidade estrutural com demanda certa e permanente (coleta, varrição). Verificar em toda ocorrência de ata de registro.
- **Qualificação técnica em todos os itens do escopo** — contraria a restrição às parcelas de maior relevância (art. 67, §1º).
- **Orçamento defasado** — data-base além da atualidade razoável; não sanável por índice.
- **Contradição TR × planilha × minuta** — quantitativos, produtividades e obrigações divergentes entre anexos (art. 5º — vinculação ao instrumento convocatório).
- **Prazos exíguos** — divulgação abaixo do art. 55 ou reinício não observado após alteração substancial.

---

## Criando um projeto 14.133

```bash
# Exemplo: Pregão Eletrônico 023/2026 de Macaíba
ferramentas/novo_projeto.sh licitacao macaiba-pe023-2026
```

O script copia `licitacoes-14133/_template/`. Convenção de nome e índice dos projetos em `licitacoes-14133/README.md`. A estrutura do projeto é a mesma documentada em `concessoes/README.md` (docs/, docs/extraido/, docs/v2/, output/ versionado).
