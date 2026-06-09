"""
=========================================================
LESSON 4: If / Else Statements (Choices)
=========================================================

1. DECISIONS
How does a video game know if you died? It checks if your health is zero.
In Python, we check conditions using `if`, `elif` (else if), and `else`.

    health = 50
    if health <= 0:
        print("You died.")
    elif health < 20:
        print("Low Health Warning!")
    else:
        print("You are healthy.")

2. INDENTATION
Notice how the `print` is spaced horizontally inward from the `if`? That is called "Indentation." 
Python uses spaces (tabs) to know what code belongs inside the `if` block. If you forget to indent, Python crashes!

3. COMPARISONS
- `==` Check if EQUAL (Example: `age == 18`)
- `!=` Check if NOT EQUAL
- `>` and `<` Greater Than / Less Than
- `>=` and `<=` Greater/Less or Equal To

=========================================================
YOUR TURN (PRACTICE)
=========================================================
"""

def practice_one(age):
    # TODO:
    # Look at the 'age' variable coming in.
    # Write an if statement: if age is greater than or equal to 18, return "Adult"
    if age >= 18:
        return "Adult"
    # Otherwise (else), return "Minor"
    else:
        return "Minor"

def practice_two(password):
    # TODO:
    # Write an if statement checking if the password exactly equals "Secret123"
    if password == "Secret123":
        return True
    # If it does, return True. 
    else:
        return False 
    # Else, return False.


# ==========================================
# TEST RUNNER (Do not modify!)
# ==========================================
if __name__ == "__main__":
    passed = 0
    try:
        if practice_one(20) == "Adult" and practice_one(15) == "Minor":
            print("<3 Practice 1 Passed! If/Else routing correctly.")
            passed += 1
        else: print(":( Practice 1 Failed. Be sure to check age >= 18")
    except Exception: pass

    try:
        if practice_two("Secret123") == True and practice_two("password") == False:
            print("<3 Practice 2 Passed! String equality checking correctly.")
            passed += 1
        else: print(":( Practice 2 Failed.")
    except Exception: pass
    
    if passed == 2:
        print("\n(*^▽^*) AWESOME! Making choices in code is officially unlocked.")
