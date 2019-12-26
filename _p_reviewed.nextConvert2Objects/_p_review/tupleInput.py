#! Python3

#tupleInput.py
#for tuple creation
#EASY USER INPUT

#list values only 'int' or 'str' Type  

def tupleInput():
    print('Tuple creation'.center(40,'='))
    tempTuple = ()

    while True:
        print('\tEnter value: ',end=' ')
        tupleValue = input()
        if tupleValue == '':
            break
        tempList = list(tempTuple)
        try:            
            tempList = tempList + [int(tupleValue)]
        except:
            tempList = tempList + [tupleValue]
        tempTuple = tuple(tempList)
    print('Tuple created successfully'.center(40,'='))    
    return tempTuple    
