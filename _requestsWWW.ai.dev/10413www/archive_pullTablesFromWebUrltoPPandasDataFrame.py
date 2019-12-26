## PULL TABLES FROM WEB PAGES --> PANDAS DATAFRAME 

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
    
    #url = 'https://free-proxy-list.net/'
    url = 'https://www.facebook.com/'
    
    _wwwx = _www(url)
    tttx = pullurlTables(_wwwx)
    
    #CONTAINTER: list OF DATAFRAMES <TABLES
    t2dfs = tttx.t2dfs
    #len(t2dfs)
    #t2dfs[0]    





#### @k