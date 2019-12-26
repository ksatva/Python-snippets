#os.path.join
import os
print(os.path.join('usr','bin','spam'))

print(os.getcwd())  #for current working directory

os.chdir('/home/kishore/testdir')   #to change directory
print(os.getcwd())

#single dot ( . ) -this directory
#dot-dot ( . . ) -parent folder
#not a directory but notations of path

#os.makedirs('/home/kishore/LearnPY/delicious/walnut/waffles')
print(os.getcwd())

print(os.path.abspath('.'))     #for absolute path
print(os.path.abspath('./i.xml'))
print(os.path.isabs('.'))       #check if absolute path
print(os.path.isabs(os.path.abspath('.')))

print(os.path.relpath('/home/kishore/LearnPY/delicious'))
print(os.path.relpath('/home/kishore/LearnPY/delicious', '/home/kishore/testdir/tdir0'))
print(os.getcwd())

print('\n')
path = '~/testdir/e.html'
print(os.path.basename(path))   #for path basename
print(os.path.dirname(path))    #for path dirname

#os.path.split is a nice shortcut if both values needed
print('\n')
#to get path's dir name and base name together
#os.path.split(pathVariable)
pdfFilePath = '~/testdir/g.pdf'
print(os.path.split(pdfFilePath))
#same operation/ same tuple creation use paranthesis('xxxxx ')
print((os.path.dirname(pdfFilePath), os.path.basename(pdfFilePath)))

print(pdfFilePath.split(os.path.sep))   #a List is created
print(os.path.split('/home/kishore'))

print('\n')



#Finding file sizes
#finding folder contents
print(os.path.getsize('/home/kishore/Music/BryanAdamsSummerof69.mp3'))
print(os.path.getsize('/home/kishore/Music'))

print(os.listdir('/home/kishore/testdir'))
path = '/home/kishore/testdir'
print(os.listdir(path))
#print(os.listdir('/bin'))

#finding total file size in a directory
totalsize=0
for filename in os.listdir('/home/kishore/Music'):
    totalsize+= os.path.getsize(os.path.join('/home/kishore/Music',filename))
print(totalsize)





#program checking path validity

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


#-------------------------------------------
#reading and writing files
#open() call return File object
#read() / write() on the file object
#close() to close the File object

#binary files (pdf,mp3,doc... etc) self explore
    #for now text files only

def hellofile(vpath):
    vhellofile = open(vpath)
    print(type(vhellofile))
    vhellocontent = vhellofile.read()
    print(type(vhellocontent))

hellofile(path)
