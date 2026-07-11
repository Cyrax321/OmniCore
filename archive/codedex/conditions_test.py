question1 = int(input("Do you like 1. Dawn or 2. Dusk?: "))

g = r = h = s = 0
if question1 == 1 :
  r = r + 1 
  g = g + 1  
elif question1 == 2 :
  h += 1
  s += 1 
else:
  print("Wrong input") 

question2 = int(input(" When I’m dead, I want people to remember me as 1) The Good, 2) The Great, 3) The Wise, 4) The Bold: "))

if question2 == 1 :
  h += 2
elif question2 == 2 :
  s += 2 
elif question2 == 3 :
  r += 2 
elif question2 == 4 :
  g += 2 
else:
  print("Wrong input")

question3 = int(input(" Which kind of instrument most pleases your ear? 1) The violin, 2) The trumpet 3)The piano, 4)The drum: "))
if question3 == 1 :
    s += 4
elif question3 == 2 :
    h += 4
elif question3 == 3 :
    r += 4
elif question3 == 4 :
    g += 4
else:
    print("Wrong input")

print(f"Gryffindor: {s}, Ravenclaw: {r}, Hufflepuff: {h}, Slytherin: {s}")

