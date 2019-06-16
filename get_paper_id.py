import re

import pdfx
from pdfminer import pdfparser, pdfdocument, pdftypes, converter

doi_pattern = re.compile("\\b(10[.][0-9]{4,}(?:[.][0-9]+)*/(?:(?![\"&\'<>])\S)+)\\b")

vixra_regex = r"""\[\s?([^\s,]+):viXra"""


def get_doi(instr):
    """
    返回DOI
    :param instr: MetaData（大部分期刊均有）
    :return: doi，形如 '10.1371/journal.pcbi.1004697'
    """
    match = doi_pattern.search(instr)
    if match:
        return match.group()
    else:
        return


def get_identifier(pdf_path):
    """
    返回文献标示符
    :param pdf_path: pdf地址
    :return: 标示类型和值，例如'{'arXiv': '1805.03977'}, {'doi': '10.1016/j.rser.2016.06.056'}, {'None': ''}'
    """
    identifier = {}
    stream = open(pdf_path, 'rb')
    print(type(stream))
    pdf_stream = pdfparser.PDFParser(stream)
    doc = pdfdocument.PDFDocument(pdf_stream, caching=True)
    if 'Metadata' in dict(doc.catalog).keys():
        metadata = pdftypes.resolve1(doc.catalog['Metadata']).get_data().decode()
        if get_doi(metadata):
            identifier['doi'] = get_doi(metadata)
            return identifier
        else:
            identifier['None'] = ""
            return identifier
    else:
        pdf_x = pdfx.PDFx(stream)
        line = pdf_x.get_text()
        line = line.replace(' ', '')
        line = line.replace('\n', '')

        res = re.findall(vixra_regex, line, re.IGNORECASE)
        if res:
            arxiv_id = list(set([r.strip(".") for r in res]))[0][::-1]
            arxiv_id = re.sub(r'v([0-9])', '', arxiv_id)
            identifier['arXiv'] = arxiv_id
            return identifier
        else:
            identifier['None'] = ""
            return identifier


pdf_list = [r'1805.03977.pdf', r'osdi16-abadi.pdf', r'1905.06316.pdf', r'2016 Isaure Chauvot de Beauchene.pdf',
            r'1-s2.0-S136403211630288X-main.pdf']

for i in pdf_list:
    print(get_identifier(i))
