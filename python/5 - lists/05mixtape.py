# Create a mixtape.py program and think of a theme for the songs.

# Make a list called playlist and throw in some songs.

# 💿 Theme: Indie Travel Songs

# playlist = [
#   'Porches - rangerover',
#   'Mount Eerie - You Swan, Go On',
#   'Carolyn Polachek - Look at Me Now',
#   'Pinegrove - Darkness',
#   'LVP UP - Spirit Was',
#   'Mitski - First Love / Late Spring'
# ]

# Now loop over the list and print everything out! 📻

playlist = [
  'Porches - rangerover',
  'Mount Eerie - You Swan, Go On',
  'Carolyn Polachek - Look at Me Now',
  'Pinegrove - Darkness',
  'LVP UP - Spirit Was',
  'Mitski - First Love / Late Spring'
]

# with range 

for song in range(len(playlist)):
    print(playlist[song])
print('\n')

# without range 
    
for song in playlist:
    print(song)