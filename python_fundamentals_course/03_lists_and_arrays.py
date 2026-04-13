"""
=========================================================
LESSON 3: Lists and Arrays
=========================================================

1. WHAT IS A LIST?
Sometimes you need to store multiple items in a single variable. In Python, you use a List `[]`.
    inventory = ["Sword", "Shield", "Potion"]

2. INDEXING
Every item in a list has a numbered position, but computers start counting at ZERO!
"Sword" is index 0. "Shield" is index 1.
    print(inventory[0])    # Prints "Sword"
    print(inventory[1])    # Prints "Shield"

If you try to grab index 5, Python crashes with an "IndexError".

3. ADDING TO A LIST
You can push new items to the very end of the list using `.append()`
    inventory.append("Map")
    # Your inventory is now ["Sword", "Shield", "Potion", "Map"]

4. FINDING THE LENGTH
The `len()` function tells you how many items are inside.
    print(len(inventory))  # Prints 4

=========================================================
YOUR TURN (PRACTICE)
=========================================================
"""

def practice_one():
    # TODO: 
    # Create a list called `my_numbers` containing the numbers 10, 20, and 30.
    # Return it!
    pass

def practice_two():
    # TODO:
    # A list named `animals` is provided below.
    animals = ["Dog", "Cat", "Bird", "Tiger"]
    # Write code that returns ONLY the "Bird" from the list using indexing []!
    pass

def practice_three():
    # TODO:
    # A list is provided below.
    items = ["A", "B", "C"]
    # Append the letter "D" to it.
    # Then find the length of the list and return that length number!
    pass


# ==========================================
# TEST RUNNER (Do not modify!)
# ==========================================
if __name__ == "__main__":
    passed = 0
    try:
        if practice_one() == [10, 20, 30]:
            print("<3 Practice 1 Passed! Making lists.")
            passed += 1
        else: print(":( Practice 1 Failed.")
    except Exception: pass

    try:
        if practice_two() == "Bird":
            print("<3 Practice 2 Passed! Indexing arrays.")
            passed += 1
        else: print(":( Practice 2 Failed. Hint: 'Bird' is the 3rd item, so it's index 2!")
    except Exception: pass
    
    try:
        if practice_three() == 4:
            print("<3 Practice 3 Passed! Appending and counting length.")
            passed += 1
        else: print(":( Practice 3 Failed. Did you append D and then use len()?")
    except Exception: pass
    
    if passed == 3:
        print("\n(*^▽^*) FANTASTIC! You're catching on fast.")
