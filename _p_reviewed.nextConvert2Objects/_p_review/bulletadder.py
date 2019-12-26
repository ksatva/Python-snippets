import pyperclip as p

text = p.paste()
#operate on text
text = text.replace('\t', ' ')
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '*' + lines[i]
text = '\n'.join(lines)    

    
p.copy(text)
