
#? from os import *
#? chdir('path') doesnot work


import os
from re import *
import shutil

count = 0
#os.chdir('/home/kishore/LearnPY')
#os.makedirs('/home/kishore/LearnPY/zipfolder')
for filename in os.listdir('/home/kishore'):

    #print(filename)
    if filename.endswith('.py'):
        shutil.move(filename, '/home/kishore/LearnPY/')
        print(filename)
        count+=1
print('%s files moved'%count)
