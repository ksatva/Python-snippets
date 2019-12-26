#! python

#download_function.py2
import urllib2

def download(url, user_agent = 'orek', num_retries=2):
   print 'Downloading:',url
	headers = {'User_agent':user_agent}
	request = urllib2.Request(url,headers = headers)
   
	try:
      html = urllib2.urlopen(url).read()
	
   except urllib2.URLError as e:
      print 'Download error:',e.reason
      html = None
		
      if num_retries > 0:
         if hasattr(e,'code') and 500 <= e.code < 600:
            #recursively retry 5xx http errors
            return download(url, num_retries-1)
   return html

#test run
#download('http://httpstat.us/500')
