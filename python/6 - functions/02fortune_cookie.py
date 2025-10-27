# how to define a function
# def name():
  # The code inside

# calling the function/executing the function
  #name()

# Create a fortune_cookie.py program that gives the user random fortunes.

# Define a function named fortune(). Inside the function, print out a random fortune from the list of options below:

# Don't pursue happiness – create it.
# All things are difficult before they are easy.
# The early bird gets the worm, but the second mouse gets the cheese.
# Someone in your life needs a letter from you.
# Don't just think. Act!
# Your heart will skip a beat.
# The fortune you search for is in another cookie.
# Help! I'm being held prisoner in a Chinese bakery!
# Make sure to use the random module's random.randint() and an if/elif/else.

# Then, call the fortune() function three times and see what you get!

# Bonus: If you're daring, rewrite the function without an if/elif/else.

import random

def fortune():
  random_fortune = random.randint(1,8)
  if random_fortune == 1:
    print("Don't pursue happiness, create it.")
  elif random_fortune == 2:
    print('All things are difficult before they are easy.')
  elif random_fortune == 3:
    print('The early bird gets the worm, but the second mouse gets the cheese.')
  elif random_fortune == 4:
    print('Someone in your life needs a letter from you.')
  elif random_fortune == 5:
    print("Don't just think. Act!")
  elif random_fortune == 6:
    print('Your heart will skip a beat.')
  elif random_fortune == 7:
    print('The fortune you search for is in another cookie.')
  elif random_fortune == 8:
    print("Help! I'm being held prisoner in a Chinese bakery!")
  else:
    print('Your day will be beautiful!')

fortune()
fortune()
fortune()