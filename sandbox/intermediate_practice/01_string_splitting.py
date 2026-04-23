"""
=========================================================
PRACTICE: String Splitting (.split)
=========================================================
The `.split(mark)` method turns one string into a LIST of strings.
Example: "A-B-C".split("-") -> ["A", "B", "C"]
=========================================================
"""

def exercise_one():
    # TODO: Split this string by the comma ","
    # Return the resulting list!
    data = "Python,Java,C++,Ruby"
    new_data = data.split(",")
    return new_data

def exercise_two():
    # TODO: 
    # 1. Split this string by the dash "-"
    # 2. Return ONLY the second item in the list (The word "Orange")
    fruit_string = "Apple-Orange-Banana"
    new_fruit = fruit_string.split("-")
    return new_fruit[1]

def exercise_three():
    # TODO: THE LOG PARSER TRICK (Double Split)
    # 1. Split by the vertical bar " | " to get chunks.
    # 2. Take the FIRST chunk and split it again by ": "
    # 3. Return the number string (the second part of the second split).
    raw_data = "SCORE: 100 | USER: Cyrax"
    new_data1 = raw_data.split(" | ")
    new_data2 = new_data1[0].split(": ")
    return new_data2[1]


# ==========================================
# TEST RUNNER
# ==========================================
if __name__ == "__main__":
    passed = 0
    
    # Test 1
    try:
        if exercise_one() == ["Python", "Java", "C++", "Ruby"]:
            print("<3 Exercise 1 Passed!")
            passed += 1
        else: print(":( Exercise 1 Failed.")
    except Exception as e: print(f"o_O Exercise 1 Error: {e}")
    
    # Test 2
    try:
        if exercise_two() == "Orange":
            print("<3 Exercise 2 Passed!")
            passed += 1
        else: print(":( Exercise 2 Failed. Returning the whole list?")
    except Exception as e: print(f"o_O Exercise 2 Error: {e}")
        
    # Test 3
    try:
        if exercise_three() == "100":
            print("<3 Exercise 3 Passed!")
            passed += 1
        else: print(":( Exercise 3 Failed.")
    except Exception as e: print(f"o_O Exercise 3 Error: {e}")
        
    if passed == 3:
        print("\n(*^▽^*) YOU ARE READY FOR THE LOG PARSER QUEST!")
