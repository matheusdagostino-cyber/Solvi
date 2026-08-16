#!/usr/bin/env bash
# Cria um diretório de projeto a partir do template do regime jurídico.
#
#   ferramentas/novo_projeto.sh concessao rio-claro-conc032-2026
#   ferramentas/novo_projeto.sh licitacao macaiba-pe023-2026
#
# Convenção de nome: [municipio]-[modalidade][numero]-[ano]
# minúsculas, sem acento, separado por hífen.

set -euo pipefail

uso() {
    cat <<'EOF'
uso: novo_projeto.sh <regime> <nome-do-projeto>

  regime          concessao | licitacao
  nome-do-projeto [municipio]-[modalidade][numero]-[ano]
                  ex.: rio-claro-conc032-2026, macaiba-pe023-2026

opções:
  -h, --help      esta mensagem
EOF
}

case "${1:-}" in
    -h|--help) uso; exit 0 ;;
    "")        uso >&2; exit 1 ;;
esac

regime="$1"
projeto="${2:-}"

if [ -z "$projeto" ]; then
    echo "erro: nome do projeto não informado" >&2
    uso >&2
    exit 1
fi

case "$regime" in
    concessao|concessoes) base="concessoes" ;;
    licitacao|licitacoes|14133) base="licitacoes-14133" ;;
    *) echo "erro: regime desconhecido '$regime' (use: concessao | licitacao)" >&2; exit 1 ;;
esac

# regex nativo do bash valida a string inteira (grep -q por linha aceitaria
# nome com newline embutido e criaria diretório fora da convenção)
if ! [[ "$projeto" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]]; then
    echo "erro: '$projeto' foge da convenção de nome" >&2
    echo "      use minúsculas, dígitos e hífen: [municipio]-[modalidade][numero]-[ano]" >&2
    exit 1
fi

raiz="$(cd "$(dirname "$0")/.." && pwd)"
template="$raiz/$base/_template"
destino="$raiz/$base/$projeto"

if [ ! -d "$template" ]; then
    echo "erro: template não encontrado em $base/_template" >&2
    exit 1
fi

if [ -e "$destino" ]; then
    echo "erro: $base/$projeto já existe" >&2
    exit 1
fi

cp -r "$template" "$destino"

cat <<EOF
criado: $base/$projeto

próximos passos:
  1. colocar os documentos do edital (PDF/DOCX) em $base/$projeto/docs/
  2. preencher a ficha em $base/$projeto/README.md
  3. preencher o contexto extra-editalício em $base/$projeto/CLAUDE.md
  4. registrar o projeto no índice de $base/README.md
  5. no Claude Code: FASE1 $projeto
EOF
