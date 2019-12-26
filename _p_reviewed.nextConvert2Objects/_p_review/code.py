pathin = "/run/user/1001/gvfs"
from ABC import *


def walkwork(path):

    import os
    
        
    folcount = filecount = 0
    for folder, subfolder, files in os.walk(path):
        #folcount+=1
        if 'Phone/Documents/docsync' in folder:
            print('located...')
            path = folder
            
            for file in folder:
                if 
            #print(folder)
            break
           # return folder
        #write work
                
        #for file in files:
         #   filecount+=1
            #write work
            
    print('count data returns...')        
    return {'PATH' : path, 'FOLDERS' : folcount, 'FILES' : filecount}


os.listdir(pathin)


    

