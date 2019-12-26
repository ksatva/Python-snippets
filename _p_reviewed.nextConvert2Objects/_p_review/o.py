#! /usr/bin/python3
#o.py
'''
searches and open a file in default app
setpath = /home/kishore/
'''

from BLOCKS import *
#input

def o():
#setpath-----------------
    path = '/home/kishore/'

#filename as key---------------------
    key = keyinput()

#search---------------
    for folder,subfol, files in os.walk(path):
        for file in files:
            if file == key:
                print('found: '+str(file))
#open in default app
                appopen(file)
            




