import random 

# title 

print('===================')
print('rock paper scissors lizard spock')
print('===================')
print('     ')

# import random for usage

import random

# choices 


print('1) ✊ rock')
print('2) ✋ paper')
print('3) ✌️  scissors')
print('4) 🦎  lizard')
print('5) 🖖  spock')
print('     ')

# player + computer choices

player = int(input("let's choose a number between 1-5:   "))
computer = random.randint(1,5)

# result

print(f'you chose: {player} and cpu chose {computer}')

# choose a winner

if player == computer:
    print('tie game :|')
    print('thanks for playing c:')
elif player == 1:
    if computer == 3:
        print('rock breaks scissors, you win c:')
        print('thanks for playing!')
    elif computer == 2:
        print('paper covers rock, you lose :c')
        print('thanks for playing!')
    elif computer == 4:
        print('rock crushes lizard, you win c:')
        print('thanks for playing!')
    elif computer == 5:
        print('spock vaporizes rock, you lose :c')
        print('thanks for playing!')
elif player == 2:
    if computer == 1:
        print('paper covers rock, you win c:')
        print('thanks for playing!')
    elif computer == 3:
        print('scissors cuts paper, you lose :c')
        print('thanks for playing!')
    elif computer == 4:
        print('lizard eats paper, you lose :c')
        print('thanks for playing!')
    elif computer == 5:
        print('paper disproves spock, you win c:')
        print('thanks for playing!')
elif player == 3:
    if computer == 2:
        print('scissors cuts paper, you win c:')
        print('thanks for playing!')
    elif computer == 1:
        print('rock breaks scissors, you lose :c')
        print('thanks for playing!')
    elif computer == 4:
        print('scissors beats lizzard, you win c:')
        print('thanks for playing!')
    elif computer == 5:
        print('spock smashes scissors, you lose :c')
        print('thanks for playing!')
elif player == 4:
    if computer == 1:
        print('rock crushes lizard, you lose :c')
        print('thanks for playing!')
    elif computer == 2:
        print('lizard eats paper, you win c:')
        print('thanks for playing!') 
    elif computer == 3:
        print('scissors beats lizzard, you lose :c')
        print('thanks for playing!')
    elif computer == 5:
        print('lizard poisons spock, you win c:')
        print('thanks for playing!')
elif player == 5:
    if computer == 1:
        print('spock vaporizes rock, you win c:')
        print('thanks for playing!')
    elif computer == 2:
        print('paper disproves spock, you lose :c')
        print('thanks for playing!') 
    elif computer == 3:
        print('spock smashes scissors, you win c:')
        print('thanks for playing!')
    elif computer == 4:
        print('lizard poisons spock, you lose :c')
        print('thanks for playing!')
else:
    print("let's try again with a number between 1-3 c:")