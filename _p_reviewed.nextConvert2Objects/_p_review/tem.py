def tryopen(filepath):
    #for pdf
    import PyPDF2 as pdf
    
    pdfobj=open(filepath,'rb')
    print('pdf file open...')
    pdfread = pdf.PdfFileReader(pdfobj)

    pageqty = pdfread.numPages #no. of pages in file
    pagelist = []
    for page in range(0,pageqty):
        pageobj = pdfread.getPage(page)
        pagelist = pagelist + [pageobj.extractText()]
        
    print(pagelist)
    return pagelist

tryopen('/home/kishore/Documents/tkinter.pdf')
