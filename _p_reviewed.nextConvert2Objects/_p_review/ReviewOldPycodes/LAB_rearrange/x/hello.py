# THE FIRST PROGRAM
# ctrl + s :: to save
# F5 :: to run Module

print ('Hello World!')
print ('What is your name?')
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')
myAge = input()
print('You will be '+str(int(myAge)+1)+' in a year.')

print('\nInput: ')
myName2=input()
if myName2 == myName:
    print('Hello again, '+ myName2)
else:
    print('Hello stranger')
    print('Enter password: ')
    password = input()
    if password == 'swordfish':
        print('Access granted')
        print('Age:')
        ageStranger=input()
        if int(ageStranger) < 12:
            print('kiddo')
        elif int(ageStranger) > 2000:
            print('Unlike you immortal vampire.^O^')
        elif int(ageStranger) > 100:
            print('Hello Dadu! You crossed a century')
    else:
        print('#4%#Banana$#%#papoi$@#@!$')
        

      
