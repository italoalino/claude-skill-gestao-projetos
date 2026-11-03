#!/usr/bin/env python3
"""Gera um status report de projeto em PowerPoint a partir do template neutro.
Builds a project status report in PowerPoint from the neutral template.

Uso / Usage:
    python3 build_status.py --data status.json --out status.pptx
    python3 build_status.py --data status.json --out status.pptx --template meu_template.pptx
    python3 build_status.py --data status.json --out status.pptx --lang en

O template tem 4 slides: capa, dois slides de conteúdo em branco e encerramento.
O script acha cada elemento pelo nome da forma ("Cover title" na capa, "Slide number"
nos slides de conteúdo), então dá para trocar cores, fontes, logo e textos do template
no PowerPoint à vontade, desde que esses dois nomes sejam mantidos (Página Inicial >
Organizar > Painel de Seleção). Nada é inventado: campo ausente aparece como "n/d".

O formato do JSON está em references/status-report.md. Aceita chaves em português ou inglês.
"""
import argparse
import copy
import json
import os
import sys

try:
    from lxml import etree
    from pptx import Presentation
    from pptx.dml.color import RGBColor
    from pptx.enum.shapes import MSO_SHAPE
    from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
    from pptx.oxml.ns import qn
    from pptx.util import Inches, Pt
except ImportError:
    sys.exit("Falta a biblioteca python-pptx. Instale com: pip install python-pptx / "
             "Missing python-pptx. Install it with: pip install python-pptx")

DEFAULT_LANG = "en"

NAVY = "0B2A6B"
GRAY = "5B6478"
TINT = "EEF3FC"
INK = "1F2937"
WHITE = "FFFFFF"
MUTED = "9AA3B5"
FONT = "Calibri"
GREEN, AMBER, RED = "2E9E5B", "E0A100", "D64545"

LABELS = {
    "pt": {
        "na": "n/d", "no_name": "Projeto sem nome", "empty": "Nenhum item informado",
        "no_risks": "Nenhum risco informado para este período",
        "period": "Período", "pm": "GP", "approach": "Abordagem",
        "s_summary": "Resumo do período", "s_risks": "Riscos, questões e decisões", "s_milestones": "Marcos e cronograma",
        "overall": "Status geral", "deadline": "Prazo", "complete": "Concluído", "budget": "Orçamento consumido",
        "deliverables": "Entregas do período", "next": "Próximos passos",
        "top_risks": "Principais riscos", "issues": "Questões abertas", "decisions": "Decisões necessárias",
        "h_risks": ["Risco", "P / I", "Resposta", "Dono"],
        "h_milestones": ["Marco", "Data", "Status", "Observação"],
        "rag": {"verde": "Verde", "amarelo": "Amarelo", "vermelho": "Vermelho"},
        "ms": {"concluido": "Concluído", "no_prazo": "No prazo", "em_risco": "Em risco",
               "atrasado": "Atrasado", "nao_iniciado": "Não iniciado"},
    },
    "en": {
        "na": "n/a", "no_name": "Unnamed project", "empty": "No items reported",
        "no_risks": "No risks reported for this period",
        "period": "Period", "pm": "PM", "approach": "Approach",
        "s_summary": "Period summary", "s_risks": "Risks, issues and decisions", "s_milestones": "Milestones and schedule",
        "overall": "Overall status", "deadline": "Deadline", "complete": "Complete", "budget": "Budget spent",
        "deliverables": "Delivered this period", "next": "Next steps",
        "top_risks": "Top risks", "issues": "Open issues", "decisions": "Decisions needed",
        "h_risks": ["Risk", "P / I", "Response", "Owner"],
        "h_milestones": ["Milestone", "Date", "Status", "Notes"],
        "rag": {"verde": "Green", "amarelo": "Amber", "vermelho": "Red"},
        "ms": {"concluido": "Completed", "no_prazo": "On track", "em_risco": "At risk",
               "atrasado": "Late", "nao_iniciado": "Not started"},
    },
}
L = LABELS[DEFAULT_LANG]

RAG_COLOR = {"verde": GREEN, "amarelo": AMBER, "vermelho": RED}
MS_COLOR = {"concluido": GREEN, "no_prazo": GREEN, "em_risco": AMBER, "atrasado": RED, "nao_iniciado": MUTED}

# Chaves e valores em inglês são convertidos para os nomes internos (português).
KEY_ALIASES = {
    "project": "projeto", "period": "periodo", "pm": "gp", "approach": "abordagem",
    "overall_status": "status_geral", "status_note": "status_texto", "deadline": "prazo",
    "percent_complete": "concluido_pct", "complete_basis": "concluido_base",
    "budget_pct": "orcamento_pct", "budget_note": "orcamento_texto",
    "deliverables": "entregas", "next_steps": "proximos_passos", "risks": "riscos",
    "issues": "questoes", "decisions": "decisoes", "milestones": "marcos",
    # dentro de prazo, riscos e marcos
    "value": "valor", "status": "situacao", "description": "descricao", "response": "resposta",
    "owner": "dono", "milestone": "marco", "date": "data", "notes": "obs",
}
VALUE_ALIASES = {
    "green": "verde", "amber": "amarelo", "yellow": "amarelo", "red": "vermelho",
    "completed": "concluido", "done": "concluido", "on_track": "no_prazo", "at_risk": "em_risco",
    "late": "atrasado", "delayed": "atrasado", "not_started": "nao_iniciado",
}

# Limites de itens por bloco. Vêm do espaço físico dos slides (10 x 5,625 pol.) e foram medidos
# renderizando o template: uma linha de 12 pt ocupa cerca de 0,22 pol. com o espaçamento entre
# itens, e a coluna de 4,4 pol. comporta cerca de 52 caracteres por linha.
# - entregas e próximos passos: área de 3,04 a 5,22 pol. (até o rodapé), cerca de 9 linhas
# - questões e decisões: área de 3,91 a 5,22 pol., cerca de 5 linhas
# - riscos: a tabela dá 0,5 pol. por linha (2 linhas de texto) e deixa espaço para os blocos abaixo
# - marcos: slide dedicado com linhas de 0,42 pol.; 7 linhas + cabeçalho ocupam cerca de 3,3 pol.
# Além do espaço, o status serve para leitura rápida: quem lê precisa ver só o que muda uma decisão.
LIMITS = {"entregas": 5, "proximos_passos": 5, "riscos": 3, "questoes": 3, "decisoes": 3, "marcos": 7}
# Itens acima de 100 caracteres passam de 2 linhas na coluna de 4,4 pol.
MAX_CHARS = {"entregas": 100, "proximos_passos": 100, "questoes": 100, "decisoes": 100}
CHARS_PER_LINE = 52
LINE_BUDGET = {"entregas": 9, "proximos_passos": 9, "questoes": 5, "decisoes": 5}
# Tabela de riscos: colunas de 4,0 pol. (descrição, ~60 caracteres por linha) e 2,9 pol. (resposta,
# ~42 caracteres por linha) em 11 pt; acima de 2 linhas a linha da tabela cresce e invade o bloco de baixo.
RISK_MAX_CHARS = {"descricao": 120, "resposta": 84}
# O subtítulo dos slides (projeto, período, GP, abordagem) cabe em uma linha de 9 pol. em 11 pt:
# cerca de 100 caracteres.
SUBTITLE_CHARS = 100

WARNINGS = []


def warn(msg):
    WARNINGS.append(msg)
    print(f"AVISO/WARNING: {msg}", file=sys.stderr)


def normalize(data):
    out = {KEY_ALIASES.get(k, k) if k not in ("status",) else k: v for k, v in data.items()}
    prazo = out.get("prazo")
    if isinstance(prazo, dict):
        out["prazo"] = {KEY_ALIASES.get(k, k): v for k, v in prazo.items()}
    if isinstance(out.get("riscos"), list):
        out["riscos"] = [{KEY_ALIASES.get(k, k): v for k, v in r.items()} for r in out["riscos"]]
    if isinstance(out.get("marcos"), list):
        marcos = []
        for m in out["marcos"]:
            mm = {}
            for k, v in m.items():
                k2 = "status" if k == "status" else KEY_ALIASES.get(k, k)
                mm[k2] = v
            marcos.append(mm)
        out["marcos"] = marcos
    return out


def norm_value(v):
    v = (v or "").strip().lower().replace(" ", "_")
    return VALUE_ALIASES.get(v, v)


def rgb(hex_):
    return RGBColor.from_string(hex_)


def add_text(slide, x, y, w, h, text, size=12, bold=False, color=INK,
             align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, name=None):
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    if name:
        box.name = name
    tf = box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = anchor
    p = tf.paragraphs[0]
    p.alignment = align
    r = p.add_run()
    r.text = text
    f = r.font
    f.name = FONT
    f.size = Pt(size)
    f.bold = bold
    f.color.rgb = rgb(color)
    return box


def add_bullets(slide, x, y, w, h, items, size=12, color=INK, name=None):
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    if name:
        box.name = name
    tf = box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(4)
        pPr = p._p.get_or_add_pPr()
        pPr.set("marL", "171450")
        pPr.set("indent", "-171450")
        bu_font = etree.SubElement(pPr, qn("a:buFont"))
        bu_font.set("typeface", "Arial")
        bu_char = etree.SubElement(pPr, qn("a:buChar"))
        bu_char.set("char", "•")
        r = p.add_run()
        r.text = str(item)
        r.font.name = FONT
        r.font.size = Pt(size)
        r.font.color.rgb = rgb(color)
    return box


def add_empty_note(slide, x, y, w, text=None):
    return add_text(slide, x, y, w, 0.3, text or L["empty"], size=12, color=MUTED)


def heading(slide, x, y, w, text):
    return add_text(slide, x, y, w, 0.3, text, size=14, bold=True, color=NAVY)


def add_card(slide, x, y, w, h, label, value, sub=None, dot_color=None, value_color=NAVY):
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    card.adjustments[0] = 0.08
    card.fill.solid()
    card.fill.fore_color.rgb = rgb(TINT)
    card.line.fill.background()
    card.shadow.inherit = False
    card.name = f"Card {label}"
    add_text(slide, x + 0.15, y + 0.12, w - 0.3, 0.2, label, size=10, color=GRAY)
    vx = x + 0.15
    if dot_color:
        d = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(vx), Inches(y + 0.4), Inches(0.26), Inches(0.26))
        d.fill.solid()
        d.fill.fore_color.rgb = rgb(dot_color)
        d.line.fill.background()
        d.shadow.inherit = False
        d.name = "Status dot"
        vx += 0.36
    add_text(slide, vx, y + 0.34, x + w - vx - 0.1, 0.4, value, size=22, bold=True, color=value_color,
             anchor=MSO_ANCHOR.MIDDLE)
    if sub:
        add_text(slide, x + 0.15, y + 0.76, w - 0.3, 0.3, sub, size=10, color=GRAY)
    return card


def style_cell(cell, runs, size=11, fill=WHITE, align=PP_ALIGN.LEFT):
    """runs: lista de (texto, cor, negrito)."""
    cell.margin_left = cell.margin_right = Inches(0.08)
    cell.margin_top = cell.margin_bottom = Inches(0.04)
    cell.vertical_anchor = MSO_ANCHOR.MIDDLE
    cell.fill.solid()
    cell.fill.fore_color.rgb = rgb(fill)
    tf = cell.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = align
    for text, color, bold in runs:
        r = p.add_run()
        r.text = str(text)
        r.font.name = FONT
        r.font.size = Pt(size)
        r.font.bold = bold
        r.font.color.rgb = rgb(color)


def add_table(slide, x, y, widths, header, rows, row_h=0.5, name="Table"):
    shape = slide.shapes.add_table(len(rows) + 1, len(widths), Inches(x), Inches(y),
                                   Inches(sum(widths)), Inches(0.36 + row_h * len(rows)))
    shape.name = name
    tbl = shape.table
    tbl.first_row = True
    tbl.horz_banding = False
    for i, w in enumerate(widths):
        tbl.columns[i].width = Inches(w)
    tbl.rows[0].height = Inches(0.36)
    for i, h in enumerate(header):
        style_cell(tbl.cell(0, i), [(h, WHITE, True)], fill=NAVY)
    for r_i, row in enumerate(rows, start=1):
        tbl.rows[r_i].height = Inches(row_h)
        fill = WHITE if r_i % 2 else TINT
        for c_i, runs in enumerate(row):
            style_cell(tbl.cell(r_i, c_i), runs, fill=fill)
    return shape


def clip(data, key):
    items = list(data.get(key) or [])
    limit = LIMITS[key]
    if len(items) > limit:
        warn(f"'{key}': {len(items)} itens, mantidos os {limit} primeiros / kept the first {limit}.")
        items = items[:limit]
    if key in MAX_CHARS:
        for it in items:
            if len(str(it)) > MAX_CHARS[key]:
                warn(f"'{key}': item com {len(str(it))} caracteres pode estourar a caixa / may overflow: "
                     f"\"{str(it)[:40]}...\"")
    if key in LINE_BUDGET:
        lines = sum(-(-len(str(it)) // CHARS_PER_LINE) for it in items)
        if lines > LINE_BUDGET[key]:
            warn(f"'{key}': cerca de {lines} linhas, a caixa comporta {LINE_BUDGET[key]}; o texto pode invadir "
                 f"o rodapé. Encurte os itens ou reduza a lista / about {lines} lines, the box fits "
                 f"{LINE_BUDGET[key]}; text may run into the footer. Shorten items or the list.")
    if key == "riscos":
        for r in items:
            for campo, limite in RISK_MAX_CHARS.items():
                if len(str(r.get(campo) or "")) > limite:
                    warn(f"riscos: '{campo}' com mais de {limite} caracteres faz a linha da tabela crescer e "
                         f"invadir o bloco de baixo / too long, the table row grows over the next block: "
                         f"\"{str(r.get(campo))[:40]}...\"")
    return items


def slide_title(slide, title, subtitle=None):
    add_text(slide, 0.5, 0.3, 9.0, 0.5, title, size=24, bold=True, color=NAVY, name="Title")
    if subtitle:
        add_text(slide, 0.5, 0.82, 9.0, 0.25, subtitle, size=11, color=GRAY, name="Subtitle")


def fmt_pct(v):
    if v is None or v == "":
        return L["na"]
    try:
        n = float(v)
    except (TypeError, ValueError):
        return str(v)
    return f"{n:g}%"


def find_shape(slide, name):
    for sh in slide.shapes:
        if sh.name == name:
            return sh
    return None


def build(data, template, out):
    prs = Presentation(template)
    slides = list(prs.slides)
    if len(slides) != 4:
        sys.exit("Template inesperado: esperados 4 slides (capa, 2 conteúdos, encerramento). / "
                 "Unexpected template: 4 slides expected (cover, 2 content, closing).")
    cover, blank_a, blank_b, closing = slides

    title_shape = find_shape(cover, "Cover title")
    if title_shape is None or find_shape(blank_a, "Slide number") is None:
        sys.exit("O template precisa das formas 'Cover title' (capa) e 'Slide number' (slide 2). / "
                 "Template needs shapes named 'Cover title' (cover) and 'Slide number' (slide 2).")

    # Tudo o que está no slide de conteúdo modelo (rodapé, barras, logo) é copiado para cada slide novo.
    base_elements = [sh._element for sh in blank_a.shapes if not sh.is_placeholder]
    layout = blank_a.slide_layout

    def new_content_slide(number):
        s = prs.slides.add_slide(layout)
        for ph in list(s.placeholders):
            ph._element.getparent().remove(ph._element)
        for el in base_elements:
            s.shapes._spTree.append(copy.deepcopy(el))
        num = find_shape(s, "Slide number")
        runs = num.text_frame.paragraphs[0].runs
        if runs:
            runs[0].text = str(number)
            for extra in runs[1:]:
                extra.text = ""
        return s

    projeto = data.get("projeto") or L["no_name"]
    periodo = data.get("periodo")
    partes = [p for p in (f"{L['period']}: {periodo}" if periodo else None,
                          f"{L['pm']}: {data['gp']}" if data.get("gp") else None,
                          f"{L['approach']}: {data['abordagem']}" if data.get("abordagem") else None) if p]
    # O subtítulo cabe em uma linha (cerca de 100 caracteres a 11 pt). Se estourar,
    # encurta o nome do projeto no subtítulo; o nome completo continua na capa.
    sep = "   |   "
    resto = sep.join(partes)
    espaco = SUBTITLE_CHARS - len(resto) - (len(sep) if resto else 0)
    nome_sub = projeto
    if len(projeto) > max(espaco, 30):
        nome_sub = projeto[:max(espaco, 30) - 1].rstrip() + "…"
        warn(f"nome do projeto encurtado no subtítulo / project name shortened in subtitle: '{nome_sub}'")
    subtitulo = sep.join([nome_sub] + partes)

    # Capa
    tf = title_shape.text_frame
    p0 = tf.paragraphs[0]
    for extra_p in tf.paragraphs[1:]:
        extra_p._p.getparent().remove(extra_p._p)
    if p0.runs:
        run0 = p0.runs[0]
        for extra in p0.runs[1:]:
            extra.text = ""
    else:
        run0 = p0.add_run()
    run0.text = projeto
    n = len(projeto)
    if n > 60:
        run0.font.size = Pt(22)
    elif n > 32:
        run0.font.size = Pt(28)

    # Slide 2: resumo
    s1 = new_content_slide(2)
    slide_title(s1, L["s_summary"], subtitulo)
    cx, cy, cw, ch, gap = 0.5, 1.25, 2.1, 1.25, 0.2

    sg = norm_value(data.get("status_geral"))
    if sg in RAG_COLOR:
        add_card(s1, cx, cy, cw, ch, L["overall"], L["rag"][sg], data.get("status_texto"), dot_color=RAG_COLOR[sg])
    else:
        if sg:
            warn(f"status_geral '{sg}' inválido / invalid: use verde|amarelo|vermelho ou green|amber|red.")
        add_card(s1, cx, cy, cw, ch, L["overall"], L["na"], data.get("status_texto"), value_color=MUTED)

    prazo = data.get("prazo") or {}
    add_card(s1, cx + (cw + gap), cy, cw, ch, prazo.get("label") or L["deadline"],
             prazo.get("valor") or L["na"], prazo.get("situacao"),
             value_color=NAVY if prazo.get("valor") else MUTED)
    add_card(s1, cx + 2 * (cw + gap), cy, cw, ch, L["complete"], fmt_pct(data.get("concluido_pct")),
             data.get("concluido_base"), value_color=NAVY if data.get("concluido_pct") not in (None, "") else MUTED)
    add_card(s1, cx + 3 * (cw + gap), cy, cw, ch, L["budget"], fmt_pct(data.get("orcamento_pct")),
             data.get("orcamento_texto"), value_color=NAVY if data.get("orcamento_pct") not in (None, "") else MUTED)

    heading(s1, 0.5, 2.68, 4.4, L["deliverables"])
    heading(s1, 5.1, 2.68, 4.4, L["next"])
    entregas = clip(data, "entregas")
    proximos = clip(data, "proximos_passos")
    if entregas:
        add_bullets(s1, 0.5, 3.04, 4.4, 2.0, entregas, name="Deliverables")
    else:
        add_empty_note(s1, 0.5, 3.04, 4.4)
    if proximos:
        add_bullets(s1, 5.1, 3.04, 4.4, 2.0, proximos, name="Next steps")
    else:
        add_empty_note(s1, 5.1, 3.04, 4.4)

    # Slide 3: riscos, questões, decisões
    s2 = new_content_slide(3)
    slide_title(s2, L["s_risks"], subtitulo)
    riscos = clip(data, "riscos")
    heading(s2, 0.5, 1.15, 9.0, L["top_risks"])
    if riscos:
        rows = []
        for r in riscos:
            rows.append([
                [(r.get("descricao") or L["na"], INK, False)],
                [(r.get("pi") or L["na"], INK, True)],
                [(r.get("resposta") or L["na"], INK, False)],
                [(r.get("dono") or L["na"], INK, False)],
            ])
        add_table(s2, 0.5, 1.5, [4.0, 1.0, 2.9, 1.1], L["h_risks"], rows, row_h=0.5, name="Risks")
    else:
        add_empty_note(s2, 0.5, 1.5, 9.0, L["no_risks"])
    heading(s2, 0.5, 3.55, 4.4, L["issues"])
    heading(s2, 5.1, 3.55, 4.4, L["decisions"])
    questoes = clip(data, "questoes")
    decisoes = clip(data, "decisoes")
    if questoes:
        add_bullets(s2, 0.5, 3.91, 4.4, 1.3, questoes, name="Issues")
    else:
        add_empty_note(s2, 0.5, 3.91, 4.4)
    if decisoes:
        add_bullets(s2, 5.1, 3.91, 4.4, 1.3, decisoes, name="Decisions")
    else:
        add_empty_note(s2, 5.1, 3.91, 4.4)

    # Slide 4 (opcional): marcos
    marcos = clip(data, "marcos")
    n_content = 2
    if marcos:
        s3 = new_content_slide(4)
        n_content = 3
        slide_title(s3, L["s_milestones"], subtitulo)
        rows = []
        for m in marcos:
            st = norm_value(m.get("status"))
            if st in MS_COLOR:
                status_runs = [("● ", MS_COLOR[st], True), (L["ms"][st], INK, False)]
            else:
                if st:
                    warn(f"status de marco '{st}' inválido / invalid milestone status.")
                status_runs = [(L["na"], MUTED, False)]
            rows.append([
                [(m.get("marco") or L["na"], INK, False)],
                [(m.get("data") or L["na"], INK, False)],
                status_runs,
                [(m.get("obs") or "", INK, False)],
            ])
        add_table(s3, 0.5, 1.3, [3.5, 1.4, 1.6, 2.5], L["h_milestones"], rows, row_h=0.42, name="Milestones")

    # Remove os dois slides modelo e deixa o encerramento por último
    sld_id_lst = prs.slides._sldIdLst
    drop_parts = {blank_a.part, blank_b.part}
    closing_el = None
    for sld_id in list(sld_id_lst):
        part = prs.part.related_part(sld_id.rId)
        if part in drop_parts:
            prs.part.drop_rel(sld_id.rId)
            sld_id_lst.remove(sld_id)
        elif part == closing.part:
            closing_el = sld_id
    sld_id_lst.append(closing_el)

    prs.save(out)
    return n_content + 2


def main():
    global L
    here = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", required=True, help="JSON com os dados do status / status data JSON")
    ap.add_argument("--out", required=True, help="Arquivo .pptx de saída / output .pptx")
    ap.add_argument("--template", default=os.path.join(here, "..", "assets", "template.pptx"))
    ap.add_argument("--lang", choices=sorted(LABELS), default=DEFAULT_LANG,
                    help="Idioma dos rótulos dos slides / slide label language")
    args = ap.parse_args()
    L = LABELS[args.lang]
    for label, path in (("dados / data", args.data), ("template", args.template)):
        if not os.path.isfile(path):
            sys.exit(f"Arquivo não encontrado ({label}): {path} / File not found: {path}")
    try:
        with open(args.data, encoding="utf-8") as fh:
            raw = json.load(fh)
    except json.JSONDecodeError as exc:
        sys.exit(f"JSON inválido em {args.data}, linha {exc.lineno}, coluna {exc.colno}: {exc.msg} / "
                 f"Invalid JSON in {args.data}, line {exc.lineno}, column {exc.colno}: {exc.msg}")
    if not isinstance(raw, dict):
        sys.exit("O JSON precisa ser um objeto com os campos do status. / The JSON must be an object with the status fields.")
    data = normalize(raw)
    total = build(data, args.template, args.out)
    print(f"OK: {args.out} ({total} slides, {len(WARNINGS)} aviso(s)/warning(s))")


if __name__ == "__main__":
    main()
