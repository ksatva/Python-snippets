#pyhton2.7
#urlparser.py

from urlparse import urlparse

FIXEDURL = 'http://www.google.com'
URL1 = 'http://netloc/path;param?query=arg#frag'
URL2 = 'http://user:pwd@NetLoc:80/path;param?query=arg#frag'

def urlparser(url):
    parsed = urlparse(url)
    print '----------------------------------------'
    print 'scheme: ', parsed.scheme 
    print 'netloc: ', parsed.netloc
    print 'path: ',parsed.path
    print 'params: ',parsed.params
    print 'query: ',parsed.query
    print 'fragment: ',parsed.fragment
    print 'username: ',parsed.username
    print 'password: ',parsed.password
    print 'hostname',parsed.hostname, '(netloc in lowercase)'
    print 'port: ',parsed.port
    print '\n'





######

up0 = urlparser(FIXEDURL)
up1 = urlparser(URL1)
up2 = urlparser(URL2)
print up1
print up2

