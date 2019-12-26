#demo return statement
import random
def getanswer(answerNumber):
    if answerNumber ==1:
        return 'It is certain'
    elif answerNumber==2:
        return 'It is decidedly so'
    elif answerNumber==3:
        return 'yes'
    elif answerNumber==4:
        return 'Repy Hazy try again'
    elif answerNumber==5:
        return 'Ask again later'
    elif answerNumber==6:
        return 'Concentrate and askagain'
    elif answerNumber==7:
        return 'My reply is no'
    elif answerNumber==8:
        return 'Outlook not so good'
    elif answerNumber==9:
        return 'very doubtful'

def play():
    r = random.randint(1,9)
    fortune = getanswer(r)
    print(fortune)

def shuffle():
    print('\nShuffle?')
    reply = input()
    if reply == 'y':
        play()
        shuffle()
    elif reply=='n':
        print('Gbye')
    else:
        print('Wrong input')
        shuffle()

play()
shuffle()    
