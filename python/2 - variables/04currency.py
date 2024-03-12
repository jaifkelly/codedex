# create a program that asks the user for the amount they have 
# in peso, soles, and reais and calculates the total in USD.

pesos = int(input("what do you have left in pesos? "))
reais = int(input("what do you have left in reais? "))
soles = int(input("what do you have left in soles? "))

total = pesos * .025 + reais * .28 + soles * .21

print(total)