weight = int(input("Enter your weight : "))
data = str(input("Enter the unit (kg(k) or lbs(l)) : "))

if data == "kg" or data == "k":
    lbs = weight * 2.20462 
    print(f"Your weight in lbs is : {lbs}")
elif data == "lbs" or data == "l":
    kg = weight / 2.20462
    print(f"Your weight in kg is : {kg}")
else: 
    print("Invalid unit")

    