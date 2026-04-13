"""
=========================================================
Quest: Safe Value Extractor (Exceptions)
Topic: Exceptions & IO
Difficulty: Easy
=========================================================

INSTRUCTIONS:
You are looping through dirty dataset arrays where some indices don't exist, and some elements are `None`.
Write a function `solve(data, target_index)` that takes a list `data`.
It should try to retrieve the element at `target_index`.
- If the index is out of bounds, catch the `IndexError` and return `"OUT_OF_BOUNDS"`.
- If the element is found but it is `None`, raise a custom `ValueError` with message "NULL_DETECTED".
- Otherwise, return the element.

EXAMPLES:
1) Input: data = [10, 20, 30], target_index = 5
   Expected: "OUT_OF_BOUNDS"
2) Input: data = [10, None, 30], target_index = 1
   Expected: ERROR RAISED (ValueError: "NULL_DETECTED")
3) Input: data = [10, 20, 30], target_index = 0
   Expected: 10

PREREQUISITES TO STUDY:
- `try:` and `except:` blocks
- Catching specific error types (`except IndexError:`)
- Raising custom errors (`raise ValueError("message")`)
- `None` type checking (`is None`)

HOW TO THINK ABOUT THIS:
1. We are attempting something risky: assessing an array index that might not exist. Wrap it in a `try` block.
2. If Python complains it's too big, it throws an `IndexError`. We explicitly catch that and return our fallback string.
3. If it succeeds, check if the value we grabbed is `None`. If it is, forcefully trigger an error using `raise`.
4. If it's valid, return it.

CODING STEPS FOR BEGINNERS:
1. Start `try:` block.
2. Inside `try`, grab the item: `item = data[target_index]`
3. If it's none (`if item is None:`), forcefully throw error: `raise ValueError("NULL_DETECTED")`
4. If it is not none, just `return item`
5. Outside the try, catch the specific failure: `except IndexError:`
6. Inside the except block, `return "OUT_OF_BOUNDS"`
"""

def solve(data, target_index):
    # ==========================================
    # WRITE YOUR CODE HERE
    # ==========================================
    pass


# ==========================================
# TEST RUNNER (Do not modify anything below)
# ==========================================
if __name__ == "__main__":
    tests = [
        {"input": ([10, 20, 30], 5), "expected": "OUT_OF_BOUNDS", "error": False},
        {"input": ([10, None, 30], 1), "expected": "NULL_DETECTED", "error": True},
        {"input": ([10, 20, 30], 0), "expected": 10, "error": False}
    ]
    
    passed = 0
    for i, test in enumerate(tests):
        try:
            result = solve(test["input"][0], test["input"][1])
            if not test["error"]:
                if result == test["expected"]:
                    print(f"<3 Test {i+1} Passed!")
                    passed += 1
                else:
                    print(f":( Test {i+1} Failed. Expected {test['expected']}, got {result}")
            else:
                print(f":( Test {i+1} Failed. Forgot to RAISE a ValueError!")
        except ValueError as e:
            if test["error"] and str(e) == test["expected"]:
                print(f"<3 Test {i+1} Passed! (Properly raised '{e}')")
                passed += 1
            else:
                print(f":( Test {i+1} Failed. Expected ValueError '{test['expected']}', got '{str(e)}'")
        except Exception as e:
            print(f"o_O Test {i+1} Error: {e}")
            
    print(f"\nScore: {passed}/{len(tests)}")
