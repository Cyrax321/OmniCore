"""
=========================================================
Quest: Matrix Comprehensions
Topic: Pythonic Patterns
Difficulty: Easy
=========================================================

INSTRUCTIONS:
You are given a 2D matrix (a list of lists containing integers).
Write a function `solve(matrix)` that uses a list comprehension to flatten the 2D matrix into a 1D list,
BUT only includes numbers that are strictly greater than 0.

EXAMPLES:
1) Input: [[-1, 2], [0, 4, -5], [9]]
   Expected: [2, 4, 9]

"""

def solve(matrix):
    # ==========================================
    # WRITE YOUR CODE HERE
    # ==========================================
    pass


# ==========================================
# TEST RUNNER (Do not modify anything below)
# ==========================================
if __name__ == "__main__":
    tests = [
        {"input": [[-1, 2], [0, 4, -5], [9]], "expected": [2, 4, 9]},
        {"input": [[0, 0], [-1, -2]], "expected": []},
        {"input": [[10, 20]], "expected": [10, 20]}
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
