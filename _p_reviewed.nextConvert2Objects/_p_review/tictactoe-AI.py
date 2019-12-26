import random

def dB(board):
    print('\t|\t|')
    print(' '+board[7]+' | '+board[8]+' | '+board[9])
    print('\t|\t|')
    print('----------------')
    print('\t|\t|')
    print(' '+board[4]+' | '+board[5]+' | '+board[6])
    print('\t|\t|')
    print('----------------')
    print('\t|\t|')
    print(' '+board[1]+' | '+board[2]+' | '+board[3])
    print('\t|\t|')

def ipL():
    letter=''
    while not (lettet =='X' or letter =='O'):
        print('X or O?')
        letter=input().upper()

    if letter = 'X':
        return['X','O']
    else:
        return['O','X']

def whofrst():
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player' #..........to be continued invent with python pg185
    
        
