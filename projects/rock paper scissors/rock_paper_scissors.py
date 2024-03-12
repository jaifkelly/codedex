import random 

# title 

print('===================')
print('rock paper scissors')
print('===================')
print('     ')

# import random for usage

import random

# choices 


print('1) ✊ rock')
print('2) ✋ paper')
print('3) ✌️  scissor')
print('     ')

# player + computer choices

player = int(input("let's choose a number between 1-3:   "))
computer = random.randint(1,3)

# result

print(f'you chose: {player} and cpu chose {computer}')

# choose a winner

if player == computer:
    print('tie game :|')
    print('thanks for playing c:')
elif player == 1:
    if computer == 3:
        print('rock beats scissor, you win c:')
        print('thanks for playing!')
    elif computer == 2:
        print('paper beats rock, you lose :c')
        print('thanks for playing!')
elif player == 2:
    if computer == 1:
        print('paper beats rock, you win c:')
        print('thanks for playing!')
    elif computer == 3:
        print('scissor beats paper, you lose :c')
        print('thanks for playing!')
elif player == 3:
    if computer == 2:
        print('scissor beats paper, you win c:')
        print('thanks for playing!')
    elif computer == 1:
        print('rock beats scissor, you lose :c')
        print('thanks for playing!')
else:
    print("let's try again with a number between 1-3 c:")