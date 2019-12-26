#! python3

#shutil module
#shell utilities

import shutil, os


os.chdir('/home/kishore/testdir')
#shutil.copy() demo
shutil.copy('/home/kishore/testdir/a.txt', '/home/kishore/testdir/tdir')

def path():
    print('PATH: ')
    inputpath = input()
    if os.path.exists(inputpath):
        return inputpath
    else:
        path()

def ls(pathv):
    for filename in os.listdir(pathv):
        print(filename)
#path()

path1 = path()
ls(path1)

def keeploop():
    while True:
        userinput = input()
        if userinput == 'n':
            print('gbye')
            break
        else:
            continue

    
#shutil.move() demo
#shutil.move('/home/kishore/testdir/c.doc','/home/kishore/testdir2')



