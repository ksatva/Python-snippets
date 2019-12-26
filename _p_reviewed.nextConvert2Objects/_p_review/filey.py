from shelve import *

shelfFile = open('myData')
rats = ['1', '2', '3']
shelfFile['rats'] = rats
shelfFile.close()
