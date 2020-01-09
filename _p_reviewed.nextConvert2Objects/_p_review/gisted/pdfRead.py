
#pdf open/read
#parse

import PyPDF2 as pdf

def pdfRead(file):
    pdfobj = open(file, 'rb')
    pdfread = pdf.PdfFileReader(pdfobj)

    totpages = pdfread.numPages
    pagelist =[]
    for page in range(0, totpages):
        pageobj = pdfread.getPage(page)
        pagelist = pagelist + [pageobj.extractText()]

    return pagelist

x = pdfRead('/root/Downloads/_toSD/Deep_Learning_with_Python.pdf')
