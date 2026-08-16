# CLAUDE.md — civap-ppp001-2021 `[USO INTERNO]`

Herda o `CLAUDE.md` da raiz e o de `concessoes/`. **Este projeto não segue o fluxo FASE1→FASE3 de análise de edital**: o certame (CP 001/2021 do CIVAP) já foi homologado e contratado. O trabalho aqui é de **gestão contratual e análise documental/societária da concessionária** (BAL CIVAP SPE S.A.) — todo o conteúdo é estratégico e confidencial.

## Natureza do caso

Base documental reunida pela equipe sobre o ciclo completo do certame e da contratação: edital, TR, modelagens, impugnações (Revita e Energy) com julgamentos, contrato de concessão, e um acervo societário extenso da SPE e de suas integrantes/sócias (alterações contratuais, quadros societários, CNPJs, atas JUCESP, renúncias, substituições de administradores, ação judicial no RJ).

O ponto de partida analítico é o **dossiê da própria equipe** (`docs/extraido/dossie-documental-spe-bal-civap.md`/pdf, v1.0 de 30/07/2026) — relatório conclusivo do acervo. Qualquer análise nova deve partir dele e citá-lo, não redescobrir o que já está consolidado.

## Regras específicas deste projeto

1. **Confidencialidade reforçada** — nomes de empresas e pessoas aparecem em documentos societários. Outputs que possam circular externamente usam termos genéricos ("a concessionária", "a SPE", "as consorciadas"); nomes reais só em documentos marcados `[USO INTERNO]`.
2. **Nomes de arquivo do acervo são anotações internas da equipe** (ex.: sinalizações informais sobre onde estão os achados) — tratá-los como notas de trabalho, nunca reproduzi-los em output externo.
3. **Fatos societários exigem fonte documental precisa** — toda afirmação sobre alteração de sócios, administradores ou capital referencia o documento específico (arquivo + página) e, quando de registro público, o ato na JUCESP. Documento com OCR de baixa qualidade: conferir no original do Drive antes de afirmar.
4. **Sem juízo de força de tese** (regra inviolável 3) — o dossiê aponta caminhos (ex.: hipótese de dissolução do consórcio na ação do RJ); os agentes organizam fatos e fundamentos, a avaliação é do advogado.

## Linhas de análise sinalizadas pela equipe (a desenvolver sob direcionamento)

- Alterações societárias da SPE/consorciadas pós-contratação: regularidade frente ao edital, ao contrato e ao art. 9º da Lei 11.079/2004 (transferência de controle, composição, anuência do poder concedente) — os documentos-chave estão no acervo escaneado (OCR)
- Ação judicial no RJ envolvendo o consórcio — repercussão sobre a higidez da estrutura contratada
- Execução contratual vs. metas do TR (85% de redução de massa, CTGE ≤70 km, prazos de implantação)

## Acervo e OCR

- Manifesto completo com hashes: `docs/manifesto-acervo.yaml`
- 26 originais leves versionados em `docs/`; 32 escaneados só como texto OCR em `docs/extraido/` (originais no Drive, id `16TLigxWmHAWefGkAHvkVlxPdwkqlu7ly`)
- OCR feito com Tesseract `por` a 200dpi — qualidade variável em carimbos, assinaturas e tabelas JUCESP; **sempre conferir no original antes de citar em peça**

## Notas de leitura

- `EDITAL 01.2021.pdf`, TR, minutas, modelagens e julgamentos têm texto nativo — extração confiável.
- `CONTRATO CONCESSÃO.pdf` (23MB) é escaneado — texto via OCR; conferir cláusulas citadas no original.
- Documentos societários volumosos (25–93MB) são cópias digitalizadas de atos registrais — OCR serve para busca, não para transcrição literal.
