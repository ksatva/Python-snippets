import os

#function checks external device 
def externaldevice():
    count = 0
    for filename in os.listdir('/media/kishore'):
        count+=1
    if count>=1:
        print(str(count)+' nos.')
        return True
    else:
        print('nil')
        return False


def pathInput():
    print('''\n
             checking path vaidity\n
             os.path.exists()\n
             **Enter Path: **''')
    path = input()
#main path condition if path exists
    if os.path.exists(path):
        print(os.path.exists(path))

        #if os.path.isdir(path):
            #dir.....
        #elif os.path.isfile(path):
            #file..........
        
            
        return True
    
#exit from path condition
    elif path == 'n':
        print('gbye')
        return False
    
#Check external device
    elif path == 'extdev':
        return externaldevice()
    
    else:
        print('....x')
        return True









pathInput()
#while pathInput():
 #   continue
