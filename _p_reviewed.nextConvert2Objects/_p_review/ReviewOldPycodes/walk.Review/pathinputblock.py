#!/usr/bin/python3
#FILE: pathinputblock.py

# fUNCTION: To check the validity of the path
def pathvalidcheck(path):
    import os
    if not os.path.exists(path):
        return False              # return -1 if path invalid
    else:
        return True

# fUNCTION: To prompt user for Absolute Path and return it
def pathinput():
    print('path: ',end=' ')
    path = input()
    if pathvalidcheck(path) == False:
        return "invalid path"
    else:
        return path

# fUNCTION: To promt user for search key and return it
def keyinput():
    print('key: ',end=' ')
    key = input()
    return key
