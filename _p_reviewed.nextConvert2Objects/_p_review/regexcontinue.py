from myFunc import *

def regexcontinue(mode=input(),searchFile=input()):
    while True:
        regex(mode,searchFile)
        print('continue?',end=' ')
        reply=input()
        if reply == 'n':
            break


#to be modified
