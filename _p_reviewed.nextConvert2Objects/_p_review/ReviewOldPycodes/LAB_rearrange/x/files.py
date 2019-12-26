import os
    
hellofile = open('/home/kishore/testdir/a.txt')
hellocontent = hellofile.read()
print(hellocontent)
print(hellofile.readlines())

print(os.getcwd())

#print
baconFile = open('/home/kishore/testdir/b.txt')
print('1.'+baconFile.read())

baconFile = open('/home/kishore/testdir/b.txt', 'w')
baconFile.write('hello file world!\n')
baconFile.close()

#print
baconFile = open('/home/kishore/testdir/b.txt')
print('2'+baconFile.read())

baconFile = open('/home/kishore/testdir/b.txt','a')
baconFile.write('Bacon is not a vagetable')
baconFile.close()

#print
baconFile = open('/home/kishore/testdir/b.txt')
print('3'+baconFile.read())

#............................................
 
import shelve

shelfFile = shelve.open('mydata')
parts = ['laptop', 'cellphone', 'wifi-card']
shelfFile['parts'] = parts
shelfFile.close()
#....File created...
shelfFile = shelve.open('mydata')
print(type(shelfFile))
print(shelfFile['parts'])
shelfFile.close()
#...............
shelfFile = shelve.open('mydata')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()
#...............


#saving variables pprint.pformat()
import pprint
techs = [{'name':'monitor','desc':'o/p device'},{'name':'keyboard','desc':'i/p device'}]
print(pprint.pformat(techs))
fileobj = open('mytechs.py','w')
fileobj.write('techs= ' +pprint.pformat(techs) + '\n')
fileobj.close()

fileobj = open('/home/kishore/LearnPY/mytechs.py')
print('4'+fileobj.read())
