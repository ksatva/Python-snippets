#! /usr/bin/python3

from BLOCKS import *
from myFunc import *

def walk1():
    walktype = ['.', 's', 'a', 'v', 'f', 'work']
    print('. search(s) exact(a) viz(v) ftype(f) work \nkey:',end=' ')
    key = input()
    while True:
        if key not in walktype:
            print('!keyerror!')
            print('key:',end=' ')
            key = input()
            break
       
        if key == '.':
            walkonly(pathinput())
            break
        if key == 'v':
            walkviz(pathinput())
            break
        if key == 's':
            walksearch(pathinput(),keyinput())
            break
        if key == 'a':
            walkexact(pathinput(),keyinput())
            break
        if key == 'f':
            walkdot(pathinput(),keyinput())
            break
        if key == 'work':
            walkwork()
            break
    
