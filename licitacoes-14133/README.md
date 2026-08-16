# licitacoes-14133/

Diretório-guarda-chuva dos projetos de **pregão** e **concorrência** da Lei 14.133/2021 em RSU e limpeza urbana (incluindo SRP).

Um repositório único, um diretório por certame. Não abrir repositório novo por projeto.

## Como adicionar um projeto

```bash
# a partir da raiz do repositório
ferramentas/novo_projeto.sh licitacao macaiba-pe023-2026
```

Depois:

1. Colocar os documentos do edital (PDF/DOCX) em `docs/`.
2. Preencher `README.md` do projeto (ficha: órgão, modalidade, objeto, datas, status).
3. Preencher `CLAUDE.md` do projeto com o que não está nos documentos — regulamento municipal da 14.133, determinações anteriores do TCE, histórico de impugnações, atestados disponíveis.
4. Registrar o projeto na tabela de índice abaixo.
5. Executar `FASE1 [projeto]` no Claude Code.

## Convenção de nome de diretório

`[municipio]-[modalidade][numero]-[ano]`, tudo em minúsculas, sem acento, separado por hífen.

| Modalidade | Prefixo | Exemplo |
|---|---|---|
| Pregão eletrônico | `pe` | `macaiba-pe023-2026` |
| Pregão presencial | `pp` | `itu-pp004-2026` |
| Concorrência (14.133) | `cc` | `bauru-cc012-2026` |
| Dispensa eletrônica | `de` | `itu-de101-2026` |

O prefixo `conc` é reservado ao regime de concessões (`concessoes/README.md`) — aqui, concorrência da 14.133 usa `cc` para não colidir. Município com nome composto mantém os hífens: `sao-jose-dos-campos-pe011-2026`.

## Estrutura de cada projeto

Idêntica à documentada em `concessoes/README.md`: `README.md` (ficha), `CLAUDE.md` (contexto extra-editalício), `docs/` (+ `extraido/`, `v2/` quando houver republicação) e `output/` versionado (`v1/`, `v2/`...).

## Índice de projetos

| Projeto | Município/UF | Modalidade | Objeto | Fase | Status |
|---|---|---|---|---|---|
| _(nenhum projeto ainda — registre aqui ao criar)_ | | | | | |

Fase: `FASE1` (varredura) · `FASE2` (matriz) · `FASE3` (redação — humana) · `CV` (comparação versional).
Status: `em análise` · `impugnado` · `aguardando republicação` · `encerrado`.

## Regras aplicáveis

Este diretório herda o `CLAUDE.md` da raiz e adiciona o `CLAUDE.md` deste nível (normativa 14.133, checklists dos agentes E1–E4, padrões recorrentes). O `CLAUDE.md` de cada projeto, quando existe, é a terceira camada.
