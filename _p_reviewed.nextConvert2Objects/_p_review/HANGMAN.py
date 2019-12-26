import random
HANGMANPICS = ['''
+---+
|   |
|
|
|
|
======''','''
+---+
|   |
|   O
|
|
|
======''','''
+---+
|   |
|   O
|   |
|
|
======''','''
+---+
|   |
|   O
|  /|
|   
|
======''','''
+---+
|   |
|   O
|  /|\
|   
|
======''','''
+---+
|   |
|   O
|  /|\
|  / 
|
======''','''
+---+ 
|   |
|   O
|  /|\
|  / \ 
|
======''']

words = 'ant baboon badger bat beer beaver camel cat calm cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole mouse moose monkey mule newt ptter owl panda parrot piegon python rabbit ram rat raven rhinoo salmon seal shark'.split()

def getRandomword(wordList):
    wordIndex = random.randint(0, len(wordList)-1)
    return wordList[wordIndex]

def displayBoard(HANGMANPICS, missedletters, correctLetters, secretword):
    print(HANGMANPICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter,end=' ')
    print()

    blanks='_'*len(secretword)

    for i in range (len(secretword)):
        if secretword[i] in correctLetters:
            blanks=blanks[:i]+secretword[i]+blanks[i+1:]

    for letter in blanks:
        print(letter,end=' ')
    print()

def getGuess(alreadyGuess):
    while True:
        print('guess a letter')
        guess=input()
        guess = guess.lower()
        if len(guess)!=1:
            print('Please enter a single letter.')
        elif guess in alreadyGuess:
            print('Ypu have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('pl enter a letter')
        else:
            return guess

def playAgain():
    print('play again?')
    return input().lower().startswith('y')

print(' H A N G M A N ')
missedLetters=''
correctLetters=''
secretword = getRandomword(words)
gameIsDone = False

while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretword)
    guess = getGuess(missedLetters+correctLetters)

    if  guess is secretword:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretword)):
            if secretword[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('yes won')
            gameIsDone=True
    else:
        missedLetters += guess

        if len(missedLetters) == len(HANGMANPICS)-1:
            displayBoard(HANGMANPICS,missedLetters,correctLetters,secretword)
            print('out of guess!\nafter '+str(len(missedLetters))+'missed guess'+str(len(correctLetters))+ ' corrct guess theword was %s'%secretword)
            gameIsDone =True
    if gameIsDone:
        if playAgain():
            missedLetters=''
            correctLetters=''
            gameIsDone = False
            secretword = gerRandomword(words)
        else:
            break
