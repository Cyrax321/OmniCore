''' 

Instructions
Snapple is a famous tea brand born in Brooklyn, NY. Every bottle cap hides a quirky, fun fact. 🍑

Use the random module to generate a number between 1 and 6.

Then, use an if/elif/else statement to print out one of these Snapple facts:

'Flamingos turn pink by eating shrimp.'
'Honey never goes bad.'
'Shrimp can only swim backwards.'
'A taste bud\'s life is about 10 days.'
'You can\'t sneeze while sleeping.'
'Tiny pocket in jeans was for watches.' 

'''

import random 
number = random.randint(1,6)

if number == 1 :
  print('Flamingos turn pink by eating shrimp.')
elif number == 2 :
  print('Honey never goes bad.')
elif number == 3 :
  print('Shrimp can only swim backwards.')
elif number == 4 :
  print('A taste bud\'s life is about 10 days.')
elif number == 5 :
  print('You can\'t sneeze while sleeping.')
else :
  print('Tiny pocket in jeans was for watches.')
  