#! python3

#regexp.py

from re import *

def regex(mode, searchIn):
    print('''
() - use to create separate groups
| - matching with pipe | (ex: "batman | tina fey"), (ex: 'Bat(man|mobile|copter'))
? - make part of text matching optional (ex: "bat(wo)?man")
* - group that precedes * can occur <0 to any no of times> in text (ex: 'bat(wo)*man')
\* - match actual '*' character
+ - match <1 or more no. of times>
\+ - match actual '+' character
{} - match specific repitions (ex: '(Ha){3}' for "hahaha" or more) (ex: '(ha){3,5}' --setting range)
{}? - nongreedy
[] - Own CHARACTER CLASS (ex: [aeiouAEIOU] --for vowel, ex: [^aeiouAEIOU] --consonant)
[^] - not
^ - begins with match (ex:^hello --matches string that begins with hello)
$ - ends with match (ex: '\d$' --ends with number)
    (Combine '^\d+$' --for whole string)
. - WILDCARD (ex: '.at', '..at', 'at.ct..p' --every . represents a character)
.* - WILDCARD MATCH EVERYTHING (default :: greedy)
.*? - nongreedy

\d - digit [0 - 9] <equivlent type (0|1|2|3|4|5|6|7|8|9)>
\D - any character
\w - any letter, numericdigit, underscore
\W - any letter not \w
\s - space, tab or new line character
\S - any character not \s
(Combinations format ex: \d+\s\w+')

greedy - match longest possible string (default)
nongreedy - match shortest string

re.DOTALL -
re.I - Ignore Case
''')
    print('Enter Search Format: ',end=' ')
    #reFormat = input()

    #print(reFormat)
    #print(type(reFormat))

    reObject = compile(input())
    print(reObject)

    if mode == ('s' or 'S'):
        mo = reObject.search(searchIn)
        #print(mo)
        return mo.groups()
    elif mode == ('f' or 'F'):
        mo = reObject.findall(searchIn)
        #print(mo)
        return mo
    
          
# program has bugs with string input of special characters
# to write a debugging code with a list of all possible inputs
#TO BE MODIFIED 
#regexpal.com
