## botX --a web crawling bot
#
"""-------------< FEATURES >
EXTRACT WEBPAGE METADATA --todo
REQUEST GET --_www <--[rdata, _data (=>rdata.content)]
MAKE SOUP --_www <--[..., soup]

LOGIN TO A WEBPAGE
EXTRACT TABLES FROM URL --pullurlTables [t2dfs (=>list of dataframes (tables were converted to dataframes))]

REMOVE HTML TAG FROM TEXT --removeHtmlTag [cleantext]
"""
#----------------------------------------------------
from _wwwUtils import _www, _anatomy
import requests


"""metadata tool
http://exadium.com/tools/metadata

.........
Reference-
https://pybit.es/requests-session.html
"""

class loginBot():
    """FOLLOWING DATA NEEDED FOR THIS BOT TO RUN
        payload = {
            'email': 'kishorektarafdar@gmail.com',
            'pass': 'rfvfghjujm'
            }
        POST_LOGIN_URL = "https://www.linkedin.com/login"
        REQUEST_URL = "https://www.linkedin.com/in/kishore-k-tarafdar-95a90a18b/"

        """
    #user input:
    #url = ['login url','after login page url']
    #
    #
    def __init__(self,urls,payload):
        self.postLoginURL = urls[0]
        self.payload = payload
        self.requestURL = urls[1]                     #<from db>

        with requests.Session() as session:
            self.wwwxl= _www(self.postLoginURL)
            post = session.post(self.postLoginURL, data=self.payload)
            self.wwwx = _www(self.requestURL)
            print(self.wwwx.rdata) ## FOR HTTP REQUEST STATUS 
            #login success if 200
           
        

if __name__=='__main__':
    # login form values.
    ##-----< user input >
    payload = {
        'email': 'ksrkrt',
        'pass': 'rfvfghjujm'
        }
    urls = ['https://www.facebook.com/login',
            'https://www.facebook.com/ksrkrt'
            ]
    #-----------------
    loginBotx = loginBot(urls, payload)
    print(loginBotx.wwwx.rdata)
    #print(dir(loginBotx.wwwx.rdata))
    anatomyxl = _anatomy(loginBotx.wwwx.rdata)
    print(anatomyxl.countdirs, ' --objects inside rdata :(GET respone)--loginpage')
    anatomyx = _anatomy(loginBotx.wwwx.rdata)
    print(anatomyx.countdirs, ' --objects inside rdata :(GET respone)')
    #print(anatomyx.countdirs)


"""INSTAGRAM
ACCESS-TOKEN = 
https://api.instagram.com/v1/users/self/?access_token=ACCESS-TOKEN

#for recently liked media
GET /users/self
GET /users/self/media/recent
"""






#make a database of 
#    websites : usernames
#    websites : postLoginUrl
#    websites : requestLoginUrl
#    websites : passwords
#    | website | username | postLoginurl | requestLoginurl | password  |2 tags |       
        



