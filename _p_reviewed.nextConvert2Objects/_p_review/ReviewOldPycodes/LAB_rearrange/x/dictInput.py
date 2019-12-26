#! python3

#dictInput.py
#Dictionary input
#For creating dictionary
#EASY USER INPUT

#dictionary value only 'str' type


def dictInput():
    print('Dictionary creation'.center(40,'='))
    dictTemp = {}
    #print('Input for Dictionary Name: ')
    #dictName = input()
    
        

    #print('Dictionary:: '+dictName+' created')
# set name of dictionary

    while True:
        print('\n\tEnter key: ',end=' ' )
        dictKey = input()
        if dictKey == '':
            break
        if dictKey in dictTemp:
            print('key exists:: '+dictKey+' : '+dictTemp[dictKey])
        else:
            print('\tEnter value: ',end=' ')
            dictValue = input()
            dictTemp[dictKey] = dictValue
            print('--value added successfully.')

    print('Dictionary created successfully'.center(50,'='))
    return dictTemp
