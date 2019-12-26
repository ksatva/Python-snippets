#tictactoe.py
# q  w  e
# a  s  d
# z  x  c
#above are playing keys

theBoard = {'q': ' ', 'w': ' ', 'e': ' ', 'a': ' ', 'd': ' ', 's': ' ', 'z': ' ', 'x': ' ', 'c': ' '}

def printBoard(board):
    print('\n')
    print(board['q']+' | ' +board['w']+' | '+board['e'])
    print('---+---+---')
    print(board['a']+' | ' +board['s']+' | '+board['d'])
    print('---+---+---')
    print(board['z']+' | ' +board['x']+' | '+board['c'])

turn = 'x'
for i in range(9):
    printBoard(theBoard)
    print('Turn for '+turn+' . Move on with space?')
    move = input()
    theBoard[move] = turn
    if turn == 'x':
        turn = 'o'
    else:
        turn = 'x'
printBoard(theBoard)
    
#http://nostarch.com/automatestuff/
