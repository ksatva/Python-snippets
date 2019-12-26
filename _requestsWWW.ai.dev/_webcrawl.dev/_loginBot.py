##THIS IS A LOGIN BOT- TO LOG IN TO WEB PAGES

"""metadata tool
http://exadium.com/tools/metadata

.........
Reference-
https://pybit.es/requests-session.html
"""

from _wwwUtils import _www

#url = 'https://www.facebook.com/login/'
#_wwwx = _www(url)

import requests

# Fill in your details here to be posted to the login form.
payload = {
    'email': 'ksrkrt',
    'pass': 'rfvfghjujm'
}

"""
payload = {
    'email': 'kishorektarafdar@gmail.com',
    'pass': 'rfvfghjujm'
}
POST_LOGIN_URL = "https://www.linkedin.com/login"
REQUEST_URL = "https://www.linkedin.com/in/kishore-k-tarafdar-95a90a18b/"

"""
#This URL will be the URL that your login form points to with the "action" tag.
POST_LOGIN_URL = "https://www.facebook.com/login"

#This URL is the page you actually want to pull down with requests.
REQUEST_URL ='https://www.facebook.com/ksrkrt'
urls = [POST_LOGIN_URL, REQUEST_URL]



#---< main >
with requests.Session() as session:
    post = session.post(POST_LOGIN_URL, data=payload)
    _wwwx = _www(REQUEST_URL)
    print(_wwwx.rdata) ## FOR HTTP REQUEST STATUS
    
    #r = session.get(REQUEST_URL)
    #print(r.text)   #or whatever else you want to do with the request data!




##MK1 :dev
####creating object
class wxxx():
    def __init__(self,urls,payload):
        self.postLoginUrl = urls[0]
        self.payload = payload
        self.requestUrl = urls[1]                     #<from db>
        

#make a database of 
#    websites : usernames
#    websites : postLoginUrl
#    websites : requestLoginUrl
#    websites : passwords
#    | website | username | postLoginurl | requestLoginurl | password  |2 tags |       
        



