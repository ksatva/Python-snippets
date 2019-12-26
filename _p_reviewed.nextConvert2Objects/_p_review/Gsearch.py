

def G(searchkey):
	
	#search internet and store results (url) in a list
	#also write in a file
   searchresults = []
   count = 0
   maxcount = 2
   
   from google import search
   for url in search(searchkey, stop = maxcount):
   	#print(url)
		#count +=1
      while True:
         searchresults.append(url)
    		#last line created a data structure[results]; 
    
   return results
'''
def Gwriteinfile(inputlist):
   #next write [results] to a file
   from myFunc import *
   filepath = filepathcreation('Gsearch')
   Gfileobject = open(filepath,'a')
   for key in results:
      write2file(Gfileobject, key)
    #input results to a file done 
   '''

#parse url

#main function
if __name__ == '__main__':
   
	results = G(input('GSearch: '))
   
	print(results)
   
	#--to change when py2 and py3 compatible-------
	



#filter search by receiving website metadata
