
import shutil,os   #, send2trash
os.chdir('/home/kishore/testdir')
#pathfr =
#pathto =
#shutil.copy(pathfr, pathto)
#filename =
#changedNamewithPath =
#shutil.copy(filename,changedNamewithPath)

shutil.copytree('/home/kishore/testdir','/home/kishore/testdir_backup')
shutil.move('/home/kishore/testdir/f.html','/home/kishore/testdir/tdir5')

file = open('file.txt','a')
file.write('my name is byr this is my byr')
file.close()

#send2trash(send2trash(file.txt))

#import ls
#ls.ls()





