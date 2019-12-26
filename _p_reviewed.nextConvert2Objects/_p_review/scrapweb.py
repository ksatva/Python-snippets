

from urllib.request import urlopen

html = urlopen("http://pythonscraping.com/pages/page1.html")
#print(html.read())

from bs4 import BeautifulSoup

bsobj=BeautifulSoup(html.read(),"lxml");
print(bsobj.h1)
