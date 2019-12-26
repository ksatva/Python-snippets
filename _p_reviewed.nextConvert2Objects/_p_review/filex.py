from shelve import *

shelfFile = open('myData')
cats = ['k', 'l', 'm']
shelfFile['cats'] = cats
shelfFile.close()
