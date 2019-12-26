from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError 
#flag variable keeps track of program flow
global flag
flag = []
try:
    html = urlopen("http://www.facebook.com")
    flag.append(1)
except HTTPError as e:
    flag.append(0)
try:
    bsObj = BeautifulSoup(html.read(), 'lxml')
    title = bsObj.h1
    flag.append(1)



except AttributeError as e:
    flag.append(0)
#title, flag
#if flag 1 1 : i now have "bsObj"        

with open ("parselogfile.log", 'w') as file:
    file.write(bsObj.prettify())
    file.close()
#print(bsObj.get_text())

title = bsObj.title
head = bsObj.head
body = bsObj.body

A = len(str(bsObj))
b = len(str(title))
c = len(str(head))
d = len(str(body))
