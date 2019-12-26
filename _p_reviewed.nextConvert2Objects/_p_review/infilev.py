#! /usr/bin/python3

'''
    FILE OPERATIONS
'''

#path input
#print('path: ',end=' ')
#path = input()

#WALK TTHE DIRECTORY TREE
def waLkr(path):
    print('walking...')
    folcount=filecount=read=exception=0 #for countdata 
    import os
    booklist = []
    for folder,sub,files in os.walk(path):
        folcount+=1
        for file in files:
            filecount+=1
            try:
                booklist = booklist+[tryopen(path+'/'+file)]
                read+=1
            except:
                exception+=1
            
            #print(path+'/'+file)
    #print(booklist)
    print('total files = %d'%filecount+'\nread = %d'%read+'\nexception = %d'%exception)
    return booklist
            
    

#POINT A FILE


#TRY OPEN
def tryopen(file):
    #for pdf
    import PyPDF2 as pdf
    pdfobj=open(file,'rb')
    print('pdf file open... %s'%file)
    pdfread = pdf.PdfFileReader(pdfobj)

    pageqty = pdfread.numPages #no. of pages in file
    pagelist = []
    for page in range(0,pageqty):
        pageobj = pdfread.getPage(page)
        pagelist = pagelist + [pageobj.extractText()]

    #print(pagelist)
    return pagelist

#EXCEPTION

#PARSE

#RETURN

#execute
path = '/home/kishore/Documents/'
waLkr(path)
