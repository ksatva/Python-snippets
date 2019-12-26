#!

#contolsysdatasearch.py

memory = []

#>----google search--------
def gsearch(searchfor):
	
   from google import search
	searchresults = []   
	count = 0
   maxcount = 1
   
   for url in search(searchfor, stop = 1):
      print(url)
      print(type(url))
      count +=1
      searchresults = searchresults + [url]
   #return url
      fopen = open('/home/kishore/read/tempsearchfile.txt', 'a')
      fopen.write(url+'\n')
      fopen.close()
#------------


filename = '/home/kishore/read/tempsearchfile.txt'

def readfromfile(filename):
	fopen = open(filename, 'r')
	return fopen.readline()


#--------->url info parse--------
def urlinfoparse(searchfor):
	
	#url type
	fopen = open(filename, 'r')
	
	while True:#infinite loop condition
		tempurl = fopen.readline()
		#open link
		#parse header
		#see if suitable









	#accept or reject
	#filter ads
	#filter pictures
	#filter text

	#return parsedata
#----------

#>----------Display result in browser----------
#######def displayresult(localurl):
	#import html format 
	#make template
	#open template
	#push results to template
		
	
if __name__=='__main__':
   
   gsearch(input('search: '))
   
   tempurl = readfromfile(filename)
   urlinfoparse(tempurl)
