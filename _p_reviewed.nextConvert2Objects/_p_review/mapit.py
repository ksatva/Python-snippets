#! /usr/bin/python3
#mapIt.py

import webbrowser, sys#, pyperclip

if len(sys.argv)>1:
    #get address from commnd line
    address = ''.join(sys.argv[1:])
#else:
    #get address from clipboard
   # address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/'+address)


