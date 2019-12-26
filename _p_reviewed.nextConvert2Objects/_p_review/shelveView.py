#! python3

#shelveView.py
#view the contents of a shelf file

from myFunc import *
from shelve import *

def shelveView(fileName):
    shelfTemp = open(fileName)

    for shelf in list(shelfTemp):
        print(str(shelf)+' :: '+str(shelfTemp[shelf]))
        #print(str(shelf).ljust(7,' ')+' :: '+str(shelfTemp[shelf]))
       
    #shelfTemp.close()
    
    while True:
        print('\nOperate any key(shelf)?')
        reply = input()

        if reply not in shelfTemp:
            break
#---------main operate code to write-----
        print('y')
        
    
    
