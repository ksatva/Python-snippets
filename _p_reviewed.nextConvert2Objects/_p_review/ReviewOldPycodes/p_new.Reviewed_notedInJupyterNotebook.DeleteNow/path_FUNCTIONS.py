
#LAYER 0 FILE
#FUNCTIONS:

def pathvalidcheck(path):
    import os
    if not os.path.exists(path):
        return False    #return -1 if path invalid
    else:
        return True
        
#------------------------------        
def pathinput():
    print('path: ',end=' ')
    path = input()
    if pathvalidcheck(path) == False:
        return "invalid path"
    else:
        return path
        
#---------CONSTRUCTION-#@@@@@#
def keyinput():
    key = input('key: ')
    
    
    return key
#-------------------------------

