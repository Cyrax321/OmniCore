"""
=========================================================
Quest: Find Duplicates (Data Cleaning)
Topic: Arrays & Hashing
Difficulty: Easy
=========================================================

INSTRUCTIONS:
In ML datasets, duplicate data can bias your model. 
Given an array of integers representing feature IDs, return True if any value 
appears at least twice in the array, and return False if every element is distinct.

EXAMPLES:
1) Input: [1, 2, 3, 1]
   Expected: True
2) Input: [1, 2, 3, 4]
   Expected: False
3) Input: [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
   Expected: True
PREREQUISITES TO STUDY:
- Python Sets (`set()`, `.add()`, `in` syntax)
- For loops iterating through arrays
- Basic boolean logic (Returning `True` or `False`)

HOW TO THINK ABOUT THIS:
1. The naive approach is a nested loop (compare every item with every other item) -> O(N^2) time.
2. An optimal approach uses a Hash Set. 
3. As you iterate through the list, ask: "Have I seen this number before?"
4. If it's already in the set, you found a duplicate! Return True.
5. If not, add it to the set and keep going.

CODING STEPS FOR BEGINNERS:
1. Initialize an empty set: `seen = set()`
2. Use a loop to go through your list: `for number in data:`
3. Check if it exists in the set: `if number in seen:`
4. Inside the `if`, return True.
5. If the `if` condition isn't met, add the number: `seen.add(number)`
6. If the loop completely finishes without returning True, put `return False` at the very end.
"""

def solve(data):
    # ==========================================
    

    # ==========================================
    pass


# ==========================================
# TEST RUNNER (Do not modify anything below)
# ==========================================
if __name__ == "__main__":
    tests = [
        {"input": [1, 2, 3, 1], "expected": True},
        {"input": [1, 2, 3, 4], "expected": False},
        {"input": [1, 1, 1, 3, 3, 4, 3, 2, 4, 2], "expected": True},
        {"input": [], "expected": False},
        {"input": [89], "expected": False}
    ]
    
    passed = 0
    for i, test in enumerate(tests):
        try:
            result = solve(test["input"])
            if result == test["expected"]:
                print(f"<3 Test {i+1} Passed!")
                passed += 1
            else:
                print(f":( Test {i+1} Failed. Expected {test['expected']}, got {result}")
        except Exception as e:
            print(f"o_O Test {i+1} Error: {e}")
            
    print(f"\nScore: {passed}/{len(tests)}")
