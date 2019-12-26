#! python3
#pw.py -A insecure password locker program

PASSWORDS ={'''
email':'43534rqwrqeftrq54rtqeteqr',
'blog':'vafdetggtretewfadse456',
'luggage' : '123456
'''}

import sys
if len(sys.argv)<2:
    print('Usage: python pw.py[account]-copu account password')
    sys.exit()

account= sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Passord for' +account+'copied to clipboard')
else:
    print('No account')
            
