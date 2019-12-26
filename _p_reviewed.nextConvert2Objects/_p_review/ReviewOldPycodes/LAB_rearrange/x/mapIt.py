#! python3
"""
mapIt.py - launches a map in the browser
using an address from the command line or clipboard
"""
import webbrowser, sys, pyperclip
if len(sys.argv)>1:
    #Get address from the command line
    address =' '.join(sys.argv[1:])
else:
    #get address from the clipboard.
    address = pyperclip.paste()

werbbrowser.open('http://www.google.com/maps/place/'+address)

