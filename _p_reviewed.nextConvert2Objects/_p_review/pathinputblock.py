#! /usr/bin/pyhton3
#pathinputblock.py
#mother path.py


#____________discard+++++++++++updated to path_Functions.py

from pathvaliditycheckblock import *

def pathinput():
    print('path: ',end=' ')
    path = input()
    if pathvalidcheck(path) == False:
        return "invalid path"
    else:
        return path

def keyinput():
    print('key: ',end=' ')
    key = input()
    return key
