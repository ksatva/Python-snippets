#! /usr/bin/python3
#infile.py
#search for a word/string in a file

#return count
def infile():
    
    print('file-path : ',end='')
    path = input()
        
    count = 0
    try:
        fileTemp = open(path)
        print('search-key : ',end='')
        key = input()   
        
        print('searching...')
        for line in fileTemp:
            fileLine = fileTemp.readline()
            if key in fileLine:
                count += 1

        fileTemp.close()
                
        if count == 0:
            print('\nMATCH:',end = ' ')
            return count

        print('\nMATCH: %d'%count)
        print('visual?',end=' ')
        ans = input()
        if ans == 'y':
            printMatch(path,key)
        return count
            
    except:
        print('!!exception!!')

def printMatch(path,key):
    
    fileTemp = open(path)
        
    for line in fileTemp:
        fileLine = fileTemp.readline()
        #print(fileLine)
        if key in fileLine:
            print('-----------------------------------------------------')
            print(fileLine)
            print('=====================================================')	

    fileTemp.close() 
    import os
    print(os.path.abspath(path))
        
