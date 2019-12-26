#! /usr/bin/env python3

from BLOCKS import *
from ABC import *
from walkwork import *

def walk():
    print('...............local system only....')
    path = pathinput()
    searchkey = keyinput()
    walktype = ['.', 's', 'a', 'v', 'f', 'work']

    #print('. search(s) exact(a) viz(v) ftype(f) work \nkey:',end=' ')
    key = input('. search(s) exact(a) viz(v) ftype(f) work \nkey:')

    while True:
        if key not in walktype:
            print('!keyerror!')
            #print('key:'end=' ')
            key = input('key:')
            break
        
        else:
            print('walk-search...')
            if key == '.':
                walkonly(path)
                break
            if key == 'v':
                walkviz(path)
                break
            if key == 's':
                walksearch(path,searchkey)
                break
            if key == 'a':
                walkexact(path,searchkey)
                break
            if key == 'f':
                walkdot(path,searchkey)
                break
            if key == 'work':
                appopen('/home/kishore/LearnPY/walkwork.py')
                walkwork(path,searchkey)
                break
    
if __name__ == '__main__':
	walk()
	print('.................walk end..')
