# Ever wonder how many people live in New York City? What about London?

# Create a favorite_cities.py program.

# Let's make a City class that uses the __init__() method to define the following attributes:

# name (string)
# country (string)
# population (integer rounded to the nearest thousand people)
# landmarks (list of strings)
# Next, create an object for your hometown and assign the attributes above.

# Lastly, create another object of the city that you've always wanted to visit!

# Bonus: Add 2-3 more attributes, like nickname, founding year, mayor, etc.

class City:
  def __init__(self, name, country, population, landmarks):
    self.name = name
    self.country = country
    self.population = population
    self.landmarks = landmarks

chula_vista = City('Chula Vista', 'United States', 273841, 'Albert Barber House')
print(vars(chula_vista))