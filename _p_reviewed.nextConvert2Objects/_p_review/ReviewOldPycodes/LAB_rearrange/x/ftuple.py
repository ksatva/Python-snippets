#! python3

#ftuple.py
#store tuple Input in a file  

from myFunc import *
from shelve import *
call = 0
def ftuple():
    #function call counter
    global call
    call += 1 

    shelfFile = open('myData')
    ftupleTemp = tupleInput()
    shelfFile['tempTuple'] = ftupleTemp
    shelfFile.close()
