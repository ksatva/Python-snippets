### --UTILITIES--

import requests
from bs4 import BeautifulSoup as bs
import re
import pandas as pd






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
        self.soup = bs(self._data,'html.parser')
        print(':: rdata -> _data -> soup')

##use:
#_wwwx = _www(url)
#--------------------------_www()---end-




