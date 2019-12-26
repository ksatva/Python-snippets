#! /usr/bin/python3
#oa.py
'''
open all files in a folder in default app
'''

from BLOCKS import *

def oa():
    import os
#----user input path-----------   
    path = pathinput()

#---set for exception count-----------
    exception = 0

#----walk and open files------------     
    for folder,subfol, files in os.walk(path):
        for file in files:
            try:
                if folder == path:  #only open file in the parent folder not in subfolders
#----------open file-------------
                    appopen(file)
            except:
                exception += 1

    print(exception)


'''
also:
o.py
pathinput.py block
appopen.py block
'''
