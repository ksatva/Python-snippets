# import random
# guess = ''
# while guess not in('h','t'):
#     print('Guess the coin toss!Enter heads or tails:')
#     guess = input()
# if guess == 'h':
#     guess = 1
# else:
#     guess = 0
# toss = random.randint(0,1)  #0 is tails, 1 is heads
# #print(toss)
# if toss == guess:
#     print('You got it!')
# else:
#     print('Nope! guess again!')
#     guess = input()
#     if guess == 'h':
#         guess = 1
#     else:
#         guess = 0
#     toss = random.randint(0,1)
#     #print(toss)
#
#     if toss == guess:
#         print('You got it!')
#     else:
#         print('Nope. You are really bad at this game.')



import random

guess = ''
count = 0
flag = True
while guess not in ('h', 't') and flag == True:
    guess = input('\nGuess the coin toss! Enter heads or tails:')
    guess = 1 if guess == 'h' else 0

    toss = random.randint(0, 1)  # 0 is tails, 1 is heads
    print('toss result: ', 'h' if toss == 1 else 't')
    print('win' if toss == guess else 'fail')

    count += 1
    if count == 3:
        flag = False


#     guess = input()
#
#     if guess == 'h':
#         guess = 1
#     else:
#         guess = 0
#     toss = random.randint(0, 1)
# # print(toss)
#
# if toss == guess:
#     print('You got it!')
# else:
#     print('Nope. You are really bad at this game.')
