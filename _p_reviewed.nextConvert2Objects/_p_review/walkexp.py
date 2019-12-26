import os
path='/home/kishore/testdir'
for foldername, subfolders, filenames in os.walk(path):
    print('the current folder is '+foldername)

    for subfolder in subfolders:
        print('subfolder of '+foldername+' : '+subfolder)
    for filename in filenames:
        print('file indide ' +foldername+' : '+filename)
    print(' ')    
