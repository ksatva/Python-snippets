#! python3

#Functions file

import os

#.....path().........
#path promt for path input
def path():
    print('PATH: ')
    inputpath = input()
    if os.path.exists(inputpath):
        return inputpath
    else:
        path()

#........................................................        
#..........ls()..........
#function list files and folders in path
def ls(pathv):
    for filename in os.listdir(pathv):
        print(filename)

#...................................................
#path1 = path()
#ls(path1)

#.............................................................
#..............keeploop()...........
#keep promting for input
def keeploop():
    while True:
        userinput = input()
        if userinput == 'n':
            print('gbye')
            break
        else:
            continue

