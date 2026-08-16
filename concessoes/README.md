# concessoes/

Diretório-guarda-chuva dos projetos de **concessão comum** (Lei 8.987/1995), **concessão patrocinada** e **concessão administrativa** (Lei 11.079/2004) em RSU e limpeza urbana.

Um repositório único, um diretório por certame. Não abrir repositório novo por projeto.

## Como adicionar um projeto

```bash
# a partir da raiz do repositório
ferramentas/novo_projeto.sh concessao rio-claro-conc032-2026
```

O script cria o diretório a partir de `_template/` e lista os próximos passos. Sem o script, basta copiar o template:

```bash
cp -r concessoes/_template concessoes/rio-claro-conc032-2026
```

Depois:

1. Colocar os documentos do edital (PDF/DOCX) em `docs/`.
2. Preencher `README.md` do projeto (ficha: órgão, modalidade, objeto, datas, status).
3. Preencher `CLAUDE.md` do projeto com o que não está nos documentos — legislação estadual, determinações anteriores do TCE, histórico de impugnações, atestados disponíveis.
4. Registrar o projeto na tabela de índice abaixo.
5. Executar `FASE1 [projeto]` no Claude Code.

## Convenção de nome de diretório

`[municipio]-[modalidade][numero]-[ano]`, tudo em minúsculas, sem acento, separado por hífen.

| Modalidade | Prefixo | Exemplo |
|---|---|---|
| Concorrência (concessão comum) | `conc` | `marilia-conc020-2025` |
| Concorrência (PPP patrocinada/administrativa) | `ppp` | `santos-ppp008-2026` |
| Chamamento público / PMI / MIP | `pmi` | `macaiba-pmi003-2026` |

Município com nome composto mantém os hífens: `sao-jose-dos-campos-conc011-2026`.

## Estrutura de cada projeto

```
concessoes/[projeto]/
├── README.md              # ficha do certame (órgão, objeto, datas, status, versões)
├── CLAUDE.md              # contexto que não está nos documentos (opcional, mas recomendado)
├── docs/
│   ├── edital.pdf
│   ├── termo-referencia.pdf
│   ├── caderno-encargos.pdf
│   ├── minuta-contrato.pdf
│   ├── plano-negocios.pdf
│   ├── matriz-riscos.pdf
│   ├── [demais anexos]
│   ├── extraido/          # saída de pdftotext/pandoc (texto versionado, PDF é o original)
│   └── v2/                # republicação: nova versão dos documentos, para o agente CV
└── output/
    ├── v1/                # análise da versão original
    │   ├── fase1-triagem.yaml
    │   ├── fase1-extratores/
    │   ├── fase1-lista-consolidada.yaml
    │   ├── fase2-selecao.yaml
    │   ├── fase2-matriz-argumentos.yaml
    │   └── [exports .docx]
    └── v2/                # criado na republicação
        ├── cv-v1-v2.yaml
        └── [exports .docx atualizados]
```

`docs/v2/` só é criado quando há republicação. Para uma terceira versão, `docs/v3/`, e assim por diante — a versão original permanece na raiz de `docs/`. O `output/` é versionado em espelho (`v1/`, `v2/`...): reanalisar uma republicação **nunca sobrescreve** os YAML da versão anterior, que são o baseline do CV.

## Índice de projetos

| Projeto | Município/UF | Modalidade | Objeto | Fase | Status |
|---|---|---|---|---|---|
| [`marilia-ppp020-2025`](marilia-ppp020-2025/) | Marília/SP | Concorrência (concessão administrativa) | Tratamento e valorização de RSU — gaseificação/pirólise + biodigestão, 30 anos | FASE1 | em análise |
| [`civap-ppp001-2021`](civap-ppp001-2021/) | CIVAP (Vale do Paranapanema)/SP | Concorrência (concessão administrativa) | Tratamento e destinação de RSU com CTGE — certame homologado; gestão contratual e análise societária da SPE | análise documental | em análise |

Fase: `FASE1` (varredura) · `FASE2` (matriz) · `FASE3` (redação — humana) · `CV` (comparação versional).
Status: `em análise` · `impugnado` · `aguardando republicação` · `encerrado`.

## Regras aplicáveis

Este diretório herda o `CLAUDE.md` da raiz e adiciona o `CLAUDE.md` deste nível (normativa do regime concessório, checklists dos agentes E1–E4, padrões recorrentes de irregularidade). O `CLAUDE.md` de cada projeto, quando existe, é a terceira camada.

Documentos de terceiros e outputs marcados `[USO INTERNO]` ficam no repositório — o repositório é privado. Nada aqui é material para protocolo direto: a Fase 3 (redação de peça) é exclusivamente humana.
