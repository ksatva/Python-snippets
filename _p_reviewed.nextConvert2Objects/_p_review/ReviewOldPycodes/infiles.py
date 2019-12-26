#! /usr/bin/python3
#infiles.py
#search for a word/string in files

import os ,time
import BLOCKS

def infiles():
   print('...............text files only.....')
   print('search-path : ',end='')
   path = input()
   print('search-key : ',end='')
   key = input()
    
   def outputfile():
        filename = str(int(time.time()))+'infiles'
        filepath = '/home/k/log_register/infiles_records/'+ filename
        return filepath
   filepath = outputfile()
   outputdatafile =open (filepath, 'a')
   outputdatafile.write((path+'\n'+key+'\n'))

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
                        
                        writestring = '\
    ------------------------vvvvvv--\n\
    found in: %s\n\
    %s\n\
    %s\n\
    --\n'%(file,  fileLine,  pathTemp)
                        
                        outputdatafile.write(writestring)
                        break
                        
                fileTemp.close()
            except:
                exception+=1
                #-----------print(exception,end='')
                #print('xxxxxx-exception-xxxxxxxx-%10d-xxxxxxxxx'%exception+'\n'+file+'\n'+path)
        
        				
        #if count == 0:
        #print('no match')
   outputdatafile.close()
   print('FILES SCANS = %d'%fcount)
   print('MATCH in %d files'%count)
   print('EXCEPTION = %d'%exception)

   if count > 0:
        print('visual?',end=' ')
        ans = input()
        if ans != 'n':
            BLOCKS.appopen(filepath)
        #code to open file
        
if __name__ == '__main__':
   infiles() 
   print('...............infiles end...')
