catnames = []
while True:
    print('Enter cat name '+str(len(catnames)+1)+' (or enter nothing to stop.):')
    name=input()
    if name=='':
        break
    catnames = catnames+[name] #list concatenation
print('the cat names are:')
for name in catnames:
    print(' '+name)
