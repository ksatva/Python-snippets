#! python3

#Regex call

def regexcall(text):
    import re
    print('Enter regex search format: ')
    format = input()
    print(type(format))
    print(format)
    searchindex = re.compile(format)
    mo = searchindex.search(text)
    print('Found ' +mo.group(1),+' '+mo.group(2))
    
while True:
    print('Input text')
    text = input()
    if len(text)>8:
        regexcall(text)
    else: break
