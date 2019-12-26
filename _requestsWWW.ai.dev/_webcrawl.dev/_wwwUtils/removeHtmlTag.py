### --UTILITIES--

import requests
from bs4 import BeautifulSoup as bs
import re
import pandas as pd



###### removing html tags with 'regex'-----
class removeHtmlTag():
	#import re
	
    def __init__(self,text):
        self.text = text
        self.TAG_RE = re.compile(r'<[^>]+>')
        self.cleantext = self.TAG_RE.sub('',text)

##use:
#hx = removeHtmlTag("<td>184.191.162.4</td>")
#hx.cleantext
#-------------------------removeHtmlTag()---end-




