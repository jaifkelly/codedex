# Create a program that checks whether a grade is above or below 55.

# Start by creating a variable called grade and give it a value that's between 0 and 100.

# Write a if/else statement for the following:

# If grade is greater than or equal to 55, then print "You passed."
# Else, print "You failed."


import random
grade = random.randint(0, 100)

if grade >= 55:
  print("You passed.")
else:
  print("You failed.")