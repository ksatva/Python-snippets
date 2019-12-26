#! /usr/bin/python3
#infiles.py
#search for a word/string in files

import os #,time

def infiles():

    print('search-path : ',end='')
    path = input()
    print('search-key : ',end='')
    key = input()
    
    fcount=count=exception=0
    print('\nsearching for "%s"...'%key)
    for f,s,files in os.walk(path):
        
        for file in files:	
            pathTemp = (f+'/'+file)
            #print(pathTemp)	#
            #count+=1
            #path = f+'/'+str(file[count])
            #print(path)
            try:
                fileTemp = open(pathTemp)
                fcount+=1
                #print(fileTemp)
                for line in fileTemp:
                    fileLine = fileTemp.readline()
                    #print(fileLine) 					
                    if key in fileLine:
                        count+=1
                        #print('-----------------------------------------------------')
                        #print('found in: %s'%file)
                        #print(fileLine)
                        #print(pathTemp)
                        #print('=====================================================')	
                        break
                        
                fileTemp.close()
            except:
                exception+=1
                #-----------print(exception,end='')
                #print('xxxxxx-exception-xxxxxxxx-%10d-xxxxxxxxx'%exception+'\n'+file+'\n'+path)
        
        				
        #if count == 0:
        #print('no match')
    print('FILES SCANS = %d'%fcount)
    print('MATCH in %d files'%count)
    print('EXCEPTION = %d'%exception)

    if count > 0:
        print('visualize?',end=' ')
        ans = input()
        if ans == 'y':
            infilesviz(path,key)

        
def infilesviz(path,key):
    fcount=count=exception=0
    
    for f,s,files in os.walk(path):

        for file in files:	
            fcount+=1
            pathTemp = (f+'/'+file)
            #print(pathTemp)	#
            #path = f+'/'+str(file[count])
            #print(path)
            try:
                fileTemp = open(pathTemp)
                #print(fileTemp)
                for line in fileTemp:
                    fileLine = fileTemp.readline()
                    #print(fileLine) 					
                    if key in fileLine:
                        count+=1
                        print('vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv%dvvvvvvvvvvvv'%count)
                        print('found in: %s'%file)
                        print(fileLine)
                        print(pathTemp)
                        print('======================================exception=%d=============='%exception)
                        
                        
                fileTemp.close()
            except:
                exception+=1
                #-----------print(exception,end='')
                #print('xxxxxx-exception-xxxxxxxx-%10d-xxxxxxxxx'%exception+'\n'+file+'\n'+path)
        
		
        #if count == 0:
        #print('no match')
    #print('FILES SCANS = %d'%fcount)
    print('occurences = %d'%count)
    print('EXCEPTION = %d'%exception)



def dotprint(dots):
    print(dots,end='')

def dotdel(dots):
    print('\b'*len(dots),end='',flush =True)


#-------------------------------------------------------

#searchinfiles('/home/kishore/.*','indicator-netspeed')

#-----------------------------------------------------
