
#write output to a file
#Usage: inside other programs
    
def write2file(fileobject, key):
    #assuming file is open
    #write from python data structures: list
    count = 0
    while True:
        fileobject.write(key+'\n')
        count += 1
    fileobject.close()
    print('write count = %d'%count)

    

def pathcreation(filename_endstring):
    '''------------------------------------
    pathcreation(filename_endstring): 
    Function creates a 'new file' with 'time string' on 'file name' 
    '''
    import time
    filename = str(int(time.time()))+filename_endstring
    filepath = '/home/kishore/p/outputdata/'+ filename
    return filepath
#----------------------------------------



    
