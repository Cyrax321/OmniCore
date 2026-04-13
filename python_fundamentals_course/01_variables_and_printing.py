"""
=========================================================
LESSON 1: Variables & Printing
=========================================================

Welcome to Python! 

1. WHAT IS A VARIABLE?
Think of a variable as a labeled box where you can store data.
When you write:
    age = 25
You are creating a box labeled 'age' and putting the number 25 inside it.

2. DATA TYPES
Python handles different types of data:
- Integers (Whole numbers):  `x = 10`
- Floats (Decimals):         `y = 3.14`
- Strings (Text):            `name = "Cyrax"`
- Booleans (True/False):     `is_cool = True`

3. PRINTING
To see what's inside a box, you use the `print()` command.
    print(age)      # This prints 25
    print("Hello")  # This prints the literal text Hello

=========================================================
YOUR TURN (PRACTICE)
=========================================================
Scroll down to the empty functions. Create the variables requested
and return them! Let me know if you get stuck.
"""

def practice_one():
    # TODO: Follow these 3 steps exactly!
    # 1. Create a variable named `my_name` and set it equal to your name (as a string).
    # 2. Create a variable named `my_age` and set it to a number.
    # 3. Create a variable named `is_learning` and set it to True.
    # 4. Return all three variables separated by commas: `return my_name, my_age, is_learning`
    pass

def practice_two():
    # TODO: 
    # Create a variable named `greeting` and set it to the exact text "Hello World"
    # Return it!
    pass


# ==========================================
# TEST RUNNER (Do not modify!)
# ==========================================
if __name__ == "__main__":
    passed = 0
    
    try:
        res1 = practice_one()
        if res1 and len(res1) == 3 and type(res1[0]) == str and type(res1[1]) in [int, float] and type(res1[2]) == bool:
            print("🌸 Practice 1 Passed! You created all the correct variable types!")
            passed += 1
        else:
            print("(╥﹏╥) Practice 1 Failed. Make sure you return a string, a number, and a boolean.")
    except Exception as e:
        print(f"(・_・;) Practice 1 Error: {e}")
        
    try:
        res2 = practice_two()
        if res2 == "Hello World":
            print("🌸 Practice 2 Passed! You made a string correctly!")
            passed += 1
        else:
            print(f"(╥﹏╥) Practice 2 Failed. Make sure you return exactly 'Hello World'. Got '{res2}'")
    except Exception as e:
         print(f"(・_・;) Practice 2 Error: {e}")
         
    if passed == 2:
        print("\n✨ AMAZING! You are ready for Lesson 2!")
