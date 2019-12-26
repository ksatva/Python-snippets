def gsearch(searchfor):
	
    from google import search
    searchresults = []   
    count = 0
    maxcount = 1

    for url in search(searchfor, stop = 1):
        count +=1
        searchresults = searchresults + [url]
    print(searchresults)
    return searchresults

#test:
gsearch(input('search: '))
