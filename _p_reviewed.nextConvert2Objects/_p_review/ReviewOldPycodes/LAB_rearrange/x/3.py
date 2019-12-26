#annoying while loop
print('Demo 1')
name=''
while name != 'kishore':
    print('Please type your name.')
    name = input()
print('Thank you!')

print('\n\nDemo2::break satement')
while True:
    print('Please type your name')
    name = input()
    if name =='kishore':
        break
print('Thank You!!')    

print('See infinite loop demo?')
userInput = input()
if userInput == 'y' or 'Y':
    while True:
        print('hello infinite world!')
