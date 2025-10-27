print('=======================')
print('sorting hat quiz 🎩')
print('=======================')

print("let's find out what house YOU belong to...")
input('what is your name? ')
print("awesome. let's get right to it!")
print("answer all of these to the best of your ability")

#instantiate each house 
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0


# ~~~~~~~~~~~~~~~ q1 ~~~~~~~~~~~~~~~


print("q1: do you like dawn or dusk?")
print("          1) dawn")
print("          2) dusk")

ans1 = int(input('choose your answer (1-2): '))

if ans1 == 1:
    gryffindor += 1
    ravenclaw += 1
elif ans1 == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print("incomplete answer, moving on")
print("onto the next question!")


# ~~~~~~~~~~~~~~~ q2 ~~~~~~~~~~~~~~~


print("q2: when i'm dead, i want people to remember me as?")
print("          1) the good")
print("          2) the great")
print("          3) the wise")
print("          4) the bold")

ans2 = int(input('choose your answer (1-4): '))

if ans2 == 1:
    hufflepuff += 2
elif ans2 == 2:
    slytherin += 2
elif ans2 == 3:
    ravenclaw += 2
elif ans2 == 4:
    gryffindor += 2
else:
    print("incomplete answer, moving on")
print("onto the last question!")


# ~~~~~~~~~~~~~~~ q3 ~~~~~~~~~~~~~~~


print("q3: which kind of instrument most pleases your ear?")
print("          1) the violin")
print("          2) the trumpet")
print("          3) the piano")
print("          4) the drum")

ans4 = int(input('choose your answer (1-4): '))

if ans4 == 1:
    slytherin += 4
elif ans4 == 2:
    hufflepuff += 4
elif ans4 == 3:
    ravenclaw += 4
elif ans4 == 4:
    gryffindor += 4
else:
    print("incomplete answer, that's okay!")
print("here's how you did...")

print("gryffindor: ", gryffindor)
print("ravenclaw: ", ravenclaw)
print("hufflepuff: ", hufflepuff)
print("slytherin: ", slytherin)

winner = max(gryffindor, ravenclaw, hufflepuff, slytherin)

print("and the winner is...")

if gryffindor == winner:
    print("Gryffindor! 🦁")
elif ravenclaw == winner:
    print("Ravenclaw! 🦅")
elif hufflepuff == winner:
    print("Hufflepuff! 🦡")
else:
    print("Slytherin! 🐍")