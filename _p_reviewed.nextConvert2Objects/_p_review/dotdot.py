import time
print('press Ctrl-C to quit......',end='')
string = '\\'
string1 = '|'
string2 = '-'
string3 = '/'
try:
    while True:
        print(string,end='')
        print('\b'*len(string),end='',flush =True)
        time.sleep(.25)
        print(string1,end='')
        print('\b'*len(string1),end='',flush =True)
        time.sleep(.25)
        print(string2,end='')
        print('\b'*len(string2),end='',flush =True)
        time.sleep(.25)
        print(string2,end='')
        print('\b'*len(string3),end='',flush =True)
        time.sleep(.25)
        print('\b'*len(string1),end='',flush =True)
        time.sleep(.25)
        print(string2,end='')
except KeyboardInterrupt:
    print('\nDone')
