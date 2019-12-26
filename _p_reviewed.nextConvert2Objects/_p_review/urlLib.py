#
#----------------URL METADATA -----------------------
#class url(object)

import urllib.request

'''
urllib.request
    urllib.request.urlopen(url...)
        geturl()
        info()
        getcode()
'''

urlPath='http://www.google.com'

def urlfile():
#writes user input urlPath in urlfile.txt............. file filecreation
    while True:
        print('urlPath: ',end=' ')
        urlPath = input()#'http://www.google.com'
        if urlPath =='':
            break
        #append infile
        fileobject = open('/home/kishore/p/urlfile.txt', 'a+')
        fileobject.write("http://www.%s\n"%urlPath)
        fileobject.close()    
    return urlPath
    #RETURN urlPath string (last entry)

def makecapsule(urlPath):
#url capsule from single url----------metadata in url
    x=[]
    x = x + [urllib.request.urlopen(urlPath)]
    xhead = x[0]
    x = x + [xhead.geturl(), xhead.info(), xhead.getcode()]
    return x
    #RETURN A LIST [x]

def readurlfile(file):
    
    urls = []
    fileobject = open(file,'r')
    data = fileobject.read()
    data = data.split()
    for element in data:
        if 'http' in element and '#' not in element:
            urls = urls + [element]
    fileobject.close()
    return urls
    #RETURN [...]

#............................................... DATA PROCESSING................            
#------------------makedata(...)
def makedata(urlist):
    data = []
    for url in urlist:
        data = data + makecapsule(url)
    datalist = data
    return datalist


#DISPLAY
'''................................................CAPSULE DISPLAY.......................
#..........................typedatadisplay
def fn1(capsule):
    count = 0
    for element in capsule:
        if count == 0:
            print(type(element))
            count+=1
        else:
            print('\t'+str(type(element)))

#..........................datadisplay
def fn2(capsule):
    count = 0
    for element in capsule:
        if count == 0:
            print(element)
            count+=1
        else:
            print('\t'+str(element))
'''
'''x[0]= urllib.request.urlopen(urlPath)
x[1] = x.geturl()
x[2] = x.info()
x[3] = x.getcode()
'''
'''
x = urllib.request.urlopen(urlPath)
print(type(x))
print(type(x.geturl()))
''''''typx.info()
x[3] = x.getcode()

print(x[0])
for i in range(1,4):
    print('\t',end = ' ')
    print(x[i])
'''
#-------datadisplay-----------fn3
def printdatafn3(datalist):
    #print(datalist)
    count = 0
    for listin in datalist:
        count +=1
        print('----------------------------------------------------------------------%d------'%count)
        print(listin)
        


##########################PROGRAM
printdatafn3(makedata(readurlfile('/home/kishore/p/urlfile.txt')))



###########################

