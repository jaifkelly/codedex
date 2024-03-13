# Create a reading_list.py program that stores the following items in a books list:

# 'Zero to One'
# 'The Lean Startup'
# 'The Mom Test'
# 'Make It Stick'
# 'Life in Code'

# Suppose we want to add one more book to the list: 'Zero to Sold'. 
# Can you use a list method to do so?

# Let's say we finished reading 'Zero to One' and 'The Lean Startup'. 
# Can you use the .remove() method to remove one and the .pop() method to remove the other?

reading_list = ['Zero to One',
                'The Lean Startup',
                'The Mom Test',
                'Make It Stick',
                'Life in Code']

reading_list.append('Zero to Sold')
print(reading_list)

reading_list.remove('The Lean Startup')
print(reading_list)

reading_list.pop(4)
print(reading_list)