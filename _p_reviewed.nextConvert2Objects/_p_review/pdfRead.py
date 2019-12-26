
#pdf open/read
#parse

import PyPDF2 as pdf

def pdfRead(file):
    pdfobj=open(file,'rb')
    pdfread = pdf.PdfFileReader(pdfobj)

    totpages = pdfread.numPages
    pagelist =[]
    for page in range(0,totpages):
        pageobj = pdfread.getPage(page)
        pagelist = pagelist + [pageobj.extractText()]

    return pagelist

x = pdfRead('/home/kishore/Documents/How can I enable access to USB devices within VirtualBox guests_ - Unix & Linux Stack Exchange.pdf')
        
