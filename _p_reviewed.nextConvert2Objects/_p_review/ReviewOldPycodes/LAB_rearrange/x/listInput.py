#! Python3

#listInput.py
#for list creation
#EASY USER INPUT

#list values only 'int' or 'str' Type  

def listInput():
    print('List creation'.center(40,'='))
    tempList = []

    while True:
        print('\tEnter value: ',end=' ')
        listValue = input()
        if listValue == '':
            break
        try:
            tempList = tempList + [int(listValue)]
        except:
            tempList = tempList + [listValue]
     
    print('List created successfully'.center(40,'='))
    return tempList    
