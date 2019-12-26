import os

def delete(pathv):
    if os.path.isdir(pathv):
        print('shutil.rmtree('+str(pathv)+')?')
        promt=input()
        if promt == 'y':
            print('Lock..?')
            promt2 = input()
            if promt2 == 'y':
                shutil.rmtree(pathv)
                print('os.rmtree success!')

        else:
            print('os.rmdir('+str(pathv)+')?')
            promt2 = input()
            if promt == 'y':
                os.rmdir(pathv)
                print('os.rmdir success!')

    elif os.path.isfile(pathv):
        print('os.unlink('+str(pathv)+')?')
        promt = input()
        if promt == 'y':
            print('Lock..?')
            promt2=input()
            if promt2 ==  'y':
                  os.unlink(pathv)
                  print('os.unlink success!')
        
    
    
