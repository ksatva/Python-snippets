## extract proxies 
"""Nomenclature

url rdata _data soup
_wwwx :full url content with soup
"""

import requests
from bs4 import BeautifulSoup as bs
import re
import pandas as pd

#from _wwwutils import removeHtmlTag, _www, _pullurlTables

### --UTILITIES--
###### removing html tags with 'regex'-----
class removeHtmlTag():
	#import re
	
    def __init__(self,text):
        self.text = text
        self.TAG_RE = re.compile(r'<[^>]+>')
        self.cleantext = self.TAG_RE.sub('',text)

##
#hx = removeHtmlTag("<td>184.191.162.4</td>")
#hx.cleantext
#----------------------------------------






###### GET WEB CONTENT TO 'SOUP'------
class _www():
	#import requests
	#from bs4 import BeautifulSoup as bs
	def __init__(self,urlx):
		#self.agent = agentx    # DI: name of agent
		self.url = urlx        # DI: name of url
		#self.proxies = proxies # DI: proxies

		#self.headers = {'User-Agent': agentx}
		self.rdata = requests.get(urlx) #,headers=self.headers,proxies=self.proxies)
		self._data = self.rdata.content
		self.soup = bs(self._data)

##
#_wwwx = _www(url)
#-------------------------------






###### HTML/WEB 'TABLE' TO PANDAS DATAFRAME------
class pullurlTables():
    #import pandas as pd
    #from bs4 import BeautifulSoup as bs
    def __init__(self,_wwwx):
        self.wwwx = _wwwx
        self.soup = _wwwx.soup
        
        self.tables = list()
        for table in self.soup.findAll("table"):
            self.tables.append(table)
        
        self.t2dfs = list()
        
        for ix in range (0,len(self.tables)):
            tttx = self.soup.find_all('table')[ix]
            records=[]
            
            for row in tttx.findAll("tr"):
                #print(row)
                cells = row.findAll("td")
                #if len(cells) > 0:
                record = []
                #for cell in cells:
                print(cells)
                print('-----------------')
                for cell in cells:
                    ##!#print(type(cell))import requests
                    ##!#print("yyyyyyy")
                    hx = removeHtmlTag(str(cell))             # *calling o-in-o  
                    print(hx.cleantext)
                    record.append(hx.cleantext)
                records.append(record)
            
            df = pd.DataFrame(data=records)
            df 
            self.t2dfs.append(df)


##
#tttx = pullurlTables(_wwwx)
#tttx.t2dfs
#-----------------------------------------------
         

if __name__ == '__main__':
    url = 'https://free-proxy-list.net/'
    _wwwx = _www(url)
    tttx = pullurlTables(_wwwx)
    
    #CONTAINTER: list OF DATAFRAMES <TABLES
    t2dfs = tttx.t2dfs    


    




""" 
### METHOD 1 : !!!!!!!!!!!
#proxySite url
url = 'https://free-proxy-list.net/'
rdata = requests.get(url) #,headers=headers,proxies=self.proxies)
#print(rdata.json())
_data = rdata.content
soup = bs(_data)



##looking cells in the 'soup'
cells=list()
#for all table (article +other)
for cell in soup.findAll("td"):
	#if 'href' in link.attrs:
		#print(link.attrs['href'])
    cells.append(cell)

#find table
print(cells)


##extracting all IPs from url
for cell in cells:
    _cellLength = len(str(cell))
    _dots = str(cell).count('.')
    if _dots == 3 and _cellLength in range (19, 25): ##'3dots' signature for locating ip 
        print(cell)



##find associated ports
##find update 
     
"""




#####        
##### METHOD 2 : get the 'table' first ---> 

"""CODE APPENDED IN 'OBJECT'
tables=list()  ##no need since directly looking in 'cells'
#for all table (article +other)
for table in soup.findAll("table"):
	#if 'href' in link.attrs:
		#print(link.attrs['href'])
    tables.append(table)

print(tables)       
"""



""" 
###
#####pandas
import pandas as pd

ttt = soup.findAll('table')[0]
newTable = pd.DataFrame(columns=range(0,2), index = [0])

records = []
for row in ttt.findAll("tr"):
    #print(row)
    cells = row.findAll("td")
    #if len(cells) > 0:
    record = []
    #for cell in cells:
    print(cells)
    print('xxxxxxxxxxxxxxx')
    for cell in cells:
        print(type(cell))
        print("yyyyyyy")
    
    
    #for cell in cells:
     #   newTable.iat[]
 
df = pd.DataFrame(data=records)
df 

"""


"""
###Remove html tags from raw_text
import re

TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    return TAG_RE.sub('', text)

remove_tags("<td>184.191.162.4</td>")

"""


"""--OBJECT CREATED
#####
tttx = soup.find_all('table')[0]
#newTable = pd.DataFrame(columns=range(0,2), index = [0]) #!!!!!!!!!!!!! CHANGE SIZE

records = []
for row in tttx.findAll("tr"):
    #print(row)
    cells = row.findAll("td")
    #if len(cells) > 0:
    record = []
    #for cell in cells:
    print(cells)
    print('xxxxxxxxxxxxxxx')
    for cell in cells:
        #!#print(type(cell))
        #!#print("yyyyyyy")
        hx = removeHtmlTag(str(cell))
        
        print(hx.cleantext)
        record.append(hx.cleantext)
    records.append(record)

df = pd.DataFrame(data=records)
df 
"""