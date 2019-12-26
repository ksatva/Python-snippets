from zipfile import *
import os

os.chdir('/home/kishore/Downloads')
examplezip = ZipFile('pyperclip-1.5.27.zip')
#print(examplezip.namelist())
for name in examplezip.namelist():
    print(str(name)+' : '+str(examplezip.getinfo(name)))
    spaminfo = examplezip.getinfo(name)
    print(str(spaminfo.file_size),end=' ')
    print(str(spaminfo.compress_size))
    print('compressed file is %sx smaller!\n'%round(spaminfo.file_size/spaminfo.compress_size,3))
examplezip.close()
