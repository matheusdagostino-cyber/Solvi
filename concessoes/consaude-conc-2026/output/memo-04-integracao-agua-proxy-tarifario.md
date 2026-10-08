# CONSAÚDE — Integração com a prestadora de água e o proxy tarifário (consumo de água)

**[USO INTERNO]** · Memo interno nº 04 · 08/10/2026
**Base:** Edital; Contrato (itens 7.4, 13, 17, 19, 39); Anexo 5 (item 4.8); Anexo 6 (Arranjo Tarifário); Anexo 7 (Matriz de Riscos); Plano de Negócio (itens 4.3 e 5.3–5.4); PIGIRS (Tabela 42).
**Textos legais conferidos:**
- art. 35 da Lei n.º 11.445/2007, redação da Lei n.º 14.026/2020, conferido no Planalto em 08/10/2026;
- art. 26 da Lei n.º 13.709/2018, conferido no Jus IA.

Sem juízo de força; nenhuma jurisprudência pesquisada.

---

## 1. Resposta curta

**Não há integração formalizada entre o CONSAÚDE e a prestadora de água.** Mesmo assim, todo o proxy tarifário depende de dados que só ela tem.

- A prestadora de água é a **SABESP nos 16 municípios**. O esgoto é prestado pelas prefeituras (PIGIRS, Tabela 42, fonte SNIS-2023).
- O **cofaturamento foi tentado e não saiu**: "as negociações com as concessionárias de água dos municípios não resultaram no interesse necessário" (Plano de Negócio, item 4.3). Por isso, o modelo adota **fatura própria** da concessionária.
- **Nenhum documento da SABESP consta dos autos disponíveis**: nem convênio, nem termo de cooperação, nem carta de anuência, nem protocolo de compartilhamento de dados.
- O contrato só prevê convênio de cobrança conjunta **facultativo**, a ser firmado **pela concessionária**. O CONSAÚDE se obriga apenas a "envidar seus melhores esforços" (Contrato, itens 7.4.3 e 7.4.4). A não celebração do convênio é **risco da concessionária** (Edital, item 4.4.4; Matriz, itens 59 e 79).
- Base legal: a cobrança na fatura de outro serviço público depende da "**anuência da prestadora do serviço**" (art. 35, § 1.º, da Lei n.º 11.445/2007). O consumo de água é parâmetro admitido (art. 35, IV), mas o *caput* exige considerar a destinação adequada e "o nível de renda da população da área atendida".

---

## 2. Onde o proxy depende da prestadora de água

| Elemento do proxy | Regra | Quem fornece o dado | Risco (Anexo 7) |
|---|---|---|---|
| **Cadastro Inicial** | O Poder Concedente entrega, como condição da OS, o cadastro dos usuários de água e esgoto, "respondendo pela sua obtenção junto à prestadora" (Contrato, 7.4.1) | SABESP, via Poder Concedente | **Público**: inconsistência ou incompletude material do Cadastro Inicial (item 36; Contrato, 17.6) |
| **Base cadastral** | A concessionária constitui e atualiza a base, incluindo economias sem ligação de água (7.4.2). Deve atualizar "sempre que o prestador de serviço de água e esgoto incluir novo usuário" e fazer novo levantamento a cada 5 anos (Anexo 5, item 4.8). | Concessionária, com dados da SABESP | **Privado**: falha na atualização da base (item 37) |
| **Volume faturado de cada economia** | VA = **média do consumo de água do ano anterior**, aplicada às 12 faturas seguintes. Mínimo de 10 m³/mês; economias sem medição pagam sempre 10 m³ (Anexo 6, item 1.2.2) | **Só a SABESP tem o dado mensal por ligação** | **Não há item específico** (ver ponto A2) |
| **Obrigação de dados contínuos** | O Poder Concedente deve obter dos municípios, "na forma dos respectivos CONTRATOS DE PROGRAMA", e assegurar "as informações cadastrais **e de consumo** necessárias [...] à cobrança das TARIFAS" (Contrato, 13, XV, ii) | Municípios → SABESP | Não mapeado |
| **Categoria do usuário / Fator de Uso** | A caracterização da economia "se dará conforme cadastro utilizado pelo agente responsável pela gestão dos serviços de fornecimento de água" (Anexo 6, Tabela 1 e nota) | Classificação da SABESP | **Compartilhado**: variação de mais de 5 p.p. em torno de **42,12%** de economias na tarifa social (item 46) |
| **Coeficiente de Geração** (CG = 3,3570 kg/m³) | Revisão com base em gravimetria e em "dados de consumo de água fornecidos pela prestadora" (Contrato, item 19; Anexo 6, item 1.6) | SABESP, ou sistema da concessionária | Privado entre revisões (item 52); compartilhado acima de ±3% (item 53) |
| **Rurais sem água** | 10 m³ × TB × Fator de Uso 0,5, com inclusão feita pela concessionária com apoio do Poder Concedente (Anexo 6) | Levantamento próprio | — |
| **Troca do proxy** | Alteração do proxy ou fixação de tarifa média | — | **Público**, com reequilíbrio (item 31) |
| **Modalidade de cobrança** | Fatura própria ou cobrança conjunta | — | **Privado** (itens 59 e 79) |

---

## 3. Números do proxy no modelo de referência (Plano de Negócio, itens 5.3–5.4)

"O número de economias e o volume faturado inicial foram estimados com base em dados da Sabesp", do SNIS e de dados municipais.

| Item | 2027 | 2056 |
|---|---|---|
| Economias ativas de água | 227.520 | 247.053 |
| Volume de água faturado (m³/ano) | 26.546.029 | 28.597.709 |
| Economias na tarifa social (social + vulnerável) | 95.843 (42,12%) | — |
| Unidades rurais sem ligação de água | 20.130 | — |
| Tarifa média | R$ 38,01 por economia/mês | — |

**Litoral (Itanhaém e Mongaguá):**
- concentram **61% das economias** (138.026);
- têm consumo médio de **8,8 e 7,9 m³/mês**, abaixo do mínimo de 10 m³;
- têm **1,4 e 1,2 habitantes por economia**, perfil de segunda residência.

Na prática, nesses dois municípios o proxy tende a funcionar como **taxa fixa pelo mínimo**. **[VALIDAÇÃO TÉCNICA]**

---

## 4. Pontos identificados (classificação preliminar)

| # | Ponto | Classificação | Dispositivo |
|---|---|---|---|
| A1 | **Dados de consumo contínuos sem instrumento.** O VA anual de cada economia exige dados mensais por ligação da SABESP durante 30 anos. A obrigação de fornecê-los é do Poder Concedente, que os obteria "dos municípios, na forma dos Contratos de Programa" (13, XV, ii). A SABESP, porém, não está vinculada a esses Contratos de Programa, e não há convênio, termo ou anuência nos autos. | DEPENDE DE FATO (contratos da SABESP com os municípios; eventual convênio) | art. 35, IV e § 1.º, da Lei n.º 11.445/2007; art. 23, IV, da Lei n.º 8.987/1995 |
| A2 | **Risco residual mal alocado.** A Matriz só aloca ao Poder Concedente o **Cadastro Inicial** (item 36). A falha no fornecimento contínuo de dados de consumo não tem item próprio. Pelo item 28.2.3 do Edital, risco não listado é **da concessionária**, embora a obrigação de fornecer os dados seja do Poder Concedente (13, XV, ii). | IRREGULAR (contradição obrigação × alocação) | art. 23, IV, da Lei n.º 8.987/1995; Edital, 28.2.3; Contrato, 13, XV |
| A3 | **Tarifa social sem critério e com remissões a itens inexistentes.** O Contrato (17.8) e o Apêndice 1 remetem aos subitens **7.2.5 (tarifa social) e 7.2.6 (Fator de Inadimplência), que não existem**: o item 7.2 só tem o 7.2.1. O item 9.3 também remete a um "subitem 7.2.2" inexistente. O Apêndice 1 diz que os critérios de elegibilidade estão no Anexo 6, mas não estão. O Anexo 6 tem a categoria "Social" com fator 0,50, sem a categoria "vulnerável", que o Plano usa (82.533 economias). Na prática, a classificação de 42% das economias fica entregue ao cadastro e aos critérios da SABESP. | IRREGULAR (omissão / erro material) | art. 35, *caput*, da Lei n.º 11.445/2007 (nível de renda); art. 23, IV, da Lei n.º 8.987/1995 |
| A4 | **Periodicidade do Coeficiente de Geração contraditória.** O Anexo 6 prevê avaliação **anual** pela agência e aplica CG¹/CG em todo reajuste. O Contrato (item 19) prevê revisão excepcional **no fim do ano 2** e, depois, só nas **revisões ordinárias quinquenais**. A Matriz (item 52) aloca ao privado a variação "entre as revisões". | IRREGULAR (contradição interna) | art. 23, IV, da Lei n.º 8.987/1995 |
| A5 | **CG inicial não reproduzível.** Com os dados publicados, RDO do ano 1 (127.906 t) ÷ volume faturado do ano 1 (26,55 milhões de m³) = **4,82 kg/m³**, não os 3,3570 kg/m³ adotados. A diferença provavelmente vem de o denominador ser o volume faturado "para fins de cobrança" (com mínimo de 10 m³ e rurais), mas essa base não foi publicada. | DEPENDE DE FATO **[VALIDAÇÃO TÉCNICA]** | Anexo 6, item 1.6 |
| A6 | **Compartilhamento de dados pessoais sem base estruturada.** O Contrato (item 39) trata as partes como controladores independentes, mas não disciplina o recebimento de dados da SABESP. Pelo art. 26, § 1.º, da LGPD, a transferência de dados pelo Poder Público a entidade privada exige, entre outras hipóteses, "previsão legal" ou respaldo em "contratos, convênios ou instrumentos congêneres" (inciso IV), com comunicação à autoridade nacional (§ 2.º). Esse instrumento não está nos autos. | DEPENDE DE FATO | art. 26, § 1.º, IV, e § 2.º, da Lei n.º 13.709/2018 |
| A7 | **Cofaturamento só com anuência da prestadora** (art. 35, § 1.º). O Poder Concedente assume apenas "melhores esforços" e o risco é privado. O Plano registra que a negociação já fracassou na estruturação. A inadimplência de partida da fatura própria (18,7%) vem do histórico de outra concessionária com cobrança direta (Plano, nota 20). | Registro factual | art. 35, § 1.º, da Lei n.º 11.445/2007; Matriz, itens 47, 59 e 79 |

### Reserva estratégica — decisão do advogado

| # | Ponto | Roteamento sugerido |
|---|---|---|
| R1 | **[RESERVA — candidato]** A fatura própria, a gestão da base cadastral e a cobrança direta favorecem licitantes que já operam cobrança direta de RSU ou têm relação comercial com a SABESP para cofaturamento. A banda de inadimplência (±3,5%) e o risco de cobrança são privados. | DECISÃO COMERCIAL |

---

## 5. Contexto externo aos autos (verificar antes de usar)

- A SABESP foi **desestatizada em 2024**, e seus contratos com os municípios paulistas foram regionalizados (URAE-1). A ARSESP regula tanto a SABESP quanto esta concessão. **Verificar** se os contratos da SABESP com os 16 municípios, ou a regulação da ARSESP, preveem compartilhamento de cadastro e consumo com o prestador de RSU, ou cobrança de terceiros na fatura de água. Isso é o que resolveria o ponto A1. *Informação de contexto, não extraída dos documentos do certame.*
- A Ata da 876.ª Reunião da ARSESP (30/09/2026) trata de um Protocolo de Intenções para a **estruturação** da concessão. Não menciona a SABESP nem dados de consumo.

## 6. O que pedir ou verificar

1. Nota técnica ou registro das tratativas com a SABESP sobre cofaturamento e cessão de cadastro e consumo (o Plano cita a tentativa, sem anexar nada).
2. Contratos da SABESP com os 16 municípios (URAE-1): cláusulas sobre dados de usuários e cobrança de terceiros.
3. Memória de cálculo do CG = 3,3570 kg/m³ e do volume "para fins de cobrança".
4. Critérios de elegibilidade das categorias social e vulnerável, e a fonte (cadastro SABESP? CadÚnico?).
5. Texto dos subitens 7.2.5 e 7.2.6 do Contrato, que são citados mas não existem na minuta.
