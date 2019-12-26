#! python3

#flist.py
#store listinput in a file  

from myFunc import *
from shelve import *
call = 0
def flist():
    #function call counter
    global call
    call += 1 

    shelfFile = open('myData')
    flistTemp = listInput()
    shelfFile['tempList'] = flistTemp
    shelfFile.close()

#print(call)
