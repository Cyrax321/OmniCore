"""
=========================================================
LESSON 7: Functions (Reusable Code)
=========================================================

1. CREATING YOUR OWN COMMANDS
So far you've been putting code inside `def practice_one():`. That is a Function!
A function is a block of code you can run over and over just by typing its name.

    def say_hello():
        print("Hello there!")

    say_hello()  # Doing this actually triggers the code!

2. ARGUMENTS (INPUTS)
Functions can accept variables passed into them, acting like a machine formula.

    def add_numbers(x, y):
        total = x + y
        return total
    
    my_math = add_numbers(5, 10) # my_math is magically 15 now!

3. RETURN = THE FINISH LINE
The `return` keyword spits an answer out of the function ending it immediately. 
If you write code underneath `return`, Python ignores it!

=========================================================
YOUR TURN (PRACTICE)
=========================================================
We aren't going to give you a pre-written function here!
"""

# TODO:
# Write a completely new function yourself named `multiply`
# It should accept two inputs: `a` and `b`. 
# Inside the function, return `a * b`!


# ==========================================
# TEST RUNNER (Do not modify!)
# ==========================================
if __name__ == "__main__":
    passed = 0
    try:
        if multiply(5, 5) == 25 and multiply(2, 3) == 6:
            print("<3 Practice 1 Passed! You defined your own function and passed arguments.")
            passed += 1
        else: print(":( Practice 1 Failed. Double check your math return.")
    except NameError:
        print(":( Error: A function named `multiply` doesn't exist. Did you spell it right?")
    except Exception as e: 
        print(f"o_O Practice 1 Error: {e}")
    
    if passed == 1:
        print("\n(*^▽^*)(*^▽^*)(*^▽^*) CONGRATULATIONS! You have completed the foundation course! (*^▽^*)(*^▽^*)(*^▽^*)")
        print("You are officially ready to tackle the python_core_quests folder!")
