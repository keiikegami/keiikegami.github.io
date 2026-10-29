#!/usr/bin/env python3
"""Build the two-page PDF CV from cv.qmd using ReportLab.

Run with a Python environment containing reportlab and pypdf. The website's
download copies are updated only after the document passes structural checks.
"""

from __future__ import annotations

import argparse
import html
import re
import shutil
from datetime import date
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    HRFlowable, KeepTogether, PageBreak, Paragraph, SimpleDocTemplate,
    Spacer, Table, TableStyle,
)
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
INK = colors.HexColor('#192b3e')
TEXT = colors.HexColor('#22262b')
MUTED = colors.HexColor('#505b66')
RULE = colors.HexColor('#b7c2cc')
FONT_DIR = Path('/System/Library/Fonts/Supplemental')


def register_fonts():
    files = {
        'CV': 'Georgia.ttf', 'CV-Bold': 'Georgia Bold.ttf',
        'CV-Italic': 'Georgia Italic.ttf', 'CV-BoldItalic': 'Georgia Bold Italic.ttf',
        'CV-Sans': 'Arial.ttf', 'CV-SansBold': 'Arial Bold.ttf',
    }
    for name, filename in files.items():
        pdfmetrics.registerFont(TTFont(name, str(FONT_DIR / filename)))
    pdfmetrics.registerFontFamily(
        'CV', normal='CV', bold='CV-Bold', italic='CV-Italic', boldItalic='CV-BoldItalic'
    )
    pdfmetrics.registerFontFamily(
        'CV-Sans', normal='CV-Sans', bold='CV-SansBold',
        italic='CV-Sans', boldItalic='CV-SansBold'
    )


def inline(text):
    text = text.replace('–', '-').replace('—', '-').replace('\u00a0', ' ')
    text = html.escape(text)

    def link(match):
        label, url = match.groups()
        if url.startswith('/'):
            url = 'https://keiikegami.github.io' + url
        return f'<a href="{url}" color="#192b3e">{label}</a>'

    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', link, text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<i>\1</i>', text)
    return text


def read_source():
    source = (ROOT / 'cv.qmd').read_text()
    content = source.split('---', 2)[2]
    sections = {}
    current = None
    for line in content.splitlines():
        if line.startswith('## '):
            current = line[3:]
            sections[current] = []
        elif current:
            sections[current].append(line)
    profile = next(p for p in content.split('\n\n') if p.startswith('Economist ')).strip()
    email = re.search(r'^Email: (.+?)\s*$', content, re.MULTILINE).group(1)
    email = email.replace(' [at] ', '@')
    return sections, profile, email


def bullets(lines):
    items = []
    for line in lines:
        if line.startswith('- '):
            items.append([line[2:].strip()])
        elif line.startswith('  ') and items:
            items[-1].append(line.strip())
    return items


def build(output, updated):
    register_fonts()
    sections, profile, email = read_source()
    styles = {
        'body': ParagraphStyle('body', fontName='CV', fontSize=9.8, leading=13.2,
                               textColor=TEXT, alignment=TA_LEFT, spaceAfter=3),
        'small': ParagraphStyle('small', fontName='CV', fontSize=9.3, leading=12.6,
                                textColor=MUTED, spaceAfter=3),
        'paper': ParagraphStyle('paper', fontName='CV-Bold', fontSize=10.1,
                                leading=13.5, textColor=INK, spaceAfter=2),
        'section': ParagraphStyle('section', fontName='CV-SansBold', fontSize=10.5,
                                  leading=13, textColor=INK, spaceBefore=7,
                                  spaceAfter=5, keepWithNext=True),
        'subsection': ParagraphStyle('subsection', fontName='CV-SansBold', fontSize=9.1,
                                     leading=12.5, textColor=MUTED, spaceBefore=3,
                                     spaceAfter=3, keepWithNext=True),
        'date': ParagraphStyle('date', fontName='CV', fontSize=9.4, leading=13.2,
                               textColor=MUTED, alignment=2),
        'name': ParagraphStyle('name', fontName='CV-SansBold', fontSize=27,
                               leading=31, textColor=INK, spaceAfter=5),
        'contact': ParagraphStyle('contact', fontName='CV-Sans', fontSize=9.6,
                                  leading=13.5, textColor=MUTED, spaceAfter=2),
    }
    # SimpleDocTemplate's frame includes six points of padding on each side.
    width = A4[0] - 98 - 12
    story = []

    def p(text, style='body'):
        return Paragraph(inline(text), styles[style])

    def heading(title):
        story.append(p(title.upper(), 'section'))

    def dated(title):
        heading(title)
        rows = []
        for item in bullets(sections[title]):
            text = item[0]
            match = re.search(r', ((?:April )?\d{4}[^,]*)$', text)
            if not match:
                raise ValueError(f'Date missing from {title}: {text}')
            rows.append([p(text[:match.start()]), p(match.group(1), 'date')])
        table = Table(rows, colWidths=[width-100, 100], hAlign='LEFT')
        table.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('LEFTPADDING', (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (0,-1), 9),
            ('TOPPADDING', (0,0), (-1,-1), 0),
            ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ]))
        story.append(table)

    story.append(p('Kei Ikegami', 'name'))
    story.append(p('Lecturer (tenured), Yokohama City University', 'contact'))
    story.append(Paragraph(
        f'<a href="mailto:{email}">{email}</a>'
        ' &nbsp; | &nbsp; '
        '<a href="https://keiikegami.github.io">keiikegami.github.io</a>',
        styles['contact']))
    story.extend([Spacer(1, 8), HRFlowable(width='100%', thickness=0.8, color=INK), Spacer(1, 9)])
    story.append(p(profile))
    dated('Academic Appointments')
    dated('Education')

    heading('Working Papers')
    for item in bullets(sections['Working Papers']):
        parts = [p(item[0], 'paper')]
        for line in item[1:]:
            parts.append(p(line, 'small' if line.startswith(('with ', 'Accepted ', '*EC ')) else 'body'))
        parts.append(Spacer(1, 1))
        story.append(KeepTogether(parts))

    heading('Publications')
    for authors, title, venue in bullets(sections['Publications']):
        story.append(KeepTogether([
            p(title.rstrip(','), 'paper'),
            p(authors.rstrip(','), 'small'), p(venue, 'small'), Spacer(1, 3),
        ]))

    heading('Work in Progress')
    for item in bullets(sections['Work in Progress']):
        title, *details = item
        if details:
            title += ' (' + '; '.join(detail[0].lower() + detail[1:] for detail in details) + ')'
        story.append(p(title))

    story.append(PageBreak())

    dated('Research and Industry Experience')

    heading('Selected Presentations')
    for line in sections['Selected Presentations']:
        if line.startswith('### '):
            story.append(p(line[4:], 'subsection'))
        elif line.startswith('- '):
            story.append(p(line[2:]))

    heading('Professional Service')
    for item in bullets(sections['Professional Service']):
        story.append(p(' '.join(item)))

    heading('Teaching')
    for line in sections['Teaching']:
        if line.startswith('### '):
            story.append(p(line[4:], 'subsection'))
        elif line.startswith('- '):
            story.append(p(line[2:]))

    heading('Grants')
    for item in bullets(sections['Grants']):
        story.append(KeepTogether([p(item[0]), *[p(line, 'small') for line in item[1:]]]))

    heading('Honors and Fellowships')
    for item in bullets(sections['Honors and Fellowships']):
        story.append(p(' '.join(item)))

    heading('Skills')
    for item in bullets(sections['Skills']):
        story.append(p(' '.join(item)))

    def page_frame(canvas, document):
        canvas.saveState()
        canvas.setStrokeColor(RULE)
        canvas.setLineWidth(0.4)
        canvas.line(49, 39, A4[0]-49, 39)
        canvas.setFont('CV-Sans', 8)
        canvas.setFillColor(MUTED)
        canvas.drawString(49, 26, f'Kei Ikegami  |  Curriculum Vitae  |  {updated:%B %Y}')
        canvas.drawRightString(A4[0]-49, 26, f'{document.page} / 2')
        if document.page > 1:
            canvas.setFont('CV-SansBold', 9)
            canvas.setFillColor(INK)
            canvas.drawString(49, A4[1]-34, 'KEI IKEGAMI')
            canvas.setFont('CV-Sans', 8)
            canvas.setFillColor(MUTED)
            canvas.drawRightString(A4[0]-49, A4[1]-34, 'CURRICULUM VITAE')
        canvas.restoreState()

    output.parent.mkdir(parents=True, exist_ok=True)
    document = SimpleDocTemplate(
        str(output), pagesize=A4, leftMargin=49, rightMargin=49,
        topMargin=48, bottomMargin=52,
        title='Kei Ikegami - Curriculum Vitae', author='Kei Ikegami',
        subject='Empirical industrial organization, econometrics, and market design',
    )
    document.build(story, onFirstPage=page_frame, onLaterPages=page_frame)
    reader = PdfReader(output)
    if len(reader.pages) != 2:
        raise ValueError(f'Expected 2 pages, got {len(reader.pages)}; adjust layout before publishing')
    text = '\n'.join(page.extract_text() for page in reader.pages)
    for required in ['WINE 2026', 'APIOC 2026', 'CUHK', 'PROFESSIONAL SERVICE', 'Reviewer', email]:
        if required not in text:
            raise ValueError(f'Missing required content: {required}')
    for stale in ['expected)', 'ki2047@nyu.edu', 'Placement Director', 'New draft coming soon']:
        if stale in text:
            raise ValueError(f'Obsolete content in PDF: {stale}')
    for target in [ROOT/'files/cv.pdf', ROOT/'docs/files/cv.pdf']:
        if output.resolve() != target.resolve():
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(output, target)
    print(f'Built and checked {output} ({len(reader.pages)} pages). Website copies synchronized.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT/'output/pdf/Kei_Ikegami_CV.pdf')
    parser.add_argument('--updated', type=date.fromisoformat, default=date.today())
    args = parser.parse_args()
    build(args.output, args.updated)
