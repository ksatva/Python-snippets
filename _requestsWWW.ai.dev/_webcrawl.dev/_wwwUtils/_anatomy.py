
### --UTILITIES--

import requests
from bs4 import BeautifulSoup as bs
import re
import pandas as pd






###### web extract: anatomy of "request GET url"
class _anatomy():
    def __init__(self,rdata):   # TODO: (self,rdata,LABELS)
        self.rdata = rdata
        self.alldirs =  dir(self.rdata)    #
        #self.allvars =  vars(r)   #dictionary
        self.countdirs = len(self.alldirs)
## -----ANALYSE request object 'r' 
#alldirs =  dir(r)    #list
#allvars =  vars(r)   #dictionary
#. type
#. id
#. 

"""
type()    :type of object
dir()     :set of attributes
id()
getattr()
hasattr()
globals()
locals()
callable()
"""

##use:
#anatomyx = _anatomy(rdata)
#print(anatomyx.countdirs)
#------------------------------_anatomy() --end-