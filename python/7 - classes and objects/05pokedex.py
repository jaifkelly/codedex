# Create a new file called pokedex.py.

# Next, let's define a Pokemon class with the following attributes:

# entry (integer)
# name (string)
# types (list of strings)
# description (string)
# is_caught (boolean)

# Next, create an instance method called .speak() that prints a string of the sound a Pokémon makes. 
# A Pokémon usually just says their name, so make the .speak() simply print out their name twice!

# Then, create another instance method called .display_details() that prints the attributes of a Pokemon object.

# Lastly, create three Pokemon class objects and use the .speak() or .display_details() instance methods for each one.

# For all the super fans, try and add more attributes to the Pokemon class definition, like level, region, height, or weight.

class Pokemon:
  def __init__(self, entry, name, types, description, is_caught):
    self.entry = entry
    self.name = name
    self.types = types
    self.description = description
    self.is_caught = is_caught

  def speak(self):
    print(f"{self.name}! {self.name}!")

  def display_details(self):
    print(f"Entry Number: {self.entry}")
    print(f"Name: {self.name}")
    if len(self.types) == 1:
      print(f"Type: {self.types[0]}")
    else:
      print(f"Type: {self.types[0]}/{self.types[1]}")
    print(f"Description: {self.description}")
    if self.is_caught:
      print(f"{self.name} has already been caught!")
    else:
      print(f"{self.name} hasn\'t been caught!")

pikachu = Pokemon(25, 'Pikachu', ['Electric'], 'It has small electric sacs on both its cheeks. If threatened it looses electric charges from the sacs.', True)
torchic = Pokemon(255, 'Torchic', ['Fire'], 'It breathes fire of over 1,800 degrees Fahrenheit, including fireballs that leave the foe scorched black.', False)
bulbasaur = Pokemon(1, 'Bulbasaur', ['Grass, Poison'], 'They have blue-green bodies with darker blue-green spots. The seed on a its back is planted at birth and then sprouts and grows along with it.', False)

pikachu.speak()
pikachu.display_details()
print()
torchic.speak()
torchic.display_details()
print()
bulbasaur.speak()
bulbasaur.display_details()