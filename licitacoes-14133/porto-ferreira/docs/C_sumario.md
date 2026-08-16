# Sumário da consolidação — Fase 1 — PE 30/2026 (REABERTURA) [USO INTERNO]

- Achados brutos (E1–E4): **379**
- Pontos consolidados: **300** (64 merges absorvendo 146 achados; 3 contradições novas)
- Reconciliação: 379 origens = 297 pontos (82 absorvidos por merge) + 3 pontos novos de contradição
- Flags: 64 com `flag_tecnico` (VALIDAÇÃO TÉCNICA), 28 com `flag_reserva` (RESERVA)

## Por tipo de achado

- IRREGULAR: **120**
- DEPENDE_DE_FATO: **129**
- CONFORME: **51**

## Por tema

| Tema | IRREGULAR | DEPENDE_DE_FATO | CONFORME | Total |
|---|---|---|---|---|
| OBJETO_ESCOPO | 25 | 22 | 7 | 54 |
| HABILITACAO | 9 | 13 | 16 | 38 |
| JULGAMENTO_PROPOSTA | 3 | 7 | 6 | 16 |
| MODELAGEM_ECONOMICA | 22 | 38 | 4 | 64 |
| RISCOS_GARANTIAS | 13 | 10 | 1 | 24 |
| REMUNERACAO_REAJUSTE | 12 | 8 | 3 | 23 |
| REGULACAO_FISCALIZACAO | 16 | 12 | 3 | 31 |
| LICENCIAMENTO_AMBIENTAL | 3 | 10 | 3 | 16 |
| QUESTOES_FORMAIS | 17 | 9 | 8 | 34 |

## Contradições inter-documentos criadas na consolidação

- **C-113** (MODELAGEM_ECONOMICA): ETP trata a cobranca dos grandes geradores como evento futuro e incerto que reduzira a tonelagem em 20%, enquanto o Decreto 3.367/2026 — anexado ao proprio edital — ja instituiu o regime desde 07/01/2026 com prazos de adesao decorridos: a premissa central da estimativa de 12.480 t/ano esta em contradicao temporal com a norma vigente, sem revalidacao do quantitativo na reabertura [origens: E4-003, E4-004, E4-070]
- **C-174** (RISCOS_GARANTIAS): TR e minuta fixam momentos incompativeis para a prestacao da garantia: o TR exige o seguro-garantia em 1 mes contado da homologacao e ANTES da assinatura, enquanto a minuta concede 10 dias contados DA ASSINATURA para comprovar a garantia — regimes inconciliaveis sobre a mesma obrigacao, agravados pelas duas redacoes alternativas do item 8.1 [origens: E2-015, E3-019, E3-022]
- **C-222** (REGULACAO_FISCALIZACAO): Edital e TR preveem, para a mesma infracao (recusa injustificada de assinar o contrato), sancoes com faixas e bases de calculo divergentes (0,5%-30% sobre o valor do contrato licitado vs 0,5%-15% sobre o valor da proposta), alem da perda de garantia de proposta que o certame nao exigiu — indeterminacao do regime sancionatorio aplicavel [origens: E1-045, E2-074, E1-043]

## Pontos com flag de reserva estratégica [RESERVA]

- **C-026** (OBJETO_ESCOPO, DEPENDE_DE_FATO): Objeto com fases alternativas/sucessivas (operação do aterro municipal — item 2 — até seu encerramento definitivo, depois destinação em aterro de outro município — item 3, conforme nota do TR item 9.1); o momento de transição depende da vida útil remanescente do aterro municipal, fato não determinável pelo edital principal e que afeta o dimensionamento das propostas
- **C-027** (OBJETO_ESCOPO, DEPENDE_DE_FATO): Justificativa do parcelamento contraditória e genérica: denomina 'parcelamento' o que descreve como agrupamento de itens em lote único, e se resume a uma frase, sem análise dos fatores de divisibilidade técnica e econômica do objeto (coleta, destinação e contêineres)
- **C-036** (OBJETO_ESCOPO, DEPENDE_DE_FATO): TR não define se o aterro municipal receberá resíduos de outras fontes (varrição e serviços próprios da Prefeitura, particulares autorizados) e se essas toneladas integram a remuneração do item 2 — indefinição do fluxo total operado e faturável
- **C-039** (OBJETO_ESCOPO, DEPENDE_DE_FATO): [USO INTERNO] Dados operacionais do aterro não anexados (levantamento topográfico, capacidade volumétrica remanescente da Vala 05, relatórios de monitoramento, condicionantes da LO) — assimetria informacional que favorece quem opera/conhece a unidade, inclusive para modelar a data real da transição ao item 3
- **C-040** (OBJETO_ESCOPO, DEPENDE_DE_FATO): Prazo de 30 dias da OS para iniciar operação exigindo simultaneamente frota adesivada com GPS, garagem, oficina, almoxarifado com 6 jogos de pneus, 0800, 80 contêineres instalados e sede local: mobilização exígua tende a favorecer empresas já instaladas na região
- **C-052** (OBJETO_ESCOPO, CONFORME): [USO INTERNO] Referencial de frete do Item 3 ancorado nos aterros mais proximos (67 km), sendo um deles ativo do proprio grupo (Sao Carlos Ambiental): assimetria favoravel na precificacao do transporte e da taxa de disposicao final em relacao a concorrentes sem aterro proprio na regiao
- **C-056** (HABILITACAO, IRREGULAR): Vinculação da capacitação técnico-PROFISSIONAL (CAT) a parcelas de relevância expressas com quantitativos mínimos (520 t/mês) — a qualificação do profissional restringe-se à comprovação de responsabilidade técnica por serviço de características semelhantes, sem imposição de quantitativos mínimos, e a própria Súmula 23 do TCE-SP invocada pelo edital trata da CAT sem autorizar quantitativos
- **C-060** (HABILITACAO, IRREGULAR): Promessa de eliminar referências incompatíveis com o regime de serviço comum cumprida apenas quanto ao critério de inexequibilidade (75% suprimido); Anexo II mantém exigências típicas de serviço de engenharia (registro CREA, CAT), em tensão com a qualificação do objeto como serviço comum
- **C-063** (HABILITACAO, IRREGULAR): Regra de aproveitamento da capacidade técnica da subcontratada para comprovar a viabilidade do Item 3 admitida apenas na resposta à 6ª impugnação, sem incorporação ao edital reaberto
- **C-067** (HABILITACAO, DEPENDE_DE_FATO): Exigência de experiência em OPERAÇÃO DE ATERRO como segunda parcela de maior relevância, quando a operação do aterro municipal (item 2) é fase transitória, excluída do 'valor máximo anual efetivamente executável' — a pertinência e o peso da parcela dependem da vida útil remanescente do aterro municipal e do valor relativo do item 2 (R$ 2.106.249,60/ano ≈ 23% do estimado global); exigência cumulada (coleta + aterro) restringe o certame a operadores verticalizados
- **C-068** (HABILITACAO, DEPENDE_DE_FATO): Exigência de tempo mínimo de experiência (36 meses) nas parcelas de relevância — a lei veda 'limitações de tempo' relativas aos atestados, havendo controvérsia sobre se a vedação alcança a exigência de duração mínima de experiência admitida na praxe de serviços contínuos
- **C-071** (HABILITACAO, DEPENDE_DE_FATO): Cumulação de exigências econômico-financeiras: capital social mínimo (1.4.2) + índices LG/SG/LC ≥ 1 + patrimônio líquido mínimo atrelado a 1/12 dos compromissos firmados — a lei admite capital mínimo OU patrimônio líquido mínimo (alternatividade), e a relação de compromissos serve à análise, não à criação de terceiro requisito autônomo
- **C-072** (HABILITACAO, DEPENDE_DE_FATO): Habilitação silente quanto à comprovação de acesso a aterro licenciado de terceiro (item 3) e quanto a licenças ambientais de operação — omissão pró-competitiva na habilitação, mas que transfere para a execução o risco de destinação inadequada; licitantes verticalizadas com aterro próprio licenciado na região detêm assimetria favorável
- **C-085** (HABILITACAO, CONFORME): Quantitativos mínimos de 520 t/mês equivalem a exatos 50% da demanda estimada (12.480 t/ano = 1.040 t/mês) — calibrados no teto máximo admitido em lei e na faixa da Súmula 24; admitido somatório de atestados concomitantes
- **C-101** (JULGAMENTO_PROPOSTA, DEPENDE_DE_FATO): Julgamento pelo menor valor global do lote somando itens 2 e 3, mutuamente excludentes e ambos com a tonelagem anual integral (12.480 t), faz o critério de julgamento não refletir o dispêndio real e permite desbalanceamento dos preços unitários entre os itens conforme a expectativa de vida útil do aterro municipal (jogo de planilha)
- **C-119** (MODELAGEM_ECONOMICA, IRREGULAR): Unidade de medida inconsistente para os contêineres: as tabelas do ETP indicam quantidade de 80 'UNIDADE' com valor unitário tratado como mensalidade por contêiner, enquanto o quadro comparativo adota quantidade 960 (unidade×mês), sem explicitar em nenhum documento que a remuneração é por unidade/mês
- **C-123** (MODELAGEM_ECONOMICA, IRREGULAR): Exclusão não justificada de cotações de coleta disponíveis nos próprios contratos anexados (Itapira R$ 225,02/t, inferior à média adotada de R$ 302,65; Artur Nogueira R$ 342,30/t) na composição do preço do item 1 — a única exclusão justificada na nota do quadro foi o outlier de contêiner de R$ 19.116,00
- **C-127** (MODELAGEM_ECONOMICA, IRREGULAR): Preço de contratação emergencial (dispensa do art. 75, VIII), de município com 280 t/mês (27% da escala de Porto Ferreira, 1.040 t/mês) e prazo de 12 meses, usado sem qualquer ajuste na média do item 3 do valor estimado
- **C-130** (MODELAGEM_ECONOMICA, IRREGULAR): Contradição direta: resposta afirma liberdade de cada licitante adotar sua CCT, mas o edital reaberto impõe atendimento integral à CCT 2025/2026 do SIEMACO Araraquara, com impacto direto na composição de custos e comparabilidade das propostas
- **C-131** (MODELAGEM_ECONOMICA, DEPENDE_DE_FATO): Duplicidade de estimativa: os itens 2 e 3 preveem, cada um, a destinação das mesmas 12.480 t/ano (soluções mutuamente excludentes — aterro municipal OU aterro externo), mas ambos são somados integralmente no valor total estimado, inflando a estimativa em mais de R$ 2 milhões/ano
- **C-137** (MODELAGEM_ECONOMICA, DEPENDE_DE_FATO): Premissa de redução de 20% da tonelagem condicionada a evento futuro e incerto (implementação da cobrança de grandes geradores), sem demonstração técnica do percentual, sem cronograma de implementação e sem tratamento do risco de a redução não se concretizar em contrato de 60 meses
- **C-141** (MODELAGEM_ECONOMICA, DEPENDE_DE_FATO): Premissas potencialmente antagônicas não conciliadas: a conteinerização de 17 pontos de descarte irregular e de pontos estratégicos tende a incorporar à coleta regular volumes hoje descartados irregularmente, na contramão da premissa de redução de 20% da tonelagem
- **C-144** (MODELAGEM_ECONOMICA, DEPENDE_DE_FATO): Item 2 do valor estimado (operação do aterro sanitário municipal + disposição final) lastreado exclusivamente em gate fees de aterros privados de terceiros, estrutura de custos distinta da operação de aterro público (cobertura, chorume, monitoramento, encerramento)
- **C-146** (MODELAGEM_ECONOMICA, DEPENDE_DE_FATO): Preço de coleta de Itapira (R$ 225,02/t, contrato anexado ao proprio ETP, escala 1.500 t/mês) excluído da média do item 1 sem justificativa expressa — sua inclusão reduziria a média de R$ 302,65 para aproximadamente R$ 287/t
- **C-150** (MODELAGEM_ECONOMICA, DEPENDE_DE_FATO): Os três referenciais do item 3 pressupõem transbordo integralmente por conta da contratada (infraestrutura e equipamentos), enquanto em Porto Ferreira a estação de transbordo é construída e licenciada pela Administração — estruturas de custo distintas não ajustadas na composição do valor estimado
- **C-156** (MODELAGEM_ECONOMICA, DEPENDE_DE_FATO): CCT prevê duas tabelas de pisos (empresas que reajustaram 9,5% ou 8,5% em 2015) e o edital exige atendimento 'integral' sem definir a tabela aplicável a licitante sem histórico na base territorial — ambiguidade de precificação entre concorrentes
- **C-237** (REGULACAO_FISCALIZACAO, DEPENDE_DE_FATO): Obrigação de instalar sede/filial/escritório local com estrutura administrativa completa em 30 dias da assinatura/OS; exigência pós-contratação é menos gravosa que requisito de habilitação, mas o prazo e a amplitude ('todos os procedimentos' de RH no local) oneram licitantes de fora e favorecem empresas já instaladas; nota-se ainda incongruência com exigência de alvará 'do município da sede da licitante'
- **C-238** (REGULACAO_FISCALIZACAO, DEPENDE_DE_FATO): Rejeição mantida: exigências acessórias (sede/filial local em 30 dias, Cartão Cidadão com senha de extrato previdenciário dos empregados, domicílio bancário no Município) permanecem, fundamentadas em TAC do MPT não disponibilizado como anexo do edital reaberto; questão de dados pessoais (LGPD) não enfrentada
