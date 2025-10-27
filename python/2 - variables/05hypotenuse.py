# Create a program that asks the user for two numbers:
# a and b, and calculates the hypotenuse using the Pythagorean equation, rewritten like so:
# a**2(short) + b**2(short) = c**2(hypotneuse) 
# sq rt of something is the same as to the power of .5

a = int(input("input a: "))
b = int(input("input b: "))

c = (a**2 + b**2) ** .5

print(c)