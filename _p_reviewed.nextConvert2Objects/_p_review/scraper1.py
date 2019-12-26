from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsobj = BeautifulSoup(html.read())
        #title = bsobj.body.h1
        title = bsobj.findAll('table')[4].findAll('tr')[2].find('td').findAll('div')[1].find('a')
    except AttributeError as e:
        return None
    return title

title = getTitle("http://www.pythonscraping.com/exercises/exercise1.html")
if title == None:
    print('Title not found!')
else:
    print(title)
