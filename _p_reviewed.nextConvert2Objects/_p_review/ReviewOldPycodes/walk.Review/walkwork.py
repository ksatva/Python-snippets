
#FUNCTION
#FOR MODIFICATION IN NEED

#-------work defined in files'----------
def walkwork(path,work):

    import os
    
    folcount = filecount = 0
    for folder, subfolder, files in os.walk(path):
        folcount+=1
        #write work
                
        for file in files:
            filecount+=1
            #write work
            work


    print('count data returns...')        
    return {'PATH' : path, 'FOLDERS' : folcount, 'FILES' : filecount}

