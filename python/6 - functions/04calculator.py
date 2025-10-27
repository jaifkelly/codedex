# return: output of function (don't NEED to print)
#         sends values from one point in code to another 
# print: display some text to the user

# Create a calculator.py program and define these five functions:

# add(a, b) that adds two numbers a and b.
# subtract(a, b) that subtracts two numbers a and b
# multiply(a, b) that multiplies two numbers a and b.
# divide(a, b) that divides two numbers a and b.
# exp(a, b) that takes a to the exponent (or power) of b.
# Make sure to return the result in each function definition.

# Test your calculator by calling each function once to make sure that it works!

def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b

def exp(a, b):
  return a ** b

print(add(2, 6))
print(subtract(2, 6))
print(multiply(2, 6))
print(divide(2, 6))
print(exp(2, 6))