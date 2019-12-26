

def G(searchkey):
	 #search internet and store results (url) in a list
	 #also write in a file

    results = []
    count = 0
    maxcount = 10

    from google import search
    for url in search(searchkey,stop =  maxcount):
        print(url)
        
#main function
if __name__ == '__main__':
   
   G(input('GSearch: '))
   
 


#filter search by receiving website metadata
