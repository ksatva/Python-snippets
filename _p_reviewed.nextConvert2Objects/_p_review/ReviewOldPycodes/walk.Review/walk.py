#!/usr/bin/python3
#FILENAME: walk.py
#Objective: To search files and folders in a local system

import os
from pathinputblock import *
from walkblock import *

def walk():
    print('\n[START]~~~~~~~~~~~~~~~~~walking local system only~~~')
 
    count=0
    while True:
        count+=1
        path = input('search-path: ')
        if not os.path.exists(path):
            input('!!! Invalid path !!!')
            if count == 3:
                return print('[Max attemts over]')
        else:
            break      		   
            
    searchkey = input('search-key: ')
    walktype = ['s', '.', 'x', 'c', 'l', 'work']
	
    wkey = input('\nChoose walktype: \nsearch(s) exactMatch(.) fileType(x) countOnly(c) list(l) work\nwalktype? ')
    
    count=0
    while True:
        if wkey not in walktype:
            count+=1
            wkey = input('!!!warning: keyerror!!!\n walktype? ')
            if count==5:
                return print('[Max attemts over]')
        
        else:
            print('walk-search...')
            if wkey == 'c':
                walk2count(path)
                break
            if wkey == 'l':
                walk2list(path)
                break
            if wkey == 's':
                walksearch(path,searchkey)
                break
            if wkey == '.':
                walkexact(path,searchkey)
                break
            if wkey == 'x':
                walk4fext(path,searchkey)
                break
         #~~~~~~   
            if wkey == 'work':
                appopen('/home/kishore/LearnPY/walkwork.py')
                walkwork(path,searchkey)
                break
    
if __name__ == '__main__':
	walk()
	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~walk~~~[end]')
