#!/usr/bin/env node
// Gera o DOCX da Fase 1 (big numbers + lista consolidada de pontos) a partir de um JSON.
// Uso: node ferramentas/utils/gerar_docx_fase1.js <entrada.json> <saida.docx>
// O JSON é produzido por ferramentas/utils/yaml_fase1_para_json.py a partir dos YAML do projeto.
// Padrão do CLAUDE.md raiz: Times New Roman 12, espaçamento 1,5, justificado, A4;
// tabelas com bordas e cabeçalho sombreado; [USO INTERNO] no cabeçalho; reservas segregadas.

const fs = require('fs');
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType,
  AlignmentType, HeadingLevel, BorderStyle, ShadingType, PageOrientation, Header,
  Footer, PageNumber, LevelFormat, PageBreak, VerticalAlign,
} = require('docx');

const [, , inPath, outPath] = process.argv;
if (!inPath || !outPath) {
  console.error('Uso: node gerar_docx_fase1.js <entrada.json> <saida.docx>');
  process.exit(1);
}
const data = JSON.parse(fs.readFileSync(inPath, 'utf8'));

const FONT = 'Times New Roman';
const BODY = 24; // 12 pt
const TABLE = 18; // 9 pt
const A4 = { width: 11906, height: 16838 };
const MARGIN = 1134; // 2 cm
const PORTRAIT_W = A4.width - 2 * MARGIN; // 9638
const LANDSCAPE_W = A4.height - 2 * MARGIN; // 14570
const HEADER_FILL = 'D9D9D9';
const RESERVA_FILL = 'FCE4D6';
const border = { style: BorderStyle.SINGLE, size: 4, color: '808080' };
const borders = { top: border, bottom: border, left: border, right: border };

function runs(text, opts = {}) {
  // Suporta **negrito** inline.
  const parts = String(text ?? '').split(/(\*\*[^*]+\*\*)/g).filter(Boolean);
  return parts.map((p) => p.startsWith('**') && p.endsWith('**')
    ? new TextRun({ text: p.slice(2, -2), bold: true, font: FONT, size: opts.size || BODY, italics: opts.italics })
    : new TextRun({ text: p, font: FONT, size: opts.size || BODY, bold: opts.bold, italics: opts.italics, color: opts.color }));
}

function para(text, opts = {}) {
  return new Paragraph({
    children: runs(text, opts),
    alignment: opts.align || AlignmentType.JUSTIFIED,
    spacing: { line: opts.line || 360, after: opts.after ?? 120, before: opts.before ?? 0 },
    numbering: opts.bullet ? { reference: 'bullets', level: 0 } : undefined,
    keepNext: opts.keepNext,
  });
}

function heading(text, level) {
  return new Paragraph({
    heading: level,
    children: [new TextRun({ text, font: FONT, bold: true, size: level === HeadingLevel.HEADING_1 ? 28 : 26 })],
    spacing: { before: 240, after: 120, line: 360 },
    keepNext: true,
  });
}

function cellParas(text, opts) {
  const lines = Array.isArray(text) ? text : String(text ?? '').split('\n');
  return lines.filter((l) => l !== undefined).map((l) => new Paragraph({
    children: runs(l, { size: TABLE, bold: opts.bold, italics: opts.italics }),
    alignment: opts.align || AlignmentType.LEFT,
    spacing: { line: 240, after: 40 },
  }));
}

function cell(text, width, opts = {}) {
  return new TableCell({
    borders,
    width: { size: width, type: WidthType.DXA },
    shading: opts.fill ? { fill: opts.fill, type: ShadingType.CLEAR, color: 'auto' } : undefined,
    margins: { top: 60, bottom: 60, left: 90, right: 90 },
    verticalAlign: VerticalAlign.TOP,
    children: cellParas(text, opts),
  });
}

function table(headers, rows, widths, opts = {}) {
  const total = widths.reduce((a, b) => a + b, 0);
  const head = new TableRow({
    tableHeader: true,
    cantSplit: true,
    children: headers.map((h, i) => cell(h, widths[i], { bold: true, fill: HEADER_FILL })),
  });
  const body = rows.map((r) => new TableRow({
    children: r.map((c, i) => cell(c, widths[i], { fill: opts.fill })),
  }));
  return new Table({ width: { size: total, type: WidthType.DXA }, columnWidths: widths, rows: [head, ...body] });
}

function pageHeader() {
  return new Header({
    children: [new Paragraph({
      alignment: AlignmentType.RIGHT,
      children: [new TextRun({ text: `[USO INTERNO] — ${data.meta.titulo_curto}`, font: FONT, size: 18, bold: true })],
    })],
  });
}

function pageFooter() {
  return new Footer({
    children: [new Paragraph({
      alignment: AlignmentType.CENTER,
      children: [new TextRun({ children: ['Página ', PageNumber.CURRENT, ' de ', PageNumber.TOTAL_PAGES], font: FONT, size: 18 })],
    })],
  });
}

function section(children, landscape = false) {
  return {
    properties: {
      page: {
        size: { width: A4.width, height: A4.height, orientation: landscape ? PageOrientation.LANDSCAPE : PageOrientation.PORTRAIT },
        margin: { top: MARGIN, bottom: MARGIN, left: MARGIN, right: MARGIN },
      },
    },
    headers: { default: pageHeader() },
    footers: { default: pageFooter() },
    children,
  };
}

function flagsText(p) {
  const f = [];
  if (p.flag_tecnico) f.push('[VALIDAÇÃO TÉCNICA]');
  if (p.flag_reserva) f.push(p.reserva_tipo === 'DECISAO_COMERCIAL' ? '[DECISÃO COMERCIAL]' : '[RESERVA]');
  if (p.fonte_externa) f.push('[FONTE EXTERNA — VERIFICAR]');
  return f.join('\n') || '—';
}

function comentario(p) {
  const out = [p.comentario || ''];
  if (p.tipo_achado === 'DEPENDE_DE_FATO' && p.depende_de) out.push(`**Depende de:** ${p.depende_de}`);
  if (p.flag_tecnico) out.push('[VALIDAÇÃO TÉCNICA: ponto depende de confirmação de engenharia]');
  return out.join('\n');
}

function numCell(p) {
  return [`**${p.id}**`, (p.ids_origem || []).join(', ')];
}

// ---------- Conteúdo ----------
const temasOrdem = data.temas;
const temaNome = data.temas_nomes;
const pontos = data.pontos;
const isPublicavel = (p) => !p.flag_reserva;

const portrait1 = [];
portrait1.push(new Paragraph({
  alignment: AlignmentType.CENTER,
  spacing: { after: 120 },
  children: [new TextRun({ text: data.meta.titulo, font: FONT, size: 32, bold: true })],
}));
portrait1.push(new Paragraph({
  alignment: AlignmentType.CENTER,
  spacing: { after: 240 },
  children: [new TextRun({ text: '[USO INTERNO]', font: FONT, size: BODY, bold: true, color: 'C00000' })],
}));
portrait1.push(table(['Campo', 'Informação'], data.meta.identificacao.map((r) => [r[0], r[1]]), [2600, PORTRAIT_W - 2600]));
portrait1.push(para('', { after: 0 }));
portrait1.push(heading('Nota metodológica', HeadingLevel.HEADING_1));
data.nota_metodologica.forEach((t) => portrait1.push(para(t, { bullet: true, after: 60 })));

// Quadro-resumo
portrait1.push(heading('Quadro-resumo da Fase 1', HeadingLevel.HEADING_1));
const resumoRows = temasOrdem.map((t) => {
  const pt = pontos.filter((p) => p.tema === t);
  const c = (fn) => String(pt.filter(fn).length);
  return [temaNome[t], c((p) => p.tipo_achado === 'IRREGULAR' && isPublicavel(p)), c((p) => p.tipo_achado === 'DEPENDE_DE_FATO' && isPublicavel(p)), c((p) => p.flag_reserva), c((p) => p.tipo_achado === 'CONFORME')];
});
const tot = (i) => String(resumoRows.reduce((a, r) => a + Number(r[i]), 0));
resumoRows.push(['**Total**', `**${tot(1)}**`, `**${tot(2)}**`, `**${tot(3)}**`, `**${tot(4)}**`]);
portrait1.push(table(['Tema', 'Irregular', 'Depende de fato', 'Reserva / decisão comercial', 'Conforme'], resumoRows, [3838, 1300, 1500, 1700, 1300]));
portrait1.push(para(data.nota_resumo, { size: 20, italics: true, before: 60 }));

// Big numbers
portrait1.push(new Paragraph({ children: [new PageBreak()] }));
portrait1.push(heading('1. Big numbers', HeadingLevel.HEADING_1));
portrait1.push(para(data.big_numbers_intro));
data.big_numbers.forEach((g) => {
  portrait1.push(heading(g.grupo, HeadingLevel.HEADING_2));
  portrait1.push(table(['Item', 'Valor', 'Fonte / observação'], g.itens.map((x) => [x.item, `**${x.valor}**`, x.obs ? `${x.fonte}\n${x.obs}` : x.fonte]), [2700, 2738, 4200]));
});

// Pontos impugnáveis (IRREGULAR, não reserva)
const W5 = [1500, 2900, 6370, 2700, 1100];
function blocoPontos(filtro, titulo, intro) {
  const ch = [heading(titulo, HeadingLevel.HEADING_1), para(intro)];
  temasOrdem.forEach((t) => {
    const lista = pontos.filter((p) => p.tema === t && filtro(p));
    if (!lista.length) return;
    ch.push(heading(`${temaNome[t]} (${lista.length})`, HeadingLevel.HEADING_2));
    ch.push(table(['Nº / origem', 'Previsão editalícia / contratual', 'Problema e comentário', 'Fundamento normativo', 'Flags'],
      lista.map((p) => [numCell(p), p.dispositivo_editalicio, [`**${p.descricao_breve}**`, ...comentario(p).split('\n')], p.dispositivo_legal, flagsText(p)]), W5));
  });
  return ch;
}

const land1 = blocoPontos((p) => p.tipo_achado === 'IRREGULAR' && isPublicavel(p), '2. Pontos impugnáveis (IRREGULAR)', data.intro_irregular);
const land2 = blocoPontos((p) => p.tipo_achado === 'DEPENDE_DE_FATO' && isPublicavel(p), '3. Pontos que dependem de fato ou documento (candidatos a esclarecimento ou diligência)', data.intro_depende);

// Reserva
const land3 = [heading('4. [RESERVA — NÃO PROTOCOLAR]', HeadingLevel.HEADING_1), para(data.intro_reserva)];
const reservas = pontos.filter((p) => p.flag_reserva);
temasOrdem.forEach((t) => {
  const lista = reservas.filter((p) => p.tema === t);
  if (!lista.length) return;
  land3.push(heading(`${temaNome[t]} (${lista.length})`, HeadingLevel.HEADING_2));
  land3.push(table(['Nº / origem', 'Previsão editalícia / contratual', 'Ponto', 'Por que reservar / decisão', 'Tipo'],
    lista.map((p) => [numCell(p), p.dispositivo_editalicio, [`**${p.descricao_breve}**`, `(${p.tipo_achado})`, ...comentario(p).split('\n')], p.nota_reserva || '—', p.reserva_tipo === 'DECISAO_COMERCIAL' ? 'DECISÃO COMERCIAL' : 'RESERVA']), W5, { fill: RESERVA_FILL }));
});

// Diligência externa, lacunas, conformes
const portrait2 = [heading('5. Diligência externa (fontes fora do pacote do edital)', HeadingLevel.HEADING_1)];
data.dd.paragrafos.forEach((t) => portrait2.push(para(t.replace(/^- /, ''), { bullet: t.startsWith('- '), after: 80 })));
portrait2.push(heading('Fontes consultadas', HeadingLevel.HEADING_2));
data.dd.fontes.forEach((t) => portrait2.push(para(t, { bullet: true, size: 20, after: 40, align: AlignmentType.LEFT })));
portrait2.push(heading('6. Documentos e dados ausentes do pacote', HeadingLevel.HEADING_1));
data.lacunas.forEach((t) => portrait2.push(para(t, { bullet: true, after: 40 })));
portrait2.push(heading('7. Itens verificados e conformes (cobertura do checklist)', HeadingLevel.HEADING_1));
pontos.filter((p) => p.tipo_achado === 'CONFORME').forEach((p) => portrait2.push(para(`**${p.id}** — ${p.descricao_breve}: ${p.comentario}`, { bullet: true, after: 40, size: 20 })));

const doc = new Document({
  creator: 'solvi-editais — pipeline Fase 1',
  title: data.meta.titulo,
  styles: { default: { document: { run: { font: FONT, size: BODY } } } },
  numbering: { config: [{ reference: 'bullets', levels: [{ level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 540, hanging: 270 } } } }] }] },
  sections: [section(portrait1), section(land1, true), section(land2, true), section(land3, true), section(portrait2)],
});

Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync(outPath, buf);
  console.log(`DOCX gerado: ${outPath}`);
});
