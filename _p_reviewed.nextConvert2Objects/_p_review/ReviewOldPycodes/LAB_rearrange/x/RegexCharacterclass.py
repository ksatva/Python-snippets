#! python3

#character class
#finding all vowels in the input sring
#for range of ############

import re

vowelRegex = re.compile('[aeiouAEIOU]')
print(vowelRegex.findall('Robocop eats baby food. BABY FOOD.'))

#finding all consonants in the input string
consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('Robocop eats baby food. BABY FOOD.'))


#demo3
atRegex = re.compile(r'...at.')   #each . (dot) is a character
print(atRegex.findall('The cat in the hatsat on the flat mat.'))

#demo4
nameRegex = re.compile(r'First name: (.*) LAST NAME: (.*)')
mo = nameRegex.search('First name: Al LAST NAME: sweigart')
print(mo.group(1))
print(mo.group(2))

#demo4
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

#demo5
greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

#newlineRegex
nonewLineRegex = re.compile('.*')
mo = nonewLineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
print(mo.group())                      

#newlineRegex demo2
newLineRegex = re.compile('.*',re.DOTALL)
print(newLineRegex.search('Serve the public trust.\nProtcect the innocent.\nUphold the law.').group())

#case sensitive regex matching
robocop = re.compile(r'robocop', re.I)  # re.I ignore case
print(robocop.search('Robocop is balak cop, robo, ROBOCOP').group())

#regex string substitution
#sub()
nameRegex = re.compile(r'Agent \w+')
print(nameRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

#DEMO2
agentNameRegex = re.compile(r'Agent (\w)\w*')
print(agentNameRegex.sub(r'\1****','Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))


#complex Regex management
#demo

# ''' (triple quote) syntax to create multiple line strings 
phoneRegex = re.compile(r'''(
    (\d{3}|\(d{3}\))?
    (\s|-|\.)?
    \d{3}
    (\s|-|\.)
    \d{4}
    (\s*(ext|x|ext.)\s*\d{2,5})?
    )''',re.VERBOSE)


#re.compile() functin cantake only single argument
#to combine (|) pipe character is used
#demo

someRegexvalue=re.compile('foo',re.IGNORECASE | re.DOTALL)
someRegexvalue=re.compile('foo',re.IGNORECASE | re.DOTALL | re.VERBOSE)


#for more information on bitwise operators
#http://nostarch.com/automatestuff/
