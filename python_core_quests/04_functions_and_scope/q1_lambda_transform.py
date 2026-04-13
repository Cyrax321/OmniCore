"""
=========================================================
Quest: Lambda Transformers (Map targeting)
Topic: Functions & Scope
Difficulty: Easy
=========================================================

INSTRUCTIONS:
You have a list of raw numerical strings that have whitespace and are currently strings.
Example: `[" 12.5 ", "  3.1 ", " 0.0"]`
Write a function `solve(data)` that uses Python's built-in `map()` function and a `lambda` 
to strip the whitespace and convert them to floats.
Return a list of floats.

EXAMPLES:
1) Input: `[" 12.5 ", "  3.1 ", " 0.0"]`
   Expected: `[12.5, 3.1, 0.0]`

"""

def solve(data):
    # ==========================================
    # WRITE YOUR CODE HERE
    # ==========================================
    pass


# ==========================================
# TEST RUNNER (Do not modify anything below)
# ==========================================
if __name__ == "__main__":
    tests = [
        {"input": [" 12.5 ", "  3.1 ", " 0.0"], "expected": [12.5, 3.1, 0.0]},
        {"input": ["-1.5", " 100.2"], "expected": [-1.5, 100.2]}
    ]
    
    passed = 0
    for i, test in enumerate(tests):
        try:
            result = solve(test["input"])
            if result is not None and result == test["expected"]:
                print(f"✅ Test {i+1} Passed!")
                passed += 1
            else:
                print(f"❌ Test {i+1} Failed. Expected {test['expected']}, got {result}")
        except Exception as e:
            print(f"⚠️ Test {i+1} Error: {e}")
            
    print(f"\nScore: {passed}/{len(tests)}")
