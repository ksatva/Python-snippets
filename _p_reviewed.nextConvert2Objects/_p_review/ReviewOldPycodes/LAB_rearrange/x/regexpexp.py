#! python3

#regexp.py

from re import *
string = 'A quick brown fox jumps over the lazy dog. A QUICK BROWN FOX JUMPS OVER THE LAZY DOGBatBatBatBatmanBatman batwomanmanBatman batwomanman supermanwoman heman woman superwoman '

def regex(mode, searchIn):

    #regexList = ['\\d', '\\D', '\\w', '\\W', '\\s', '\\S', '^', '$', '|', '?', '*', 're.I', 're.DOTALL', 're.VERBOSE']
    #string = 'A quick brown fox jumps over the lazy dog. A QUICK BROWN FOX JUMPS OVER THE LAZY DOGBatBatBatBatmanBatman batwomanmanBatman batwomanman supermanwoman heman woman superwoman '

    print('Enter search format: ',end=' ')
    #reFormat = input()

    #print(reFormat)
    #print(type(reFormat))

    reObject = compile(r'^wo')
    
    #reObject = compile(input())
    print(reObject)
    
    if mode == ('s' or 'S'):
        mo = reObject.search(searchIn)
        #print(mo.groups())
        return mo.groups()
    elif mode == ('f' or 'F'):
        mo = reObject.findall(searchIn)
        #print(mo)
        return mo
    
          
# program has bugs with string input of special characters
# to write a debugging code with a list of all possible inputs

#regexpal.com
