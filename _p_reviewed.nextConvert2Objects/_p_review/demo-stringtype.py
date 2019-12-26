#string
#list-like type
#but ulike list:
#string is immutable

name = 'Zophie'
for letter in name:
    print(' * * * * '+letter+' * * * * ' )

print(name[1])
print(name[2:5])
print('Zo' in name)

#Following process is to mutate a string
name='Zophie a cat'
newname=name[0:7]+'the'+name[8:12]
print(name)
print(newname)

#An example with list
eggs = [1,2,3]
eggs = [4,5,6]  #Entire new list is created***previous listis not modified
#to modify list ::
eggs = [1,2,3]
del eggs[2]     #[2] is the index of list
del eggs[1]
del eggs[0]
eggs.append(4)
eggs.append(5)
eggs.append(6)
print(eggs)


#--------STRING METHODS--------
#--upper()--lower()--isupper()--islower()

spam = 'hello world'
spam = spam.upper()
uspam= spam
spam = spam.lower()
print(uspam.islower())
print(uspam.isupper())      #boolean :: True/False

#----------
'hello'.upper()#HELLO
'hello'.upper().lower()#hello
'hello'.upper().lower().upper()#HELLO
'Hello'.lower().islower()#True

#--------
print('how are You?')
feeling = input()
if feeling.lower() == 'great':
    print('i feel great too')
else:
    print('I hope the rest of your day is good')

    
#--------isX string methods-----------
#-----isalpha()----isalnum()----isdecimal()-----isspace()-----istitle()------
    
'hello'.isalpha()#True, if only alphabet
'hello123'.isalpha()#False
'hello123'.isalnum()#True-alphanumeric
'123'.isdecimal()#True
'     '.isspace()#True
'This Is Title Case'.istitle()#True-words begin with uppercase followed by lowercase letters
'This Is Title Case 123'.istitle()#True
'This Is not title Case'.istitle()#False
'This Is NOT Title Case EITHER'.istitle()#False


#------------startswith()--------endswith()---------------
'hello world'.startswith('hell')#True
'hello world'.endswith('rld')#True
'abcde123'.startswith('ab123')#False
'abcde123'.endswith('12')#False

'hello world'.startswith('hello world')#True
'hello world'.endswith('hello world')#True


#------------join()----------split()-------------
#..



#---Justifying Text-----
#----rjust()-----------ljust()---------center()-----------
'hello'.rjust(10)
'hello'.rjust(20)

'hello'.rjust(20,'*')
'hello'.ljust(20,'-')
'hello'.center(20,'=')

#--------removing whitespace---------
#----strip()-------rstrip()--------lstrip()-------
spam = '       hello world       '
print(spam.strip())#strips whitespace both sides
print(spam.lstrip())#strips whitespace left side
print(spam.rstrip())#strips whitespace right side


#----------install "pyperclip" module----------
