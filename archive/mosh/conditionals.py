#and or not 

price = int(input("Enter the price : "))
product = input("Enter the product (use the terms good,bad and ok ) : ")

if price < 10 and product == "good":
    print("Buy it ")
elif price > 10 and product == "bad":
    print("Don't buy it")
else:
    print("Decide for yourself")
