import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=70, bottom=70, left=100, right=100):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'''
        <w:tcMar {nsdecls("w")}>
            <w:top w:w="{top}" w:type="dxa"/>
            <w:bottom w:w="{bottom}" w:type="dxa"/>
            <w:left w:w="{left}" w:type="dxa"/>
            <w:right w:w="{right}" w:type="dxa"/>
        </w:tcMar>
    ''')
    tcPr.append(tcMar)

def set_cell_borders(cell, top="CCCCCC", bottom="CCCCCC", left=None, right=None):
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = parse_xml(f'''
        <w:tcBorders {nsdecls("w")}>
            <w:top w:val="{"single" if top else "none"}" w:sz="4" w:space="0" w:color="{top if top else "auto"}"/>
            <w:left w:val="{"single" if left else "none"}" w:sz="4" w:space="0" w:color="{left if left else "auto"}"/>
            <w:bottom w:val="{"single" if bottom else "none"}" w:sz="4" w:space="0" w:color="{bottom if bottom else "auto"}"/>
            <w:right w:val="{"single" if right else "none"}" w:sz="4" w:space="0" w:color="{right if right else "auto"}"/>
        </w:tcBorders>
    ''')
    tcPr.append(tcBorders)

def format_custom_table(table, col_widths, hdr_bg="1E3A8A", zebra_bg="F8FAFC"):
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for r_idx, row in enumerate(table.rows):
        is_hdr = (r_idx == 0)
        is_zebra = (r_idx % 2 == 1 and not is_hdr)
        bg = hdr_bg if is_hdr else (zebra_bg if is_zebra else "FFFFFF")
        
        trPr = row._tr.get_or_add_trPr()
        trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
        if is_hdr:
            trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
            
        for c_idx, cell in enumerate(row.cells):
            cell.width = col_widths[c_idx] if c_idx < len(col_widths) else Inches(1.0)
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=60, bottom=60, left=90, right=90)
            top_bdr = "1E3A8A" if is_hdr else ("CCCCCC" if is_zebra else "E2E8F0")
            bot_bdr = "1E3A8A" if is_hdr else "CBD5E1"
            set_cell_borders(cell, top=top_bdr, bottom=bot_bdr)
            
            for p in cell.paragraphs:
                p.paragraph_format.line_spacing = 1.05
                p.paragraph_format.space_before = Pt(1)
                p.paragraph_format.space_after = Pt(1)
                for run in p.runs:
                    run.font.name = 'Times New Roman'
                    if is_hdr:
                        run.font.size = Pt(8.0)
                        run.font.bold = True
                        run.font.color.rgb = RGBColor(255, 255, 255)
                    else:
                        run.font.size = Pt(7.8)
                        run.font.color.rgb = RGBColor(15, 23, 42)

def populate_table_data(doc, table_data, col_widths, hdr_bg="1E3A8A"):
    t = doc.add_table(rows=len(table_data), cols=len(table_data[0]))
    for r_idx, row in enumerate(table_data):
        for c_idx, val in enumerate(row):
            cell = t.cell(r_idx, c_idx)
            cell.text = str(val)
    format_custom_table(t, col_widths, hdr_bg=hdr_bg)
    return t

print("Loaded table generator module.")
