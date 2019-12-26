#! python3

#fdict.py
#store dictinput in a file  

from myFunc import *
from shelve import *
call = 0
def fdict():
    #function call counter
    global call
    call += 1 

    shelfFile = open('myData')
    fdictTemp = dictInput()
    shelfFile['tempDict'] = fdictTemp
    shelfFile.close()
