"""
=========================================================
LESSON 2: Math & Logic
=========================================================

1. DOING MATH
Python is an amazing calculator.
- Addition:        `10 + 5`
- Subtraction:     `10 - 5`
- Multiplication:  `10 * 5`
- Division:        `10 / 5`   (This always returns a decimal -> 2.0)
- Exponents:       `10 ** 2`  (10 to the power of 2 -> 100)
- Modulo:          `10 % 3`   (The remainder! 10 divided by 3 is 9, remainder 1).

You can save the results to variables!
    total = 50 + 25

2. RE-ASSIGNING VARIABLES
Variables can change over time.
    score = 10
    score = score + 5   # This adds 5! The score is now 15.
    score += 5          # A shortcut! This does the exact same thing! (Score is now 20).

=========================================================
YOUR TURN (PRACTICE)
=========================================================
Scroll down and complete the math!
"""

def practice_one():
    # TODO: 
    # Create a variable `a` equal to 50
    # Create a variable `b` equal to 25
    # Create a variable `result` that is `a` minus `b`
    # Return `result`
    pass

def practice_two():
    # TODO:
    # Set a variable `health` to 100
    # Use the -= shortcut to subtract 20 from health! (Like you just took damage in a game)
    # Return `health`
    pass


# ==========================================
# TEST RUNNER (Do not modify!)
# ==========================================
if __name__ == "__main__":
    passed = 0
    try:
        if practice_one() == 25:
            print("<3 Practice 1 Passed! Basic math works.")
            passed += 1
        else:
             print(":( Practice 1 Failed. Expected 25.")
    except Exception as e: pass

    try:
        if practice_two() == 80:
            print("<3 Practice 2 Passed! You successfully modified a variable in place.")
            passed += 1
        else:
            print(":( Practice 2 Failed. Did you remember to subtract 20 from 100?")
    except Exception as e: pass
    
    if passed == 2:
        print("\n(*^▽^*) GREAT JOB! On to Arrays and Lists!")
