# Anexo — Jurisprudência de Tribunais de Contas (API Lei na Mão) [USO INTERNO]

Rodada de 16/08/2026 — PE 30/2026 (REABERTURA), Porto Ferreira/SP, Processo Administrativo n.º 3.721/2026. Fase 2 do pipeline (complemento aos blocos AN_bloco1–6). **Todas as citações são [VIT]** — verificar inteiro teor no portal do tribunal (Pesquisa Integrada TCU / e-TCE-SP) antes do protocolo.

**Notas metodológicas desta rodada:**
1. Fonte única: API Lei na Mão (`ferramentas/buscar_tce.py`), busca por relevância, tribunais TCU e TCE-SP consultados separadamente para cada tema. Nenhuma decisão citada de memória; somente o que o client retornou.
2. Entradas identificadas como `JURISPRUDENCIA-SELECIONADA-xxxxx` na base **não trazem o número real do acórdão** — correspondem a enunciados do repositório "Jurisprudência Selecionada" do TCU. São citadas como "Entendimento TCU" com a marca **[VIT — recuperar número do acórdão no inteiro teor]** e a data de sessão informada pela base. Não usar em peça antes de recuperar o acórdão de origem.
3. A base TCE-SP disponível na API é rasa: resumos genéricos, sem relator/órgão julgador, concentrada em julgamentos de contratos (2002–2018) e não no exame prévio de editais. Em quase todos os temas o TCE-SP não retornou precedente com tese identificável — as lacunas estão registradas tema a tema. As Súmulas 23, 24, 30 e 272 (TCU) já utilizadas nos blocos não dependem desta rodada. **Recomendação transversal: antes do protocolo, repetir as buscas-chave diretamente no sistema de pesquisa de jurisprudência do TCE-SP (fora desta API), notadamente para exame prévio de edital.**
4. Vários entendimentos do TCU abaixo foram firmados sob a Lei n.º 8.666/1993 (art. 30, § 1.º, I; art. 31). A correspondência com os arts. 67 e 69 da Lei n.º 14.133/2021 deve ser explicitada na peça; os dispositivos novos reproduzem, no essencial, as regras interpretadas.
5. Precedentes contrários e ressalvas estão registrados em todos os temas em que localizados. Sem juízo de força de tese.

---

## T1 — Soma de itens mutuamente excludentes no valor estimado; julgamento global; desbalanceamento de unitários (jogo de planilha)

**Queries executadas:** TCU: "jogo de planilha"; "sobrepreço orçamento estimado licitação"; "quantitativo sem justificativa licitação"; "desbalanceamento preços unitários" (0 resultados); "itens excludentes valor estimado" (0). TCE-SP: "jogo de planilha" (0); "quantitativos superestimados orçamento" (0); "critério julgamento menor preço global" (0); "sobrepreço estimativa" (0); "orçamento estimado irregular" (0); "preços unitários incompatíveis" (0); "orçamento estimativo" (0); "preço global" (só resultados genéricos, sem tese identificável).

**Decisões pertinentes (pró-tese):**
- Entendimento TCU-Plenário, sessão de 25/05/2016 (base Lei na Mão, entrada Jurisprudência Selecionada 8033) [VIT — recuperar número do acórdão no inteiro teor] — cabível **multa aos responsáveis pela elaboração de orçamento estimativo com sobrepreço, ainda que não haja dano ao erário**: o vício da estimativa é autônomo em relação ao resultado do certame.
- Acórdão 108/2018-TCU-Plenário, Rel. Aroldo Cedraz, sessão de 24/01/2018 [VIT] — medida cautelar suspensiva de certame por indícios de irregularidades, entre elas **sobrepreço no orçamento estimativo** (fumus + periculum reconhecidos em sede de exame de edital).
- Entendimento TCU-Plenário, sessão de 09/07/2014 (Jurisprudência Selecionada 20557) [VIT — recuperar número do acórdão no inteiro teor] — planilhas de custo são **elementos essenciais das propostas**, qualquer que seja o regime de execução; não são meramente informativas e servem para respaldar variações de custos e **identificar práticas como o "jogo de planilha"**.
- Entendimentos TCU-Plenário, sessões de 08/02/2017 e de 06/07/2016 (Jurisprudência Selecionada 34411 e 12550) [VIT — recuperar números dos acórdãos no inteiro teor] — a caracterização de **jogo de planilha não depende de intenção** de obter vantagem indevida dos agentes ou prepostos da contratada: o controle é objetivo.
- Entendimento TCU-Plenário, sessão de 17/06/2015 (Jurisprudência Selecionada 17221) [VIT — recuperar número do acórdão no inteiro teor] — a diferença percentual entre o valor global do contrato e o referencial **não pode ser reduzida em favor do contratado por aditamentos** que alterem a planilha orçamentária (trava anti-jogo de planilha na execução).
- Acórdão 510/2024-TCU-Plenário, Rel. Walton Alencar Rodrigues, sessão de 27/03/2024 [VIT] — contas irregulares, débito e multa por **superfaturamento decorrente de manipulação de planilhas** e aditivo irregular (dragagem do Porto de Santos): exemplo recente da resposta repressiva do TCU à distorção de planilhas.
- Entendimento TCU-Plenário, sessão de 24/06/2020 (Jurisprudência Selecionada 93766) [VIT — recuperar número do acórdão no inteiro teor] — a modelagem de **adjudicação por preço global (grupo/lote) é exceção que deve ser justificada**, admitida quando a Administração pretende contratar todos os itens do grupo nas proporções definidas; admite-se aquisição isolada de item condicionada ao menor lance válido por item. Suporta o ataque ao julgamento global de lote que soma itens que jamais serão executados cumulativamente.

**Precedentes contrários/ressalvas:**
- Entendimento TCU-Plenário, sessão de 09/06/2021 (Jurisprudência Selecionada 114194) [VIT — recuperar número do acórdão no inteiro teor] — **não se imputa débito com base em sobrepreço de itens isolados** da planilha: a avaliação deve considerar a totalidade do contrato, com compensações entre itens com sobrepreço e subpreço. Ressalva relevante à leitura "item a item" do art. 6.º, LVI, da Lei n.º 14.133/2021 cogitada na análise interna (R3): sob a lei anterior, a régua de débito era global. Verificar no inteiro teor o regime aplicado e a transponibilidade para a 14.133.
- Acórdão 1865/2026-TCU-Plenário, Rel. Odair Cunha, sessão de 15/07/2026 [VIT] — alegação de "jogo de planilha" **considerada infundada** no caso concreto (licitação Petrobras); representação improcedente. Ilustra o ônus probatório de quem invoca o conceito.

*Nota de uso:* a tese específica de T1 (itens excludentes somados na mesma estimativa) não encontrou precedente idêntico; a sustentação combina os fundamentos legais do bloco 1 com os entendimentos acima (estimativa com sobrepreço é vício autônomo; julgamento global exige justificativa; planilhas devem permitir controle de distorções). TCE-SP: nada pertinente localizado nesta base.

---

## T2 — Alocação de riscos e reequilíbrio por evento previsível; matriz de riscos em serviço continuado

**Queries executadas:** TCU: "matriz de riscos alocação"; "reequilíbrio fato previsível"; "alocação de riscos edital serviços"; "reequilíbrio econômico-financeiro evento previsível" (0). TCE-SP: "matriz de riscos" (0); "risco contratada edital" (0); "reequilíbrio econômico-financeiro".

**Decisões pertinentes (pró-tese):**
- Entendimento TCU-Plenário, sessão de 28/05/2025 (Jurisprudência Selecionada 184618) [VIT — recuperar número do acórdão no inteiro teor] — recomendável que a Administração adote **diretrizes na elaboração de matrizes de risco**: detalhamento dos riscos, compatibilização com o regime contratual e análise prévia da matriz, para garantir **coerência entre planejamento, orçamento e obrigações contratuais**. Contexto de obras; a ratio (matriz coerente com o desenho remuneratório) é o que falta ao edital de Porto Ferreira (evento datado tratado como extraordinário; risco controlado pela contratante alocado à contratada).
- Entendimento TCU-Plenário, sessão de 18/11/2015 (Jurisprudência Selecionada 14919) [VIT — recuperar número do acórdão no inteiro teor] — essencial a inclusão, no instrumento convocatório, de **matriz de risco detalhada especificando a alocação de cada risco a cada signatário** (contratação integrada; aplicável por analogia como parâmetro de completude).
- Acórdão 2429/2024-TCU-Plenário, Rel. Benjamin Zymler, sessão de 13/11/2024 [VIT] — reconhecida a **possibilidade de reequilíbrio econômico-financeiro em caso de erro substancial** (inadequação de premissas do projeto) e onerosidade excessiva, com base no Código Civil. Útil como contraponto à cláusula 9.1.6.5: quando o defeito é da modelagem da Administração, a repartição de riscos não bloqueia a revisão.

**Precedentes contrários/ressalvas:**
- Entendimento TCU-Primeira Câmara, sessão de 18/07/2023 (Jurisprudência Selecionada 154520) [VIT — recuperar número do acórdão no inteiro teor] — variação cambial, por si só, **não justifica reequilíbrio**; exige-se consequência incalculável e onerosidade excessiva que rompa a equação. É a mesma linha "evento previsível = risco do contratado" dos TJPR citados no bloco 1 — confirma que, mantido o edital, o remédio ex post será negado; reforça o fundamento prático da correção ex ante.
- Acórdãos TCE-SP, sessões de 13/04/2018 e 19/04/2018, TC-10128/989/18 e TC-10582/989/18 [VIT — resumos genéricos; recuperar relator, órgão julgador e fundamentos no e-TCE] — termos de reequilíbrio econômico-financeiro julgados **irregulares por ausência de justificativa adequada e de comprovação da necessidade**, com devolução de valores e multa. Uso indireto: o TCE-SP glosa reequilíbrio concedido sem lastro documental — mais uma razão para exigir a disciplina no edital, e não confiar na recomposição futura.

---

## T3 — Passivo ambiental de aterro; encerramento; obrigações pós-contratuais sem remuneração

**Queries executadas:** TCU: "passivo ambiental aterro" (1 resultado impertinente — passivo ambiental de obra rodoviária); "encerramento aterro sanitário" (impertinente); "serviço sem remuneração contrato" (impertinentes); "chorume tratamento" (0); "obrigação contratual sem item orçamentário" (impertinente); "custos não previstos planilha edital" (impertinentes). TCE-SP: "passivo ambiental" (0); "aterro operação encargos" (0); "coleta resíduos sólidos edital irregular" (0); "aterro sanitário" (apenas julgamentos genéricos de contratos de manutenção de aterro, sem tese identificável nos resumos).

**Não localizei precedente específico para esta tese na base Lei na Mão** (queries acima) — nem sobre assunção de passivo ambiental preexistente em operação de aterro público, nem sobre encargo continuado sem item remuneratório, nem sobre encerramento de aterro em contrato administrativo. A tese permanece ancorada na fundamentação legal e judicial do bloco 1 (T3). Para a dimensão "obrigação sem remuneração/planilha", podem ser usados por analogia os precedentes de T7/T8 sobre definição precisa do objeto e deficiência de projeto (Acórdãos 2158/2015, 2504/2010 e 63/2024, todos TCU-Plenário [VIT]).

**Precedentes contrários/ressalvas:** nenhum localizado.

---

## T4 — Quantitativo superestimado sem memória de cálculo; grandes geradores

**Queries executadas:** TCU: "memória de cálculo quantitativos"; "estimativa quantidades estudo técnico preliminar"; "quantitativo sem justificativa licitação"; "grandes geradores resíduos" (0). TCE-SP: "grandes geradores" (0); "quantitativo estimado edital" (0).

**Decisões pertinentes (pró-tese):**
- Entendimento TCU-Plenário, sessão de 14/09/2016 (Jurisprudência Selecionada 21439) [VIT — recuperar número do acórdão no inteiro teor] — nas licitações e prorrogações de serviços contínuos, a Administração deve incluir **nos estudos técnicos preliminares a previsão de quantidades**, definição de postos e estimativa de preços (dever de planejamento; formulado para manutenção predial, ratio geral).
- Acórdão 9718/2022-TCU-Primeira Câmara, Rel. Vital do Rêgo, sessão de 29/11/2022 [VIT] — representação parcialmente procedente por **falhas na pesquisa de preços e na elaboração do estudo técnico preliminar**, com determinações de controle interno.
- Acórdão 63/2024-TCU-Plenário, Rel. Vital do Rêgo, sessão de 24/01/2024 [VIT] — **multa ao gestor** por projeto básico deficiente com **inconsistências nos quantitativos de serviços** (remissão a T7).

**Precedentes contrários/ressalvas:**
- Acórdão 2990/2025-TCU-Plenário, Rel. Bruno Dantas, sessão de 08/12/2025 [VIT] — falhas formais (ausência de justificativa para não parcelamento e **falta de estimativas de custos**) **sem prejuízo demonstrado à competitividade não conduzem à anulação** (7 licitantes, sem desclassificações). Antecipa a defesa "vício formal sem prejuízo" — a réplica do bloco 2 (vício no processo de formação da estimativa + efeitos em cascata sobre teto/garantia/multa) deve enfrentá-la.
- Sobre a premissa específica de **grandes geradores** (decreto municipal vigente ignorado no ETP; medição não segregada): **não localizei precedente específico para esta tese na base Lei na Mão** (queries: "grandes geradores resíduos" TCU; "grandes geradores" TCE-SP).

---

## T5 — Pesquisa de preços: exclusão de cotações sem justificativa; emergenciais como referência; cesta heterogênea

**Queries executadas:** TCU: "pesquisa de preços cotações desconsideradas" (1 impertinente); "cesta de preços aceitáveis"; "contratação emergencial referência de preços"; "pesquisa preços metodologia média". TCE-SP: "pesquisa de preços" (genéricos); "preços contratações similares" (0).

**Decisões pertinentes (pró-tese):**
- Entendimento TCU-Plenário, sessão de 21/10/2015 (Jurisprudência Selecionada 16331) [VIT — recuperar número do acórdão no inteiro teor] — estimativas de preços prévias devem estar fundamentadas em **cesta de preços aceitáveis** (pesquisa direta com fornecedores, licitações anteriores, sistemas de compras), para evitar sobrepreço e assegurar aderência ao mercado. Parâmetro de qualidade da cesta — o oposto da cesta heterogênea sem normalização do ETP de Porto Ferreira.
- Acórdão 1445/2022-TCU-Plenário, Rel. Augusto Sherman, sessão de 22/06/2022 [VIT] — identificadas **falhas na elaboração da estimativa de preços, com indícios de superfaturamento**; representação parcialmente acolhida com medidas saneadoras (e censura à desclassificação sem diligência).
- Acórdão 11660/2019-TCU-Segunda Câmara, Rel. Marcos Bemquerer, sessão de 29/10/2019 [VIT] — impropriedade em pregão municipal: **estimativa de preços elaborada sem considerar contratos anteriores** — cotação disponível ignorada vicia a formação do referencial (paralelo direto à exclusão sem motivação do contrato de Itapira).
- Acórdão 2004/2015-TCU-Plenário, Rel. José Múcio Monteiro, sessão de 12/08/2015 [VIT] — contratação emergencial com proposta **em desacordo com os referenciais (SICRO) gerou superfaturamento**; responsabilizados os que examinaram a proposta. Por analogia: preço de emergencial não dispensa cotejo crítico — usá-lo como fonte de referencial sem ajuste inverte a lógica do controle.

**Precedentes contrários/ressalvas:**
- Entendimento TCU-Plenário, sessão de 26/03/2014 (Jurisprudência Selecionada 21827) [VIT — recuperar número do acórdão no inteiro teor] — **não há metodologia legal obrigatória** para o preço de referência; a média aritmética de pesquisas de mercado foi considerada adequada. Defesa provável da Administração ("liberdade metodológica"); a réplica do bloco 2 permanece: o vício apontado não é a escolha da média, e sim a **motivação seletiva** dos descartes e a ausência de atualização/normalização exigidas pelo art. 23, § 1.º, II, da Lei n.º 14.133/2021.

---

## T6 — Imposição de CCT específica (SIEMACO Araraquara); vinculação a instrumento coletivo determinado

**Queries executadas:** TCU: "convenção coletiva trabalho edital"; "enquadramento sindical licitação". TCE-SP: "convenção coletiva" (0); "piso salarial edital" (0); "salários edital licitação" (0).

**Decisões pertinentes (pró-tese):**
- Entendimentos TCU-Plenário, sessões de 15/05/2019 e de 12/08/2020 (Jurisprudência Selecionada 73010 e 97014) [VIT — recuperar números dos acórdãos no inteiro teor] — na planilha de formação de preços **o licitante pode utilizar norma coletiva diversa da adotada pelo órgão contratante**; o enquadramento sindical define-se pela **atividade econômica preponderante do empregador**, não sendo a categoria dos trabalhadores o critério único do orçamento. É exatamente a regra que a resposta à 6.ª impugnação enunciara e que o item 5.4.29 do TR reaberto contraria.
- Entendimento TCU-Plenário, sessão de 30/09/2020 (Jurisprudência Selecionada 99882) [VIT — recuperar número do acórdão no inteiro teor] — **irregular a exigência de que as propostas indiquem os acordos/convenções coletivas** das categorias que executarão o serviço; a vinculação editalícia a instrumento coletivo determinado é inadequada.
- Entendimento TCU-Primeira Câmara, sessão de 20/07/2021 (Jurisprudência Selecionada 116633) [VIT — recuperar número do acórdão no inteiro teor] — em serviços não cobertos por CCT aplicável, **é indevida a fixação de salários no edital**; o valor do orçamento de referência é mera estimativa, vedada a desclassificação de proposta com salários inferiores.
- Acórdão 1646/2025-TCU-Plenário, Rel. Jorge Oliveira, sessão de 23/07/2025 [VIT] — confirmadas falhas na **fixação de salários-base superiores aos das convenções coletivas** e na **falta de clareza do ato convocatório sobre os salários aceitos** nas propostas — dupla frente que espelha a indeterminação do 5.4.29 (duas tabelas de piso; sem piso de motorista).

**Precedentes contrários/ressalvas:**
- Entendimentos TCU-Plenário, sessão de 28/11/2018, e TCU-Primeira Câmara, sessão de 05/05/2020 (Jurisprudência Selecionada 65954 e 90345) [VIT — recuperar números dos acórdãos no inteiro teor] — admite-se exigir **piso salarial superior ao da CCT desde que o gestor demonstre compatibilidade com os preços de mercado** para serviços similares. Porta de defesa da Administração (proteção da exequibilidade); pressupõe, porém, justificativa demonstrada nos autos — inexistente no certame — e não legitima a imposição de instrumento expirado e de base territorial alheia.

---

## T7 — Projeto básico/anexo técnico deficiente; licenciamento da estação de transbordo

**Queries executadas:** TCU: "projeto básico deficiente licitação"; "definição objeto precisa edital"; "estação de transbordo resíduos" (0). TCE-SP: "projeto básico" (apenas resultados genéricos).

**Decisões pertinentes (pró-tese):**
- Acórdão 2158/2015-TCU-Plenário, Rel. Marcos Bemquerer, sessão de 26/08/2015 [VIT] — **multa aos responsáveis por projeto básico deficiente**; a ausência dos elementos exigidos por lei no projeto básico é **irregularidade grave autônoma**, ainda que o sobrepreço apurado seja de baixa materialidade.
- Acórdão 63/2024-TCU-Plenário, Rel. Vital do Rêgo, sessão de 24/01/2024 [VIT] — projeto básico deficiente, com **inconsistências nos quantitativos**; rejeitadas as justificativas e mantida a multa ao gestor.
- Acórdão 872/2016-TCU-Plenário, Rel. Marcos Bemquerer, sessão de 13/04/2016 [VIT] — **inadequação do projeto básico e restrição à competitividade** do certame de saneamento → multa aos responsáveis.
- Acórdão 2504/2010-TCU-Plenário, Rel. Marcos Bemquerer, sessão de 22/09/2010 [VIT] — o projeto básico deve ser elaborado **com precisão, assegurar a viabilidade técnica e o adequado tratamento do impacto ambiental** do empreendimento; censurados critérios inadequados de habilitação e julgamento derivados da deficiência do projeto.
- Acórdão 3062/2011-TCU-Plenário, Rel. Valmir Campelo, sessão de 23/11/2011 [VIT] — deficiências de projeto básico, investimento plurianual fora do PPA, licitação **sem previsão orçamentária adequada e sem todas as licenças e autorizações ambientais necessárias** → certame revogado. Precedente-ponte para o elo licenciamento (LI emitida após o texto editalício afirmar obras iniciadas) e para T17(c).

**Precedentes contrários/ressalvas:** nenhum localizado nesta rodada. TCE-SP: sem precedente com tese identificável.

---

## T8 — Especificações contraditórias/impossíveis; dimensionamento inconsistente

**Queries executadas:** TCU: "especificações contraditórias edital" (0); "edital contradição formulação propostas" (impertinente); "cláusulas conflitantes instrumento convocatório" (impertinentes); "definição objeto precisa edital". TCE-SP: "contradição edital anexos" (0); "divergência edital termo referência" (0); "exame prévio de edital" (amostra genérica).

**Decisões pertinentes (pró-tese):**
- Acórdão 2600/2015-TCU-Plenário, Rel. Vital do Rêgo, sessão de 21/10/2015 [VIT] — censura a edital que utiliza **termos vagos nos critérios de aceitação** dos produtos: parâmetros de aferição devem ser objetivos (aplicável, por identidade de razão, a obrigações cujo conteúdo o edital não define — "triagem primária", KPI sem base).
- Acórdão 2504/2010-TCU-Plenário, Rel. Marcos Bemquerer, sessão de 22/09/2010 [VIT] — remissão (T7): precisão como condição de validade do instrumento.
- Acórdão TCE-SP, sessão de 08/08/2014, TC-3706/989/14 [VIT — resumo genérico; recuperar relator, órgão julgador e fundamentos no e-TCE] — edital de concorrência considerado **irregular por inconsistências nos requisitos de habilitação e na definição do objeto**, com **suspensão do certame** até correção. Único retorno TCE-SP com tese aproveitável; confirmar no inteiro teor se se trata de exame prévio de edital e quais os vícios.

**Precedentes contrários/ressalvas:** nenhum localizado. Sobre a figura específica da **antinomia interna entre anexos** (KPI que pune o cumprimento do plano de frequências; mapas divergentes), **não localizei precedente específico na base Lei na Mão** — sustentar pela via principiológica do bloco 3 c/c os precedentes de precisão acima.

---

## T9 — Sonegação de dados/estudos aos licitantes; assimetria informacional

**Queries executadas:** TCU: "divulgação anexos edital licitantes" (impertinentes); "informações indispensáveis elaboração propostas"; "assimetria informação licitantes" (impertinentes); "publicidade elementos edital sítio" (impertinentes); "informações necessárias proposta edital omissão". TCE-SP: "disponibilização documentos edital" (0); "vistoria informações edital" (0).

**Decisões pertinentes (pró-tese):**
- Acórdão 14077/2023-TCU-Primeira Câmara, Rel. Weder de Oliveira, sessão de 05/12/2023 [VIT — **resumo da base não informa o desfecho; recuperar inteiro teor antes de qualquer uso**] — representação admitida contra pregão de serviços de engenharia alegando **falta de documentos essenciais do edital**, com pedido de suspensão e de **disponibilização das plantas do projeto básico**. Registro de admissibilidade da tese em foro de contas; o mérito deve ser conferido.
- Entendimento TCU-Plenário, sessão de 26/03/2014 (Jurisprudência Selecionada 20537) [VIT — recuperar número do acórdão no inteiro teor] — remissão (T15): a igualdade de acesso às informações que influenciam a elaboração das propostas é o fundamento da obrigatoriedade de republicação — base de contas para a isonomia informacional invocada no bloco 3.

**Precedentes contrários/ressalvas:** nenhum localizado. Sobre o núcleo específico (retenção de dados operacionais do ativo público licitado — topografia, pesagens, monitoramento — após promessa de divulgação), **não localizei precedente específico na base Lei na Mão** (queries acima). A tese segue apoiada no art. 25, § 3.º, e art. 18 da Lei n.º 14.133/2021 e nos precedentes judiciais do bloco 3 (TJSP 1002566-86.2023 [VIT]).

---

## T10 — Garantia contratual: modalidade à escolha do contratado; prazo do art. 96, § 3.º; cláusulas alternativas não resolvidas

**Queries executadas:** TCU: "garantia modalidade escolha contratado"; "seguro-garantia exigência edital"; "caução fiança bancária seguro garantia"; "garantia execução contrato prazo"; "opção contratado modalidade garantia". TCE-SP: "garantia contratual" (0); "seguro garantia contrato" (0); "caução" (erro da API).

**Não localizei precedente específico para esta tese na base Lei na Mão** (queries acima) — nem sobre a imposição/supressão editalícia de modalidade de garantia em detrimento da opção do contratado (art. 96, § 1.º), nem sobre o prazo mínimo do art. 96, § 3.º, nem sobre minuta publicada com redações alternativas não resolvidas. A tese permanece ancorada na literalidade do art. 96 da Lei n.º 14.133/2021 e na doutrina citada no bloco 4.

**Registro conexo (legalidade estrita em matéria de garantias):** Acórdão 1836/2011-TCU-Primeira Câmara, Rel. Ubiratan Aguiar, sessão de 29/03/2011 [VIT] — determinação a município para **abster-se de incluir exigências sem previsão legal** (alvará, prazo para depósito de **garantia de participação**, certidões) em editais futuros — ver uso principal em T11.

**Precedentes contrários/ressalvas:** nenhum localizado.

---

## T11 — Sanções sem dosimetria; multa sem processo; bis in idem; glosa vs. sanção

**Queries executadas:** TCU: "multa sem processo defesa prévia" (impertinentes — multas do próprio TCU); "dosimetria multa contratual"; "penalidades edital base cálculo" (impertinentes); "indicadores desempenho glosa pagamento" (impertinente); "acordo de níveis de serviço" (impertinentes); "instrumento medição resultado". TCE-SP: "aplicação multa contraditório" (0); "penalidade multa contrato irregular" (0).

**Decisões pertinentes (pró-tese):**
- Acórdão 1836/2011-TCU-Primeira Câmara, Rel. Ubiratan Aguiar, sessão de 29/03/2011 [VIT] — determinação para que o município **se abstenha de incluir nos editais exigências sem previsão legal, entre elas garantia de participação** — suporta diretamente o ataque ao item 22.9 do edital (perda de "garantia de proposta" que o certame não exigiu; art. 58 da Lei n.º 14.133/2021 exige previsão editalícia expressa).
- Acórdão 881/2024-TCU-Plenário, Rel. Aroldo Cedraz, sessão de 08/05/2024 [VIT] — contratação que **não afere o resultado a ser atingido pela contratada** viola a Constituição e a legislação de regência — reforço à exigência de que o anexo KPI contenha fórmula objetiva de nível de serviço e fator de ajuste (sem isso não é instrumento de medição de resultado, é sanção inominada).

**Precedentes contrários/ressalvas:**
- Acórdão 311/2026-TCU-Primeira Câmara, Rel. Jhonatan de Jesus, sessão de 27/01/2026 [VIT] — o TCU **não atua como instância revisora de penalidades contratuais** aplicadas por seus jurisdicionados; controvérsias sobre multas devem ser levadas ao Judiciário quando sem reflexo direto no erário federal. Ressalva de roteamento: o questionamento em contas deve mirar o **vício abstrato do regime sancionatório do edital** (exame de edital/representação preventiva), não a revisão de multa aplicada.
- Sobre os núcleos específicos — **multa sem valores/bases como vício de cláusula necessária (art. 92, XIV), sanções divergentes entre edital e TR, e bis in idem glosa + multa** — **não localizei precedente específico na base Lei na Mão** (queries acima). Sustentação segue nos dispositivos e na jurisprudência judicial do bloco 4.

---

## T12 — Medição sob controle da contratada; retenção integral vs. parcela incontroversa; conta vinculada

**Queries executadas:** TCU: "memória de cálculo quantitativos" (compartilhada com T4 — retornou a linha de medição/fiscalização); "retenção pagamento parcela incontroversa" (0); "conta vinculada encargos trabalhistas" (impertinentes); "retenção de pagamentos serviços prestados". TCE-SP: "conta vinculada contrato" (0).

**Decisões pertinentes (pró-tese):**
- Entendimento TCU-Segunda Câmara, sessão de 06/06/2023 (Jurisprudência Selecionada 152280) [VIT — recuperar número do acórdão no inteiro teor] — atestar execução **com base apenas em medições realizadas pela própria contratada, sem verificação rigorosa e documentada, configura erro grosseiro** passível de responsabilização do fiscal. Precedente central para a arquitetura do 9.4.6 (balança operada pelo credor da medição, sem contrapesagem): a independência do procedimento de medição é dever da Administração — a correção interessa a ambas as partes.
- Entendimento TCU-Plenário, sessão de 05/08/2009 (Jurisprudência Selecionada 21110) [VIT — recuperar número do acórdão no inteiro teor] — multa a fiscal por grave deficiência de fiscalização, com **ingerência da contratada nas medições** e inconsistências entre o medido e o executado.
- Entendimento TCU-Plenário, sessão de 10/09/2008 (Jurisprudência Selecionada 31114) [VIT — recuperar número do acórdão no inteiro teor] — vedado pagar com base em **boletins de medição imprecisos**; exige-se medição-verificação dos serviços e **memória de cálculo** correspondente.
- Entendimento TCU-Plenário, sessão de 20/02/2013 (Jurisprudência Selecionada 21174) [VIT — recuperar número do acórdão no inteiro teor] — a comprovação de recolhimento de contribuições previdenciárias **não deve ser exigida como condição para o pagamento** das notas fiscais — linha de contas convergente com o STJ citado no bloco 4 contra a retenção integral da cláusula 4.4.5.

**Precedentes contrários/ressalvas:** nenhum localizado. Sobre **conta vinculada em ente municipal sem regulamento** e sobre **critério de medição indefinido como vício de edital**, **não localizei precedente específico na base Lei na Mão** (queries acima).

---

## T13 — Habilitação técnica: CAT com quantitativo mínimo; quadro permanente; 36 meses; visita técnica

**Queries executadas:** TCU: "capacidade técnico-profissional quantitativo mínimo"; "quadro permanente vínculo profissional"; "quantitativo sem justificativa licitação"; "experiência mínima anos atestado" (nada específico sobre prazo trienal); "visita técnica declaração substitutiva" (nada específico); "garantia execução contrato prazo" (retorno colateral pertinente). TCE-SP: "atestado capacidade técnica quantitativo" (0); "qualificação técnica restritiva" (0); "atestados qualificação técnica edital" (0); "visita técnica obrigatória" (0); "exame prévio de edital" (genéricos).

**Decisões pertinentes (pró-tese) — T13.a (quantitativo mínimo em CAT/capacitação técnico-profissional):**
- Entendimento TCU-Plenário, sessão de 01/02/2012 (Jurisprudência Selecionada 22141) [VIT — recuperar número do acórdão no inteiro teor] — a exigência de **quantitativo mínimo para comprovação da capacidade técnico-profissional contraria a lei** (art. 30, § 1.º, I, da Lei n.º 8.666/1993; correspondência: art. 67, I e § 2.º, da Lei n.º 14.133/2021).
- Entendimento TCU-Plenário, sessão de 16/10/2019 (Jurisprudência Selecionada 80316) [VIT — recuperar número do acórdão no inteiro teor] — reitera a vedação de quantitativo mínimo na capacitação técnico-profissional.
- Entendimento TCU-Plenário, sessão de 16/03/2022 (Jurisprudência Selecionada 128556) [VIT — recuperar número do acórdão no inteiro teor] — quantitativos mínimos para capacitação técnico-profissional **exigem justificativa vinculada à complexidade técnica do objeto**; sem ela, afronta à lei.
- Acórdão 165/2012-TCU-Plenário, Rel. Aroldo Cedraz, sessão de 01/02/2012 [VIT] — caso concreto: edital com quantitativo mínimo para capacidade técnico-profissional; representação parcialmente procedente com ciência ao órgão.
- Convergência com a Súmula 23 do TCE-SP (invocada pelo próprio edital), que veda quantitativos mínimos na capacitação técnico-profissional — a contradição interna apontada em T13.a fica corroborada pela linha do TCU.

**Pró-tese — atestado técnico-operacional e teto de 50% (dialoga com a Súmula 24 do TCE-SP):**
- Entendimento TCU-Primeira Câmara, sessão de 26/03/2019 (Jurisprudência Selecionada 70421) [VIT — recuperar número do acórdão no inteiro teor] — **irregular atestado com quantitativo mínimo superior a 50%** do objeto, salvo justificativa técnica adequada.
- Entendimento TCU-Plenário, sessão de 15/12/2004 (Jurisprudência Selecionada 34242) [VIT — recuperar número do acórdão no inteiro teor] — vedados percentuais acima de 50%, admitidos apenas em casos excepcionais **devidamente justificados no processo ou no edital**. Nota: os 520 t/mês do edital equivalem a exatos 50% — o percentual em si está na faixa admitida (achado CONFORME do bloco 5); o ataque útil é a base de cálculo (tonelagem sem memória — T4/T5) e a aplicação da mesma tonelagem à parcela transitória de aterro.

**Pró-tese — T13.b (quadro permanente/vínculo do RT):**
- Entendimento TCU-Plenário, sessão de 09/12/2009 (Jurisprudência Selecionada 25483) [VIT — recuperar número do acórdão no inteiro teor] — **desnecessário que o profissional integre o quadro permanente**; basta contrato de prestação de serviços.
- Entendimento TCU-Plenário, sessão de 26/11/2014 (Jurisprudência Selecionada 21881) [VIT — recuperar número do acórdão no inteiro teor] — comprovação restrita à indicação de profissional com o acervo exigido, **vinculável por contrato civil de prestação de serviços**, sem quadro permanente.
- Entendimento TCU-Primeira Câmara, sessão de 26/05/2015 (Jurisprudência Selecionada 21832) [VIT — recuperar número do acórdão no inteiro teor] — interpretação ampliada de "quadro permanente": contrato de prestação de serviços basta.
- Entendimento TCU-Plenário, sessão de 27/01/2010 (Jurisprudência Selecionada 25394) [VIT — recuperar número do acórdão no inteiro teor] — admitido **contrato civil com prazo determinado**, garantida a permanência do profissional durante a execução, e admitida a **substituição por profissional de experiência equivalente ou superior** (espelha o art. 67, § 6.º, da Lei n.º 14.133/2021).
- Entendimento TCU-Plenário, sessão de 04/03/2015 (Jurisprudência Selecionada 25230) [VIT — recuperar número do acórdão no inteiro teor] — **é restritiva a cláusula que proíbe a comprovação de vínculo por contrato de prestação de serviços** (e a que impõe visita técnica por profissional específico).
- Acórdão 141/2008-TCU-Plenário, Rel. Ubiratan Aguiar, sessão de 13/02/2008 [VIT] — exigências não previstas em lei restringem o caráter competitivo; interpretação do art. 30, § 1.º, I, quanto à qualificação profissional.

**Precedentes contrários/ressalvas:**
- Sobre **T13.c (36 meses no teto do art. 67, § 5.º, sem justificativa)**: **não localizei precedente específico na base Lei na Mão** (queries: "experiência mínima anos atestado" e correlatas). A moldura legal admite o prazo; o ataque segue pela ausência de justificativa da calibragem (art. 37, XXI, CF) e pela aplicação à parcela transitória — linha do bloco 5.
- Sobre **visita técnica**: nada além do já autorizado (Súmula 272 do TCU, uso direto). Nenhum precedente adicional localizado nesta rodada.
- TCE-SP: sem retorno com tese identificável (Súmulas 23/24/30 permanecem as âncoras estaduais).

---

## T14 — Cumulação capital social + patrimônio líquido + índices; justificativa dos índices; recuperação judicial

**Queries executadas:** TCU: "capital mínimo patrimônio líquido cumulação"; "índices econômico-financeiros justificativa edital"; "capital social mínimo qualificação econômico-financeira"; "recuperação judicial licitação participação". TCE-SP: "capital mínimo" (0); "índices contábeis habilitação" (0).

**Decisões pertinentes (pró-tese) — T14.a (cumulação):**
- Acórdão 2743/2016-TCU-Plenário, Rel. Marcos Bemquerer, sessão de 26/10/2016 [VIT] — censurada a **cumulação indevida de patrimônio líquido mínimo e garantia de execução contratual** para fins de qualificação econômico-financeira — linha da alternatividade dos instrumentos de comprovação (correspondência: art. 69, § 4.º, da Lei n.º 14.133/2021, "capital mínimo **ou** patrimônio líquido mínimo").
- Entendimento TCU-Plenário, sessão de 04/04/2018 (Jurisprudência Selecionada 54764) [VIT — recuperar número do acórdão no inteiro teor] — **vedada a exigência cumulativa de capital social mínimo e garantia de proposta** — mesma ratio de não sobreposição de filtros econômicos.
- Entendimento TCU-Plenário, sessão de 07/02/2024 (Jurisprudência Selecionada 163642) [VIT — recuperar número do acórdão no inteiro teor] — **ilegal exigir capital social integralizado mínimo** além do que autoriza o art. 31, §§ 2.º e 3.º, da Lei n.º 8.666/1993 (precedente formado sob a lei anterior; explicitar a transposição para o art. 69 da Lei n.º 14.133/2021).

**Pró-tese — T14.b (justificativa dos índices):**
- Acórdão 932/2013-TCU-Plenário, Rel. Ana Arraes, sessão de 17/04/2013 [VIT] — **multa** por exigência de **índice econômico-financeiro não usual e não justificado no processo licitatório**; justificativas dos responsáveis rejeitadas. Paralelo direto ao PL ≥ 1/12 sem demonstração técnica e à nota circular do item 1.4.3.

**Pró-tese — T14.d (recuperação judicial):**
- Entendimento TCU-Plenário, sessão de 16/08/2023 (Jurisprudência Selecionada 156300) [VIT — recuperar número do acórdão no inteiro teor] — recuperação judicial ou extrajudicial **não impede a participação** em licitação, desde que comprovada a capacidade econômico-financeira para o contrato.
- Entendimento TCU-Plenário, sessão de 13/05/2020 (Jurisprudência Selecionada 90902) [VIT — recuperar número do acórdão no inteiro teor] — participação admitida mediante **certidão da instância judicial competente** sobre a aptidão econômico-financeira.
- Acórdão 1697/2023-TCU-Plenário, Rel. Jorge Oliveira, sessão de 16/08/2023 [VIT] — caso concreto (serviços de limpeza hospitalar): a recuperação judicial **não pode ser impeditiva** se demonstrada capacidade econômico-financeira.

**Precedentes contrários/ressalvas:**
- Entendimento TCU-Plenário, sessão de 15/10/2008 (Jurisprudência Selecionada 31675) [VIT — recuperar número do acórdão no inteiro teor] — **válida** a exigência de capital social mínimo integralizado como critério de qualificação (dentro do limite legal) — o vício de Porto Ferreira não é o capital em si, e sim a tríplice cumulação.
- Acórdão 1467/2026-TCU-Plenário, Rel. Antonio Anastasia, sessão de 10/06/2026 [VIT] — exigências de habilitação econômico-financeira **mantidas sob a Lei n.º 14.133/2021 quando amparadas em justificativa técnica e jurídica demonstrada** (caso: cômputo de contratos de SPEs) — confirma que a justificativa salva a exigência; a contrario, a ausência de justificativa (nosso caso, T14.b) a condena.

---

## T15 — Respostas a esclarecimento/impugnação não incorporadas ao edital; vinculação das respostas

**Queries executadas:** TCU: "resposta esclarecimento vincula edital"; "esclarecimentos licitantes publicidade respostas". TCE-SP: "resposta esclarecimento pregão" (0).

**Decisões pertinentes (pró-tese):**
- Acórdão 279/2018-TCU-Plenário, Rel. Bruno Dantas, sessão de 21/02/2018 [VIT] — **as respostas e esclarecimentos relativos à licitação possuem caráter vinculante** e devem ser harmonizados com as especificações do edital. Âncora de contas para o efeito integrativo que o art. 164, parágrafo único, da Lei n.º 14.133/2021 não explicita (constatação do bloco 5).
- Entendimento TCU-Plenário, sessão de 26/03/2014 (Jurisprudência Selecionada 20537) [VIT — recuperar número do acórdão no inteiro teor] — **obrigatória a republicação do edital quando as respostas a esclarecimentos, ainda que publicadas em portal oficial, influenciam a elaboração das propostas** — é o núcleo exato da tese T15: regra concedida em resposta que afeta proposta entra no texto, com nova divulgação (art. 55, § 1.º, da Lei n.º 14.133/2021).
- Acórdão 8455/2021-TCU-Primeira Câmara, Rel. Weder de Oliveira, sessão de 25/05/2021 [VIT] — impropriedades pela **falta de republicação do edital**, em desrespeito a princípios administrativos (representação parcialmente procedente).
- Acórdão 978/2025-TCU-Plenário, Rel. Walton Alencar Rodrigues, sessão de 07/05/2025 [VIT] — cautelar deferida em concessão tendo entre os fundamentos a **falta de reabertura de prazo após a republicação do edital** (remissão a T18; reforça o pedido de devolução de prazo).

**Precedentes contrários/ressalvas:**
- Acórdão 141/2023-TCU-Primeira Câmara, Rel. Walton Alencar Rodrigues, sessão de 24/01/2023 [VIT — **resumo da base não informa o desfecho; recuperar inteiro teor antes de qualquer uso**] — registro de representação questionando, entre outros pontos, a **falta de publicidade nas respostas a questionamentos** (Codevasf) — usar somente após verificação.
- Ver também, em sentido de ressalva, Acórdão 10682/2023-TCU-Primeira Câmara (T18): ausência de republicação **sem prejuízo demonstrado** ao caráter competitivo não invalida o certame — o nexo "regra concedida → efeito na formulação da proposta" deve ser demonstrado ponto a ponto (o bloco 5 já faz esse encadeamento).

---

## T16 — Sede/filial local; mobilização exígua; exigências acessórias (LGPD, domicílio bancário)

**Queries executadas:** TCU: "exigência sede escritório local"; "instalação escritório local contratada"; "prazo mobilização exíguo" (0); "prazo início serviços restrição competitividade"; "restrição competitividade sede domicílio"; "dados pessoais LGPD contratação" (impertinentes); "domicílio bancário empregados" (impertinente); "gestão interna contratada intervenção" (impertinentes). TCE-SP: "sede no município" (0).

**Decisões pertinentes (pró-tese):**
- Acórdão 1334/2026-TCU-Plenário, Rel. Antonio Anastasia, sessão de 27/05/2026 [VIT] — **irregular a exigência de base operacional a 500 metros** do local de execução **sem comprovação da necessidade**; a justificativa deve demonstrar que critérios funcionais não bastariam. Transponível ao excesso do item 20.2.e (sede local com internalização de "todos os procedimentos" de RH): o núcleo funcional pode se justificar, o excesso não.
- Acórdão 6923/2025-TCU-Segunda Câmara, Rel. Aroldo Cedraz, sessão de 02/12/2025 [VIT] — cláusula de edital que **restringia a participação a empresas de determinadas regiões comprometeu a competitividade**; irregular (pregão declarado deserto). Princípio do art. 9.º, I, "b", em foro de contas.

**Precedentes contrários/ressalvas:**
- Acórdão 1677/2020-TCU-Plenário, Rel. Augusto Sherman, sessão de 01/07/2020 [VIT] — exigência de **instalação de escritório fixo considerada razoável** para as necessidades do órgão; alegações improcedentes. Defesa provável do núcleo da exigência — coerente com o roteamento do bloco 5 (atacar amplitude e prazo, não a existência da base local).
- Sobre **mobilização exígua/contradição 30 dias × Dia 07**, **Cartão Cidadão com senha de extrato previdenciário (LGPD)** e **domicílio bancário municipal**: **não localizei precedente específico na base Lei na Mão** (queries acima). As teses seguem ancoradas na LGPD, no art. 48, VI, da Lei n.º 14.133/2021 e na ADI 6649 [VIT] (bloco 5).

---

## T17 — Vigência/prorrogação (teto decenal); regime de execução; valor global não declarado

**Queries executadas:** TCU: "vigência decenal prorrogação" (0); "prorrogação serviços contínuos 14.133" (impertinentes); "limite dez anos contrato prorrogação" (impertinente); "valor global estimado vigência contratual" (impertinentes); "previsão orçamentária plurianual licitação". TCE-SP: "vigência 60 meses".

**Decisões pertinentes (pró-tese) — dimensão (c), valor global/orçamento plurianual:**
- Acórdão 3062/2011-TCU-Plenário, Rel. Valmir Campelo, sessão de 23/11/2011 [VIT] — investimento com duração superior a um ano **sem constar do plano plurianual** e licitação **sem previsão orçamentária adequada** (além de projeto básico deficiente) → certame revogado. Suporte de contas para a exigência de declaração do valor global e da previsão plurianual (arts. 16 e 17 da LC n.º 101/2000; art. 106, II, da Lei n.º 14.133/2021).
- Acórdão TCE-SP, sessão de 07/10/2013, TC-36157/026/13 [VIT — resumo genérico; recuperar relator, órgão julgador e fundamentos no e-TCE] — contrato com **vigência de 60 meses julgado irregular por falta de justificativa adequada da duração**, comprometendo economicidade — no regime da 14.133 a vigência quinquenal é autorizada (art. 106), mas o precedente reforça o dever de justificar e dimensionar o vínculo plurianual (valor global, dotações).

**Precedentes contrários/ressalvas:** nenhum localizado. Sobre os núcleos (a) **cômputo do teto decenal do art. 107** (prazo inicial + prorrogações) e (b) **"regime de execução continuado" como cláusula vazia**, **não localizei precedente específico na base Lei na Mão** (queries acima) — teses seguem pela literalidade dos arts. 106, 107 e 92, IV, da Lei n.º 14.133/2021 (bloco 6).

---

## T18 — Taxa da plataforma (BLL) repassada ao licitante; restrição do canal de impugnação; erros de edição/republicação

**Queries executadas:** TCU: "taxa utilização sistema eletrônico licitante" (impertinentes — taxa de administração de contratos de benefícios); "taxa credenciamento pregão eletrônico" (impertinentes); "cobrança pelo provedor do sistema" (impertinente); "impugnação restrição canal apresentação" (0); "erro material edital republicação". TCE-SP: "bolsa de licitações taxa" (0).

**Decisões pertinentes (pró-tese):**
- Acórdão 978/2025-TCU-Plenário, Rel. Walton Alencar Rodrigues, sessão de 07/05/2025 [VIT] — cautelar suspendendo concorrência por irregularidades que incluem a **falta de reabertura do prazo após a republicação do edital** — suporte ao pedido de errata consolidada com devolução de prazo (art. 55, § 1.º, da Lei n.º 14.133/2021) formulado em T18/T15.

**Precedentes contrários/ressalvas:**
- Acórdão 10682/2023-TCU-Primeira Câmara, Rel. Augusto Sherman, sessão de 12/09/2023 [VIT] — reconhecidas a **ausência de republicação do edital e a falta de publicidade** de atos do procedimento, mas, **sem prejuízo identificado ao caráter competitivo**, os embargos foram rejeitados — o dano à formulação das propostas precisa ser demonstrado (o bloco 6 já articula esse nexo para os itens b, c, e, f e j).
- Sobre os núcleos específicos — **repasse da taxa da plataforma privada ao licitante vencedor sem divulgação do percentual** e **impugnação exclusivamente pela plataforma privada (art. 164 restringido)** — **não localizei precedente específico para estas teses na base Lei na Mão** (queries acima). Observação de estratégia já constante do bloco 6: o TCE-SP é o foro natural dessas chaves em exame prévio de edital paulista; repetir a busca no sistema próprio do TCE-SP antes do protocolo.

---

## Balanço da rodada

| Tema | Precedente de contas localizado? | Observação |
|---|---|---|
| T1 | Sim (TCU; nada TCE-SP) | 7 pró + 2 ressalvas; tese específica de itens excludentes sem precedente idêntico |
| T2 | Sim (TCU; TCE-SP uso indireto) | contra-precedente mapeado (previsibilidade) |
| T3 | **Não** | usar analogias de T7/T8 + fundamentação do bloco 1 |
| T4 | Sim (TCU, parcial) | grandes geradores sem precedente específico |
| T5 | Sim (TCU) | contra-precedente de liberdade metodológica mapeado |
| T6 | Sim (TCU, linha direta) | ressalva: piso superior admitido com justificativa |
| T7 | Sim (TCU, denso) | multas por projeto básico deficiente |
| T8 | Parcial | antinomia interna entre anexos sem precedente específico |
| T9 | Parcial | 1 registro sem desfecho no resumo + fundamento via T15 |
| T10 | **Não** | tese segue na literalidade do art. 96 |
| T11 | Parcial | garantia de proposta sem previsão (1836/2011); ressalva de foro (311/2026) |
| T12 | Sim (TCU — medição) | conta vinculada municipal sem precedente |
| T13 | Sim (TCU, o mais denso) | 36 meses sem precedente específico |
| T14 | Sim (TCU) | pró e contra mapeados; recuperação judicial pacificada |
| T15 | Sim (TCU, linha direta) | vinculação + republicação obrigatória |
| T16 | Sim (TCU, parcial) | LGPD/domicílio bancário/mobilização sem precedente |
| T17 | Parcial | teto decenal e regime de execução sem precedente |
| T18 | Parcial | taxa de plataforma e canal de impugnação sem precedente |

**Síntese quantitativa:** 16 de 18 temas com ao menos um precedente pertinente localizado (dos quais 6 apenas parciais — T8, T9, T11, T17, T18 e, quanto ao núcleo "grandes geradores", T4); 2 temas sem nenhum precedente específico (T3 e T10). Total de decisões citadas neste anexo: **77** (73 TCU — sendo 39 entradas "Jurisprudência Selecionada" sem número de acórdão, todas marcadas para recuperação do número no inteiro teor — e 4 TCE-SP), consolidadas com metadados em `TCE_LeiNaMao_resultados.csv` (dedup por número+ano+tribunal; coluna `verificado=false` em todas → [VIT]).

**Pendências desta rodada para antes do protocolo:**
1. Recuperar número de acórdão, relator e trechos do inteiro teor de todas as 39 entradas "Jurisprudência Selecionada" (Pesquisa Integrada do TCU).
2. Verificar inteiro teor dos acórdãos numerados TCU (Pesquisa Integrada) e dos 4 TCE-SP (e-TCE) — resumos da base são sintéticos e, no caso TCE-SP, genéricos.
3. Repetir as chaves de T13, T14, T15, T16 e T18 no sistema de pesquisa próprio do TCE-SP (exame prévio de edital), não coberto adequadamente pela API.
4. Conferir a transponibilidade dos entendimentos firmados sob a Lei n.º 8.666/1993 para os dispositivos correspondentes da Lei n.º 14.133/2021 em cada citação usada em peça.

*Documento produzido pelo agente de busca jurisprudencial da Fase 2. Não constitui peça formal. Nenhuma avaliação de força de tese. Seleção e uso das citações são decisão exclusiva do advogado.*
