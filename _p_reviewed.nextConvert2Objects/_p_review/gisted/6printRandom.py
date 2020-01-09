#module import demo

import random
for i in range(5):
    print(random.randint(1, 10))
    
# demo flow control: exit program with sys.exit()

import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed '+response+'.')    
