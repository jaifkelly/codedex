# Write a program that asks the user some questions 
# using int() and places them into one of the Houses based on their answers:

# Q1) Do you like Dawn or Dusk?
#     1) Dawn
#     2) Dusk

# If answer is equal to 1, Gryffindor and Ravenclaw both get a +1.
# Else if answer is equal to 2, Hufflepuff and Slytherin both get a +1.
# Else, output the message "Wrong input."


# Q2) When I’m dead, I want people to remember me as:
#     1) The Good
#     2) The Great
#     3) The Wise
#     4) The Bold

# If the answer is 1, Hufflepuff +2.
# Else if answer is 2, Slytherin +2.
# Else if answer is 3, Ravenclaw +2.
# Else if answer is 4, Gryffindor +2.
# Else, output the message "Wrong input."


# Q3) Which kind of instrument most pleases your ear?
#     1) The violin
#     2) The trumpet
#     3) The piano
#     4) The drum

# If the answer is 1, Slytherin +4.
# Else if the answer is 2, Hufflepuff +4.
# Else if the answer is 3, Ravenclaw +4.
# Else if the answer is 4, Gryffindor +4.
# Else, output "Wrong input."

print('welcome to the sorting hat quiz!')
input('what is your name? ')
print("awesome. let's get right to it! \n answer all of these to the best of your ability")

#instantiate each house 
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

q1 = int(input('do you like dawn or dusk? \n 1) dawn \n 2) dusk \n '))

if q1 == 1:
    gryffindor += 1
    ravenclaw += 1
elif q1 == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print("oops, wrong input. let's try that again")
print("onto the next question!")

q2 = int(input("when i'm dead, i want people to remember me as: \n 1) the good \n 2) the great \n 3) the wise \n 4) the bold \n "))

if q2 == 1:
    hufflepuff += 2
elif q2 == 2:
    slytherin += 2
elif q2 == 3:
    ravenclaw += 2
elif q2 == 4:
    gryffindor += 2
else:
    print("oops, wrong input. let's try that again")
print("onto the last question!")

q3 = int(input("which kind of instrument most pleases your ear? \n 1) the violin \n 2) the trumpet \n 3) the piano \n 4) the drum \n "))

if q3 == 1:
    slytherin += 4
elif q3 == 2:
    hufflepuff += 4
elif q3 == 3:
    ravenclaw += 4
elif q3 == 4:
    gryffindor += 4
else:
    print("oops, wrong input. let's try that again")
print("all done! let's total these up and see what you get...")

print("gryffindor: ", gryffindor)
print("ravenclaw: ", ravenclaw)
print("hufflepuff: ", hufflepuff)
print("slytherin: ", slytherin)

winner = max(gryffindor, ravenclaw, hufflepuff, slytherin)

if gryffindor == winner:
    print("Gryffindor! 🦁")
elif ravenclaw == winner:
    print("Ravenclaw! 🦅")
elif hufflepuff == winner:
    print("Hufflepuff! 🦡")
else:
    print("Slytherin! 🐍")

# ~~~~~~~~~~~~~~~~~~~~ refactored in 07 ~~~~~~~~~~~~~~~~~~~~~~~~