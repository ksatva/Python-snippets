'''
filename = '/home/kishore/read/tempsearchfile.txt'


	
fopen = open(filename, 'r')
		
templine = fopen.readline()
print(templine[:])	

'''
'''
def gsearch(searchfor):
	
    from google import search
    searchresults = []   
    count = 0
    maxcount = 1

    for url in search(searchfor, stop = 1):
        count +=1
        searchresults = searchresults + [url]
    print(searchresults)
    return searchresult
    
gsearch(input('search: '))
'''
#memory=[[],[],[],[],[],[],[],[],[],[]]
memory = []
searchresult = ['https://en.wikipedia.org/wiki/Control_system', 'https://en.wikipedia.org/wiki/Distributed_control_system', 'https://en.wikipedia.org/wiki/Hierarchical_control_system', 'https://en.wikipedia.org/wiki/Networked_control_system', 'https://www.electrical4u.com/control-system-closed-loop-open-loop-control-system/', 'http://www.electronics-tutorials.ws/systems/closed-loop-system.html', 'https://www.facstaff.bucknell.edu/mastascu/eControlHTML/Intro/Intro1.html', 'http://www.businessdictionary.com/definition/control-system.html', 'http://nptel.ac.in/courses/108101037/', 'http://nptel.ac.in/syllabus/108103008/', 'https://www.youtube.com/watch?v=O-OqgFE9SD4', 'http://www.lecsindia.com/', 'https://en.wikibooks.org/wiki/Control_Systems']

import urllib.request
import urllib.parse

print(urllib.request.urlopen(searchresult[0]))
for result in searchresult: 
    memory = memory +[urllib.parse.urlparse(result)]
    
    
print(memory)
    
