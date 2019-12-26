#! python3

#magic8ball.py

from random import *
from myFunc import *

number = [1,2,3,4,5,6,7,8,9]
outcome = ['certain', 'decidedly so', 'try again', 'yes', 'ask again', 'concentrate', 'no', 'not so good', 'doubtful']

def getAnswer(ansNum):
    mapChart = dictFrom2list(number, outcome)
    #dictValue = ansNum
    return mapChart[ansNum]

while True:
    print('PLAY? ',end=' ')
    userInput = input()
    if userInput == 'n':
        break
    print(getAnswer(randint(1,9)))
    print('---END---\n')
        
    
    


#khura iocl card no. #---6070 9403 3179 2811---

