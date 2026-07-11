'''question : Instructions
Ah, the four seasons of the year – winter, spring, summer, or fall; all you have to do is call!

Ask the user the month number using input().

Check for the four seasons using an if/elif/else statement and logical operators:

month is 1, 2, 3, print 'Winter 🌨️'
month is 4, 5, 6, print 'Spring 🌱'
month is 7, 8, 9, print 'Summer 🌻'
month is 10, 11, 12, print 'Autumn 🍂'
Everything else is 'Invalid'
Logical operators in Python include the and and or keywords. Which one should you use? '''

month = int(input("What's the month? Enter in numbers(1-12): "))

if 1 <= month <= 3 :
  print('Winter 🌨️')
elif 4 <= month <= 6 :
  print('Spring 🌱')
elif 7 <= month <= 9 :
  print('Summer 🌻')
elif 10 <= month <= 12 :
  print('Autumn 🍂')
else: 
  print('Invalid')