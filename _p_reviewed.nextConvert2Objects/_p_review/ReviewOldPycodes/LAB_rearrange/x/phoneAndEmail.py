#! python3
#phoneAndEmail.py -Finds phone numbers and emai addresses n a clipboard.

#???Download pyperclip module

import pyperclip, re

#phoneRegex
phoneRegex = re.compile(r'''(
    (\d{3}|\(d{3}\))?
    (\s|-|\.)?
    \d{3}
    (\s|-|\.)
    \d{4}
    (\s*(ext|x|ext.)\s*\d{2,5})?
    )''',re.VERBOSE)

#emailRegex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
    )''',re.VERBOSE)

#Find matches in a clipboard text.
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8] != ' ':
        phoneNum += ' x'+groups[8]
    matches.append(groups[0])

#copy resultsto the clipboard
if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print('copied to clipboard: ')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
    
