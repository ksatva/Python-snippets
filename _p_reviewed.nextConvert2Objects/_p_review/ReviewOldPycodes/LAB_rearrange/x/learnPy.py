message = 'It was a bt Python 3.4.3 (default, Nov 17 2016, 01:08:31) C 4.8.4] on linuxType "copyright", "credits" or "license()" for more information.'
print (message)
count={}

for character in message:
    count.setdefault(character,0)
    count[character] += 1

print(count)
