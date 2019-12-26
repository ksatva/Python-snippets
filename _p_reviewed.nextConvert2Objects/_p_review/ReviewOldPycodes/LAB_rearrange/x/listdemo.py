def supplieslist():
    supplies = []

    while True:
        print('Enter supplies:')
        supply = input()
        if supply =='':
            break
        supplies = supplies +[supply]
    return supplies

supplies = supplieslist()
for i in range(len(supplies)):
    print('Index '+str(i)+' in supplies is: '+supplies[i])

print('Enter supply name')
ip = input()
if ip not in supplies:
    print('entry %s not found'%ip)
else:
    print('%s is a supply'%ip)
