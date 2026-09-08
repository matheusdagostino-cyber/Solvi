# Consulta — Consórcio AMSA (Maciço de Baturité/CE): dois contratos de destinação final

Consulta interna sobre a possibilidade de um município consorciado à AMSA manter, ao mesmo tempo, a destinação final contratada pelo consórcio (custeada pelo rateio) e um contrato próprio, direto, com a mesma unidade de destinação, para o volume excedente.

Não é análise de edital; por isso não segue o pipeline E1–E4/C/AN/R do `CLAUDE.md` raiz. As regras invioláveis (jurisprudência verificada, ancoragem normativa, sem juízo de força, flags `[VIT]`, `[PENDENTE]`, `[VALIDAÇÃO TÉCNICA]`, `[RESERVA]`) foram observadas.

## Conteúdo

| Arquivo | Descrição |
|---|---|
| `memo-dois-contratos-destinacao-final.md` | Memo interno `[USO INTERNO]` com resposta direta, fundamentos, análise, alternativas de estruturação, checklist e inventário dos 30 normativos da AMSA |
| `memo-dois-contratos-destinacao-final.docx` | Mesmo memo em Word (Times New Roman 12, espaçamento 1,5, A4) |
| `memo-cota-extra-estrutura-juridica.md` / `.docx` | Memo `[USO INTERNO]` restrito à estrutura jurídica da cota extra: os três instrumentos (contrato AMSA–unidade, contrato de rateio com franquia, contrato de programa) e a mecânica de apuração, preço, cobrança e pagamento do excedente |
| `fontes/links.md` | URLs de todos os documentos consultados |
| `fontes/contrato-consorcio-amsa-2018-trechos.md` | Transcrição das cláusulas relevantes do Contrato de Consórcio (versão 5/04/2018), feita a partir das imagens do anexo à Lei 334/2018 de Mulungu |
| `fontes/contrato-rateio-04-2025-baturite.md` | Resumo e transcrição das cláusulas financeiras do Contrato de Rateio 04/2025 (cota de R$ 30 mil/mês; autorização de retenção do ICMS/IQM pela SEFAZ) |
| `fontes/retencao-icms-iqm.md` | Onde está prevista a retenção do ICMS/IQM em favor da AMSA: documentos do consórcio, base estadual, modelo em outros consórcios cearenses, lacunas e precedentes de Tribunais de Contas `[VIT]` |
| `fontes/textos/` | Texto extraído (camada de texto ou OCR) dos estatutos, atas, editais de convocação, portarias, despacho do MP e leis de ratificação |

## Pendências registradas no memo

- Contrato atual de destinação final (aterro controlado): não está no repositório nem no portal da AMSA. Sem ele não é possível verificar exclusividade, quantitativos por município, preço e vigência.
- Plano regional integrado homologado pelo consórcio, resolução do Fundo Regional e contratos de programa município–AMSA: não localizados.
- Jurisprudência de Tribunais de Contas: não pesquisada (chave da API Lei na Mão ausente no ambiente).

## Como atualizar

1. Colocar o contrato atual de destinação final em `docs/` (criar a pasta) e revisar os itens 2.2, 5.4 e 7 do memo.
2. Rodar a busca no Lei na Mão (`ferramentas/buscar_tce.py`) com os termos sugeridos no item 8 do memo e incluir os resultados com flag `[VIT]`.
3. Regenerar o `.docx` com `pandoc memo-dois-contratos-destinacao-final.md -o memo-dois-contratos-destinacao-final.docx --reference-doc=<referência com Times New Roman 12, 1,5, justificado>`.
