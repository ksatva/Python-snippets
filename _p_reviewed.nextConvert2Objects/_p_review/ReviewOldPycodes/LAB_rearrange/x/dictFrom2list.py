#! python3
#dictfrom2list.py

#Program INPUT: 2 NOS. OF list :: OUTPUT: 1 dictionary

from myFunc import *

def dictFrom2list(keyList, valueList):
    #print('Dictionary creation from 2 lists'.center(50,'='))
    dictTemp = {}
    i = -1
    if len(keyList) != len(valueList):
        return '\n ---x x x Size mismatch'
    for key in keyList:
        i+=1
        dictTemp[key] = valueList[i]

    print('Success:: Dictionary created from 2 lists'.center(50,'='))
    return dictTemp
        
