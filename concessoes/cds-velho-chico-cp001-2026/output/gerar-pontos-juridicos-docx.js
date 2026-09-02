const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType,
  ShadingType, AlignmentType, BorderStyle, PageOrientation, HeadingLevel, Footer, PageNumber,
} = require("docx");

const FONT = "Times New Roman";
const pts = [
  // ---- OBJETO E ESCOPO ----
  { tema: "Objeto e escopo", prev: "Edital: capa, preâmbulo, item 4.3; Errata de 27/08/2026; Anexo I, itens 1 e 1.1; Contrato: cl. 8 e 8.3.2.5; Anexo XX, item 5",
    com: "O regime jurídico oscila entre os documentos: a capa fala em concessão patrocinada, o preâmbulo em “contrato de concessão” e o Anexo I dizia “concessão comum” até a errata publicada no dia seguinte. O contrato não prevê contraprestação pecuniária regular: a remuneração é tarifária e a única obrigação pública é a TEP de serviços opcionais e um aporte contingente por inadimplência. O próprio Anexo XX afirma que o projeto “não é deficitário sob a ótica tarifária”. A errata alterou o regime e a data-base sem reabertura de prazo.",
    fund: "art. 2.º, §§ 1.º a 3.º, e art. 10 da Lei n.º 11.079/2004; art. 55, § 1.º, da Lei n.º 14.133/2021" },
  { tema: "Objeto e escopo", prev: "Edital: itens 3.1, 3.3 e 3.4; Contrato: cl. 5.1, 8.7 e 8.9 e Anexo IV (Termo de Adesão); Anexo IV do Edital (pesos dos indicadores); Anexo I, item 1.4",
    com: "Só a destinação de RDO é obrigatória. Coleta de RDO (29,6% da TUF) e manejo de RPU, RCD e RSS (100% da TEP) dependem de adesão futura de cada município, sem prazo, permanência mínima, regra de retirada ou reequilíbrio. Os indicadores atribuem 50,75% da nota a serviços por adesão, e a autoclave e a unidade de RCD são investimentos obrigatórios mesmo sem adesão. O caderno registra contratos municipais de coleta vigentes por até 120 meses. O licitante precifica objeto indeterminado.",
    fund: "art. 4.º, VI, e art. 5.º, III, da Lei n.º 11.079/2004; art. 23, I, II e IV, da Lei n.º 8.987/1995" },
  { tema: "Objeto e escopo", prev: "Contrato: cl. 2.1 (Célula), 8.6, 18.2, 18.4 e 18.17; Anexo I, itens 1.3 e 1.4; Anexo III (EVEF), Tabela 9",
    com: "A TUF-D só passa a ser devida quando a destinação ocorrer em aterro implantado pela concessionária, mas nenhum documento diz para onde vai o RDO entre a ordem de serviço e a operação do aterro, nem quem paga esse transporte e destinação. Os cinco lixões seguem ativos após o prazo legal de 02/08/2024. O prazo da célula é de um ano nas cláusulas 2.1 e 18.2 e de cinco na 18.4, e o EVEF lança metade do CAPEX do aterro no ano 2. O caderno descarta os aterros licenciados de Caetité e Bom Jesus da Lapa como “inviáveis” sem demonstração.",
    fund: "art. 47, II, e art. 54 da Lei n.º 12.305/2010; art. 7.º da Lei n.º 11.079/2004; art. 23, I e II, da Lei n.º 8.987/1995", vt: true },
  // ---- HABILITAÇÃO ----
  { tema: "Habilitação", prev: "Edital: itens 4.3, 14.1, 15.5.1.1 e 15.5.1.2; Anexo XXI (justificativa econômico-financeira)",
    com: "O “valor do contrato” que serve de base ao capital social mínimo (R$ 100,4 milhões, mais 30% em consórcio), à garantia da proposta (R$ 10 milhões) e à garantia de execução é a receita tarifária de 30 anos, R$ 1,004 bilhão, para um CAPEX de R$ 123 milhões (R$ 32 milhões nos cinco primeiros anos) e uma SPE de R$ 6,4 milhões. Só se admite capital social, não patrimônio líquido. Os índices ILC, ILG e endividamento são exigidos de cada consorciada, sem o somatório previsto em lei, e o Anexo XXI transcreve o art. 69 sem enfrentar o § 4.º.",
    fund: "art. 58, § 1.º, art. 69, §§ 4.º e 5.º, art. 15, III e § 1.º, e art. 98, parágrafo único, da Lei n.º 14.133/2021; art. 18, V, da Lei n.º 8.987/1995" },
  { tema: "Habilitação", prev: "Edital: itens 15.4.2 (15 parcelas), 15.4.3 e 15.4.3.2; Anexo XXI (parcelas de maior relevância)",
    com: "O Anexo XXI indica quatro parcelas de maior relevância (aterro, coleta de RDO, triagem e compostagem, transbordo) e diz que a experiência será exigida “exclusivamente” nelas, que somam cerca de 4% do valor do contrato. O edital exige quinze, com 50% dos quantitativos. Entre as onze não justificadas estão serviços opcionais que podem nunca ser prestados e “gestão comercial de saneamento” para 49.374 habitantes, admitida em água e esgoto, o que direciona o certame a operadoras de saneamento. Os quantitativos de coleta seletiva (94 t/mês estimado, 47 t/ano mínimo) e de compostagem não têm relação com o caderno.",
    fund: "art. 18, IX, e art. 67, I e §§ 1.º e 2.º, da Lei n.º 14.133/2021; art. 37, XXI, da CF/1988", vt: true },
  { tema: "Habilitação", prev: "Edital: itens 15.4.1.2, 15.4.3 (alíneas a a o), 15.4.4 e 15.4.6",
    com: "Registro no CREA e no CRA de todas as consorciadas, independentemente da parcela executada. Profissional com CAT para cada uma das quinze parcelas, inclusive educação ambiental, apoio a cooperativas e coleta seletiva, atividades sem conteúdo de engenharia. Equipe mínima de cinco engenheiros com atestados já na habilitação. No somatório de atestados, um deles deve trazer 50% do quantitativo, sem justificativa.",
    fund: "art. 67, I e § 5.º, da Lei n.º 14.133/2021" },
  { tema: "Habilitação", prev: "Edital: itens 6.3, alínea g, 6.4, alínea g, e 15.4.8, II; Anexo XXI (limite de consorciados)",
    com: "Máximo de três consorciados com participação mínima de 35% para empresas: três operadoras somam 105%, de modo que só cabe a composição duas empresas e um fundo. A consorciada que apresentar atestados precisa deter 35%, o que impede que a técnica venha de uma minoritária. A vedação a licitantes com “sócio comum, independente da participação societária” alcança situações fora da hipótese legal de vínculo de controle.",
    fund: "art. 14 e art. 15, III e § 4.º, da Lei n.º 14.133/2021; art. 19 da Lei n.º 8.987/1995" },
  { tema: "Habilitação", prev: "Edital: item 15.4.5 e item 18.5",
    com: "O item 15.4.5 exige, como documento de habilitação, “comprovação emitida pela Comissão” de que a licitante visitou os locais; o item 18.5 admite declaração formal substitutiva do responsável técnico. As duas regras convivem no mesmo edital.",
    fund: "art. 63, III, da Lei n.º 14.133/2021; Súmula 272 do TCU" },
  // ---- JULGAMENTO ----
  { tema: "Julgamento da proposta", prev: "Edital: itens 16.4.2 a 16.4.2.3, Tabela A, 16.4.2.2.8.1 a 16.4.2.2.8.10, 16.4.3 e 16.6; Anexo XIII, Apêndice A",
    com: "O julgamento é por menor tarifa, mas a proposta passa por filtro técnico binário (“atendido / não atendido”) em sete itens sem parâmetro objetivo, com desclassificação facultativa (“poderá”) e por itens que o próprio edital declara opcionais (“ações de equidade, se já implantadas”, “programa de integridade, se já implantado”). Exige-se ainda declaração de consultor de valores mobiliários credenciado na CVM validando a modelagem, cujo modelo o exime de qualquer responsabilidade.",
    fund: "art. 5.º e art. 59 da Lei n.º 14.133/2021; art. 12, II, da Lei n.º 11.079/2004; art. 15, I, da Lei n.º 8.987/1995" },
  { tema: "Julgamento da proposta", prev: "Edital: itens 16.4.4 e 17.13; Anexo XIII (carta de proposta)",
    com: "Um único multiplicador K incide linearmente sobre a TUF-D (destinação obrigatória), a TUF-C e as TEPs (serviços opcionais com custo próprio). A carta de proposta lista quatro valores e não distingue TEP-C de TEP-D. Ponto que comporta esclarecimento dirigido sobre a forma de aplicação.",
    fund: "art. 15, I, da Lei n.º 8.987/1995; art. 12, II, da Lei n.º 11.079/2004", vt: true },
  // ---- MODELAGEM ----
  { tema: "Modelagem econômica", prev: "Anexo III (EVEF), § 4 e Tabelas 3 a 5; Anexo XV, Tabela 2; Anexo XVIII, Tabela 2; Anexo I, Tabela 45",
    com: "O EVEF grafa 117.626 t/ano de RDO onde o modelo usa 29.916 t. As colunas por município estão trocadas entre o caderno de demanda e o estudo operacional. A receita é função do volume de água faturada, que cresce 24% em cinco anos sem fonte, com população estável. Não há pesagem nem gravimetria local; um caderno diz que a população é majoritariamente urbana e outro, rural.",
    fund: "art. 10, I, alínea a, e § 4.º, da Lei n.º 11.079/2004; art. 11, II, da Lei n.º 11.445/2007", vt: true },
  { tema: "Modelagem econômica", prev: "Anexo III (EVEF), Tabelas 9, 16 e 28; Anexo XVIII, Quadro 3",
    com: "O OPEX lança “destinação final” a R$ 85/t por 30 anos (R$ 135 milhões) apesar de o aterro ser próprio e já orçado em CAPEX, mão de obra e manutenção. Não há linha de CAPEX para as quatro ETRs, a unidade de compostagem, os galpões, a balança ou o centro de educação ambiental, todos listados como escopo. Encerramento e pós-fechamento do aterro não estão orçados, e há reinvestimento de R$ 10,9 milhões no ano 30 depreciado no próprio ano.",
    fund: "art. 10, § 4.º, da Lei n.º 11.079/2004; art. 36 da Lei n.º 8.987/1995", vt: true },
  { tema: "Modelagem econômica", prev: "Anexo III (EVEF), p. 6, 7 e 10 e Tabelas de custos; Anexo XVI (Value for Money), Tabela 1",
    com: "As tarifas são referenciadas a julho de 2026 e o CAPEX e o OPEX a dezembro de 2025, num modelo “em moeda constante”. O Value for Money de 20,61% é calculado sobre o fluxo da PPP; sobre o comparador público seria 17,1%, e o comparador presume execução direta com pessoal próprio, ao contrário do diagnóstico de terceirização já existente.",
    fund: "art. 10, I, alínea a, e § 1.º, da Lei n.º 11.079/2004" },
  // ---- RISCOS E GARANTIAS ----
  { tema: "Riscos e garantias", prev: "Edital: itens 25.3 e 25.4; Anexo XX, itens 8 e 9 e Anexo A (contrato de depósito), cl. 1.1 e 6.1.1; Contrato: cl. 4.1, alínea g, e 13.1.38",
    com: "O fundo garantidor municipal “deverá ser criado” e o comitê gestor é “criado por esta lei”: texto de minuta de lei transplantado para o edital, sem lei identificada. As contas de pagamento e garantia dependem de repasse mensal voluntário de FPM e ICMS pelos municípios, e o contrato de depósito se extingue após seis meses sem repasse, ou seja, no próprio evento garantido. O “seguro-garantia” do art. 8.º, III, é atribuído à concessionária. O contrato não tem cláusula de inadimplência pecuniária do parceiro público; o único remédio é suspender RSS e RPU após 90 dias.",
    fund: "art. 8.º, I a V, da Lei n.º 11.079/2004; art. 167, IV e IX, da CF/1988; art. 5.º, III, da Lei n.º 11.079/2004" },
  { tema: "Riscos e garantias", prev: "Anexo XX, item 6; Anexo XIX, item 2.4; Contrato: cl. 8.3.2.5, 8.3.2.9, 8.9.1 e 41.1; Edital: item 25.2",
    com: "O limite de 5% da RCL foi verificado só sobre a soma dos cinco municípios e só no ano 1; o contrato fala em “RCL do trimestre”, conceito inexistente. Não há PPA, LDO, contrato de rateio nem declaração do ordenador; o Anexo XIX admite que isso “depende do juízo de conveniência de cada gestor”. Os municípios devem a TEP e o aporte sem serem partes, e a TEP não tem atualização nem juros de mora.",
    fund: "art. 10, I, alínea b, II a V, e art. 28 da Lei n.º 11.079/2004; arts. 16 e 17 da LC n.º 101/2000; art. 8.º da Lei n.º 11.107/2005" },
  { tema: "Riscos e garantias", prev: "Anexo I, itens 1.4 e 3.2; Contrato: cl. 6.1, 14.1.2, 14.1.3, 18.3, 18.8, 18.8.1 e 22; Anexo V (Matriz), itens 19 e 41; Anexo XVII, itens 2.1.2, 2.3.2 e 2.3.3 e Anexo I",
    com: "A área da CVR não está identificada: o caderno manda a concessionária comprá-la, o contrato e a matriz falam em desapropriação pelo concedente, e a vigência começa com a “liberação das áreas”. As ETRs são construídas pela concessionária, pelos municípios ou pelo concedente, conforme o documento. Não há licença prévia nem diretrizes de licenciamento para o aterro; as diretrizes ambientais trazem texto sobre Angra dos Reis e citam o Código Florestal revogado.",
    fund: "art. 5.º, III, e art. 10, VII, da Lei n.º 11.079/2004; art. 18, XII, art. 29, VIII e IX, e art. 31, VI, da Lei n.º 8.987/1995", vt: true },
  { tema: "Riscos e garantias", prev: "Anexo I, itens 3.10.3.1 e 3.10.3.2; Contrato: cl. 18.2.1 e 18.13; Anexo XVII, item 2.2.1 e Anexo I, item 3.5; Anexo XV, p. 20",
    com: "A concessionária elabora, licencia em seu nome e executa o PRAD dos cinco lixões, com desembolso limitado ao CAPEX de R$ 8,9 milhões, sem quantitativos e sem remoção de massa orçada. A cláusula que exclui o passivo não vincula o órgão ambiental nem terceiros. Contrato e caderno divergem sobre o titular do passivo (consórcio ou municípios), e a desocupação dos catadores fica com os municípios sem prazo.",
    fund: "art. 3.º, IV, e art. 14, § 1.º, da Lei n.º 6.938/1981; art. 225, § 3.º, da CF/1988; art. 5.º, III, da Lei n.º 11.079/2004", vt: true },
  { tema: "Riscos e garantias", prev: "Edital: itens 10.3, 18.6 e 28.2.3; Contrato: cl. 23.2; Anexo V (Matriz), item 27 e itens 3, 22 e 38 a 44",
    com: "Tudo o que não estiver na matriz é risco da concessionária, inclusive erro nos levantamentos da própria Administração, que qualifica seus estudos como “preliminares” e “meramente indicativos” e veda qualquer pleito por insuficiência de dados. A matriz publicada não tem os itens 3 e 22 e as colunas de responsabilidade dos itens 38 a 44 estão ilegíveis.",
    fund: "art. 5.º, III, da Lei n.º 11.079/2004; art. 103, caput e § 1.º, da Lei n.º 14.133/2021; art. 18, XV, da Lei n.º 8.987/1995" },
  // ---- REMUNERAÇÃO ----
  { tema: "Remuneração e reajuste", prev: "Edital: item 4.2; Contrato: cl. 6.1, 8.3, 8.3.2 e 41.2; Anexo I, item 10.2.2; Anexo XIX, item 2.2; Anexo XX, item 9",
    com: "A cobrança da TUF na fatura de água depende de anuência da Embasa, obrigação de meio do concedente; sem acordo, a concessionária cobra diretamente, com custo não modelado. A vigência do contrato só começa com esse acordo. Os anexos divergem se a cobrança é taxa ou tarifa; se taxa, a concessionária não pode arrecadá-la. A base é o m³ de água faturada, sem tarifa social, e os fatores de uso e de localização serão homologados só depois.",
    fund: "art. 29 e art. 35 da Lei n.º 11.445/2007; art. 5.º, I, e art. 8.º, IV, da Lei n.º 11.079/2004" },
  { tema: "Remuneração e reajuste", prev: "Anexo I, itens 10.4 e 10.5; Anexo IV, item 4.1 e Tabelas 8 e 10; Contrato: cl. 27.2, 27.3, 28.5 e 28.5.2",
    com: "O índice de reajuste é definido como soma ponderada de razões (aproximadamente 1 mais a variação) e aplicado como (1 + I), o que duplica a tarifa no primeiro reajuste; há três fórmulas diferentes para o mesmo reajuste. O Fator de Avaliação, de até 4% de redução, incide sobre a base já reajustada, sem piso nem recuperação, e a nota exatamente igual a 90% não cai em faixa alguma. A taxa de regulação é de 0,5% com banda de neutralidade fixada entre 1% e 2%.",
    fund: "art. 23, IV, da Lei n.º 8.987/1995; art. 6.º, § 1.º, da Lei n.º 11.079/2004; art. 37 da Lei n.º 11.445/2007" },
  { tema: "Remuneração e reajuste", prev: "Contrato: cl. 25.2, 26.2.1.4, 26.3.3, 26.3.5, 26.3.9 a 26.3.13, 26.4.3 e 26.4.4",
    com: "O reequilíbrio exige “onerosidade excessiva” demonstrada por laudo pericial, sob pena de não conhecimento. O direito é renunciado se não exercido em cinco anos. A agência decide o cabimento em 60 dias, sem prazo para conclusão, e sem acordo o concedente escolhe o mecanismo a seu exclusivo critério. Fluxo de caixa marginal para todo evento, com taxa de 3,874% real mais NTN-B, sem memória de cálculo.",
    fund: "art. 9.º, §§ 2.º a 4.º, e art. 10 da Lei n.º 8.987/1995; art. 5.º, III, da Lei n.º 11.079/2004; art. 37, XXI, da CF/1988" },
  { tema: "Remuneração e reajuste", prev: "Edital: item 3.1.5; Contrato: cl. 5.1.5, 18.15, 18.17, 32.3, 32.4, 37.6, 39.6 e 44.2.4; Anexo V (Matriz), item 42",
    com: "Reversão “sem valor residual” convive com indenização do investimento não amortizado e com a matriz que aloca esse risco à concessionária. A célula deve reverter com cinco anos de vida útil e a concessionária deve iniciar nova célula dois anos antes do fim, embora a vida útil exigida supere o prazo do contrato. A amortização integral é imposta apesar de o contrato reconhecer prazos fiscais maiores. O aterro “inicial” é declarado não reversível.",
    fund: "art. 35 e art. 36 da Lei n.º 8.987/1995; art. 5.º, I, da Lei n.º 11.079/2004", vt: true },
  // ---- REGULAÇÃO E SANÇÕES ----
  { tema: "Regulação e sanções", prev: "Edital: preâmbulo e item 34.2; Contrato: preâmbulo, cl. 28, 30.1.1, 30.1.2.5, 30.1.9 e 30.1.12; Anexo IV, item 1.1",
    com: "A AGERSA regula “até que eventualmente” se crie agência intermunicipal; não há convênio de delegação juntado nem regra de transição. Agência e concedente aplicam penalidades, com recurso da autarquia estadual ao Presidente do consórcio e multas revertidas ao consórcio. A declaração de inidoneidade é atribuída à agência. A designação de entidade reguladora é condição de validade do contrato.",
    fund: "art. 8.º, § 5.º, art. 11, III, e arts. 21 a 23 da Lei n.º 11.445/2007; art. 156, § 6.º, da Lei n.º 14.133/2021" },
  { tema: "Regulação e sanções", prev: "Anexo IV: itens 1, 1.1, 3.5, Tabelas 3, 4 e 8, indicadores 10, 11, 12 e 13",
    com: "A “nota recebida” de cada indicador não tem regra de conversão, de modo que a nota total que define o Fator de Avaliação não é calculável. As faixas de enquadramento divergem dentro do próprio anexo. Dois indicadores exigem crescimento perpétuo em relação ao ano anterior, um mede em número de viagens, e dois são de percepção do usuário. As normas de apuração serão editadas depois da contratação.",
    fund: "art. 5.º, VII, da Lei n.º 11.079/2004; art. 23, III, da Lei n.º 8.987/1995" },
  { tema: "Regulação e sanções", prev: "Edital: itens 34.3.2, 34.7, 34.18 a 34.21; Contrato: cl. 1.1, 3.1.3, 30.1.2.2, 30.1.15 a 30.1.19",
    com: "As penalidades do edital divergem das do contrato em alíquota (0,1% contra 0,5% ao dia), prazo de tolerância (90 dias contra 6 meses), suspensão (2 contra 3 anos) e multa por rescisão (2% contra 1%). O contrato declara prevalecer sobre o edital e o anexo “mais recente” sobre os demais. A intervenção é automática ao atingir o teto mensal de multas.",
    fund: "art. 5.º e art. 92, XIV, da Lei n.º 14.133/2021; art. 5.º, II, da Lei n.º 11.079/2004; arts. 32 e 33 da Lei n.º 8.987/1995" },
  // ---- FORMAIS / FINANCIAMENTO ----
  { tema: "Procedimento", prev: "Edital: preâmbulo (consulta e audiência pública; Processo TCM/BA 03450e26) e item 16.6; Certidão TCM/BA, Processo 482352",
    com: "A audiência pública ocorreu em 31/10/2025 e a consulta não tem datas informadas. O critério de julgamento foi alterado depois, por deliberação do TCM/BA, de modo que a minuta submetida à consulta não é a licitada. A análise prévia do edital foi autuada no TCM/BA em 27/08/2026, um dia após a publicação, e pode deslocar o calendário.",
    fund: "art. 10, VI, da Lei n.º 11.079/2004; art. 11, IV, da Lei n.º 11.445/2007" },
  { tema: "Financiamento e controle", prev: "Edital: itens 6.6 e 25.5.3 e 25.5.4; Contrato: cl. 33.3, 33.5, 35.9, 39.1.8, 44.1.8 e 44.2",
    com: "A assunção de controle pelos financiadores depende de autorização casuística, sem prazo. O edital libera a oneração de ações sem anuência; o contrato exige aprovação prévia do concedente e “das agências”. A transferência de controle é livre após cinco anos, mas a transferência sem anuência é causa de caducidade. O “aporte-dívida via debêntures” foi transplantado de contrato de água e esgoto, está duplicado e não tem valores nem fonte.",
    fund: "art. 27, art. 27-A e art. 28 da Lei n.º 8.987/1995; art. 9.º, § 1.º, da Lei n.º 11.079/2004" },
];

const reserva = [
  { prev: "Edital: itens 15.4.7, 15.4.9, 15.5.1.1 e 15.5.1.2; item 6.4, alínea c",
    com: "Barreiras de porte que o grupo tende a atender: capital social de R$ 100,4 milhões, índices por consorciada, quinze parcelas de atestado e acervo de empresas do mesmo grupo econômico admitido. As vedações de participação por sanção alcançam só os municípios do consórcio." },
  { prev: "Anexo I, item 10.5; Anexo IV, item 4.1; Contrato: cl. 8.9.3, 31.2 e 45.7.2; Anexo I, item 10.2.2 (Coeficiente de Geração)",
    com: "Erros de redação favoráveis, se lidos literalmente: reajuste aplicado como (1 + I); aporte por inadimplência sem franquia na cláusula 8.9.3; seguros complementares a cargo do concedente; reequilíbrio a favor da concessionária por risco próprio na operação assistida; Coeficiente de Geração de 0,0095 contra 0,0086 calculado." },
  { prev: "Anexo I, item 3.10.3.1; Contrato: cl. 18.12, 18.15, 35.9 e 8.2.1; Anexo V (Matriz), itens 14 e 17; Anexo XX, Anexo A, cl. 5.1.5",
    com: "Alocações favoráveis: exclusão contratual do passivo dos lixões e do pós-encerramento; risco tributário e de mudança de lei ao concedente; pagamento por boletim de medição quando faltar atestado público; transferência de controle livre após cinco anos; receitas acessórias amplas e pré-autorizadas com só 3% de compartilhamento, sem compartilhamento de ganhos de refinanciamento." },
  { prev: "Anexo III (EVEF), Tabelas 3, 16, 28 e premissas de WACC e tributos",
    com: "Folgas de modelagem: sem redução de IRPJ da SUDENE, sem benefício fiscal da dívida, sem créditos de PIS/COFINS, WACC de 11,86% real, TUF de RDO a cerca de R$ 713/t contra TEP de R$ 312,78/t e possível dupla contagem de R$ 135 milhões em destinação final." },
  { prev: "Anexo I, itens 1.4, 4 e 9; Contrato: cl. 31.1; Anexo IV",
    com: "Especificações frouxas: renovação de frota a 120 e 180 meses; importâncias seguradas mínimas de R$ 356 mil; nenhum indicador para aterro e ETRs; alternativa regional de destinação (Caetité e Bom Jesus da Lapa) descartada sem demonstração." },
];

// ---------- helpers ----------
const run = (t, o = {}) => new TextRun({ text: t, font: FONT, size: o.size || 20, bold: o.bold, italics: o.italics, color: o.color });
const para = (t, o = {}) => new Paragraph({ alignment: o.align || AlignmentType.JUSTIFIED, spacing: { after: o.after ?? 120, line: o.line || 276 }, children: Array.isArray(t) ? t : [run(t, o)] });
const border = { style: BorderStyle.SINGLE, size: 4, color: "808080" };
const borders = { top: border, bottom: border, left: border, right: border };
const cell = (children, w, o = {}) => new TableCell({
  width: { size: w, type: WidthType.DXA }, borders, margins: { top: 60, bottom: 60, left: 90, right: 90 },
  shading: o.shade ? { type: ShadingType.CLEAR, fill: o.shade, color: "auto" } : undefined,
  verticalAlign: "top", children,
});
const hcell = (t, w) => cell([para([run(t, { bold: true, size: 18 })], { align: AlignmentType.LEFT, after: 0 })], w, { shade: "D9D9D9" });
const tcell = (t, w, o = {}) => cell([para([run(t, { size: 18, ...o })], { align: AlignmentType.LEFT, after: 0, line: 240 })], w, o);

// landscape A4: 16838 wide; margins 850 each => 15138 usable
const W = [560, 1500, 3000, 6878, 3200]; // sum 15138
const RW = [560, 3600, 10978];

function tableMain() {
  const rows = [new TableRow({ tableHeader: true, children: [hcell("Nº", W[0]), hcell("Tema", W[1]), hcell("Previsão editalícia / contratual", W[2]), hcell("Comentário", W[3]), hcell("Fundamento", W[4])] })];
  pts.forEach((p, i) => {
    const comChildren = [run(p.com, { size: 18 })];
    if (p.vt) comChildren.push(run(" [VALIDAÇÃO TÉCNICA: ponto depende de confirmação de engenharia ou modelagem]", { size: 18, italics: true }));
    rows.push(new TableRow({ cantSplit: false, children: [
      tcell(String(i + 1), W[0]),
      tcell(p.tema, W[1]),
      tcell(p.prev, W[2]),
      cell([para(comChildren, { align: AlignmentType.JUSTIFIED, after: 0, line: 240 })], W[3]),
      tcell(p.fund, W[4]),
    ] }));
  });
  return new Table({ width: { size: 15138, type: WidthType.DXA }, columnWidths: W, rows });
}
function tableReserva() {
  const rows = [new TableRow({ tableHeader: true, children: [hcell("Nº", RW[0]), hcell("Previsão editalícia / contratual", RW[1]), hcell("Comentário", RW[2])] })];
  reserva.forEach((p, i) => rows.push(new TableRow({ children: [tcell("R" + (i + 1), RW[0]), tcell(p.prev, RW[1]), cell([para([run(p.com, { size: 18 })], { after: 0, line: 240 })], RW[2])] })));
  return new Table({ width: { size: 15138, type: WidthType.DXA }, columnWidths: RW, rows });
}

const doc = new Document({
  styles: { default: { document: { run: { font: FONT, size: 24 } } } },
  sections: [{
    properties: { page: { size: { width: 11906, height: 16838, orientation: PageOrientation.LANDSCAPE }, margin: { top: 850, bottom: 850, left: 850, right: 850 } } },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.RIGHT, children: [run("[USO INTERNO] · Fase 1 · sem jurisprudência · página ", { size: 16 }), new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 16 })] })] }) },
    children: [
      para([run("CONCORRÊNCIA PÚBLICA N.º 001/2026 – CDS VELHO CHICO (BA) — PONTOS JURÍDICOS", { bold: true, size: 26 })], { align: AlignmentType.LEFT, after: 60 }),
      para([run("Concessão patrocinada dos serviços de coleta, transporte, transbordo, triagem, tratamento e destinação final de RDO, RPU, RCD e RSS e coleta seletiva nos Municípios de Ibotirama, Paratinga, Oliveira dos Brejinhos, Muquém do São Francisco e Morpará", { size: 20 })], { align: AlignmentType.LEFT, after: 60 }),
      para([run("Órgão: Consórcio de Desenvolvimento Sustentável do Velho Chico. Modalidade: concorrência presencial (B3), critério menor tarifa (multiplicador K). Valor estimado: R$ 1.004.249.630,25 (30 anos de receita, base jul/2026). Edital publicado em 26/08/2026; errata em 27/08/2026; análise prévia no TCM/BA (Proc. 482352) autuada em 27/08/2026. Impugnação até 13/10/2026; entrega dos envelopes em 16/10/2026; sessão pública em 22/10/2026.", { size: 20 })], { align: AlignmentType.LEFT, after: 60 }),
      para([run("[USO INTERNO] — Versão 1 (leitura de 02/09/2026). Lista de Fase 1: sem jurisprudência, sem classificação de força de tese. A coluna de acompanhamento de republicação será acrescentada se houver nova versão do edital. Os IDs completos de cada achado estão nos relatórios E1 a E4 do projeto.", { size: 20, italics: true })], { align: AlignmentType.LEFT, after: 200 }),
      tableMain(),
      new Paragraph({ spacing: { before: 360, after: 120 }, children: [run("[RESERVA — NÃO PROTOCOLAR]", { bold: true, size: 24 })] }),
      para([run("Pontos que podem funcionar como vantagem competitiva do grupo. Não devem ser levantados publicamente; a decisão de reservar ou suscitar é exclusiva do advogado.", { size: 20, italics: true })], { align: AlignmentType.LEFT, after: 120 }),
      tableReserva(),
    ],
  }],
});

Packer.toBuffer(doc).then(b => { fs.writeFileSync(process.argv[2], b); console.log("ok", b.length); });
