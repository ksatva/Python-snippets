#dictionaries
#{'keys':'values')
#every 'key' is associated with a 'value'
#can use integer values as keys
#order of {key1:value1,key2:value2} does not matter unlike lists

myCat={'size':'fat', 'color':'gray', 'disposition': 'loud', 'gender': 'male'}
spam={112345:'luggage combination', 32: 'the answer'}

birthdays={'Alice':'Apr 1','Bob':'Dec 12'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == ' ':
        break

    if name in birthdays:
        print(birthdays[name]+' is the birthday of '+name)
    else:
        print('No information for '+name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated')
        
