#! python3
#dict4m2list.py
#make dictionary from 2 list

from myFunc import *

def dictMap2list(keyList, valueList):
    dictTemp = {}
    i = -1
    if len(keyList) != len(valueList):
        return '\n ---x x x Size mismatch'
    for key in keyList:
        i+=1
        dictTemp[key] = valueList[i]

    return dictTemp
        
