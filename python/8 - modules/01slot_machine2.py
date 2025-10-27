import random
symbols = ['🍒',' 🍇', '🍉', '7️⃣']

def play():
  for i in range(1, 10):
    results = random.choices(symbols, k=3)
    print(f"{results[0]} | {results[1]} | {results[2]}")

    jackpot = results[0] == '7️⃣' and results[1] == '7️⃣' and results[2] == '7️⃣'

    if jackpot:
      print('Jackpot! 💰')
      break
    else:
      results = random.choices(symbols, k=3)

user_choice = ''
while user_choice.upper() != 'N':
  play()
  user_choice = input('Play again? Y or N: ')

print('Thanks for playing!')