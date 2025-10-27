# When you go to a drive-thru like McDonald's, 
# you can order food using the item numbers. 
# For example, a Happy Meal might be a #3!

# Create a drive_thru.py program with your favorite fast food chain's menu.

# Define a get_item() function that takes in one parameter, 
# the number of the item you want to order, and returns the name of that item!

# Make sure to call this function a few times to make sure that it works!

# Lastly, let's do the following:

# Create a welcome menu and put that in a welcome() function.
# Create a main program that takes in user input with input().

def get_item(item_number):
  if item_number == 1:
    return '🍔 Cheeseburger' 
  elif item_number == 2:
    return '🍟 Fries' 
  elif item_number == 3:
    return '🥤 Soda' 
  elif item_number == 4:
    return '🍦 Ice Cream' 
  elif item_number == 5:
    return '🍪 Cookie'
  else:
    return 'invalid option'

def welcome():
  print('Menu:')
  print('1. 🍔 Cheeseburger')
  print('2. 🍟 Fries')
  print('3. 🥤 Soda')
  print('4. 🍦 Ice Cream')
  print('5. 🍪 Cookie')

welcome()

user_input = int(input('Welcome to JK cooking corner, please select an item to order:'))
print(get_item(user_input))