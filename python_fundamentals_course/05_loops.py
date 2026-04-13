"""
=========================================================
LESSON 5: Loops (Repeating Actions)
=========================================================

1. DO NOT REPEAT YOURSELF!
If you have 10,000 images in an AI dataset, you can't write 10,000 lines of code.
You write 1 line of code inside a Loop!

2. FOR LOOPS
A `for` loop cycles through every item in a list one by one.

    animals = ["Dog", "Cat", "Bird"]
    for animal in animals:
        print(animal)

`animal` becomes "Dog", then the loop restarts, and `animal` becomes "Cat", etc.

3. FOR RANGES
Sometimes you just want to do something 5 times. Use `range(5)`!
    
    for number in range(5):
        print(number) # Prints 0, 1, 2, 3, 4 (Stops BEFORE 5!)

4. ACCUMULATOR PATTERN
A very common programming trick is adding up a total.
    total = 0
    for number in [1, 2, 3]:
        total = total + number
    print(total) # Prints 6!

=========================================================
YOUR TURN (PRACTICE)
=========================================================
"""

def practice_one():
    # TODO:
    # A list of numbers is given below.
    numbers = [10, 10, 10]
    # Set a variable `total = 0` BEFORE the loop.
    # Write a `for` loop to go through the list, adding each number to `total`.
    # After the loop finishes (un-indent!), return `total`.
    pass

def practice_two():
    # TODO:
    # Create an empty list: `results = []`
    # Use `range(3)` in a for loop.
    # Inside the loop, append the word "Hello" to the `results` list.
    # Return `results`.
    pass


# ==========================================
# TEST RUNNER (Do not modify!)
# ==========================================
if __name__ == "__main__":
    passed = 0
    try:
        if practice_one() == 30:
            print("✅ Practice 1 Passed! Accumulator loop works perfectly.")
            passed += 1
        else: print("❌ Practice 1 Failed. Make sure your total builds up!")
    except Exception: pass

    try:
        res = practice_two()
        if type(res) == list and len(res) == 3 and res[0] == "Hello":
            print("✅ Practice 2 Passed! Looping ranges.")
            passed += 1
        else: print("❌ Practice 2 Failed.")
    except Exception: pass
    
    if passed == 2:
        print("\n🎉 EXCELLENT! Loops are the bread and butter of Python.")
