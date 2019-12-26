spam =  ['cats','dofs', 'moose']
bacon= ['dogs','moose','pats']

x = spam==bacon
print(x)

spam = {'name': 'xophie', 'age' :'7'}

import pprint
message='a quick brown fox jumps over a lazy dog'
count={}

for character in message:
    count.setdefault(character,0)
    #print(type(count.setdefault(character,0))
    count[character]+=1

pprint.pprint(count)

