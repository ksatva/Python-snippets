### --UTILITIES--

import requests
from bs4 import BeautifulSoup as bs
import re
import pandas as pd






###### web extract: HTML/WEB 'TABLE' TO PANDAS DATAFRAME------
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

##use:
#tttx = pullurlTables(_wwwx)
#tttx.t2dfs
#------------------------------pullurlTables() --end-
