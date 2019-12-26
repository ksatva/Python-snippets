#codetest.py
import sys
sys.path.append('/home/kishore/p/webscrap/')

from webscrapfunc import *

url0='http://example.webscraping.com'
x = 'example.webscraping.com/(index|view)/'
#link_crawler(url,x)

uurl =raw_input('url: ')
uuurl = 'http://www.'+str(uurl)

y = download(uuurl)
print y
