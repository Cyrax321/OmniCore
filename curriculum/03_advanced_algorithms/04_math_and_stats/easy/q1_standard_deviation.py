"""
=========================================================
Quest: Standard Deviation
Topic: Math & Stats
Difficulty: Easy
=========================================================

INSTRUCTIONS:
Standard distribution helps us understand how spread out our data is.
Given an array of floats, calculate the standard deviation.
1. Find the mean (average).
2. For each number, subtract the mean and square the result (the squared difference).
3. Find the mean of those squared differences (this is the variance).
4. Take the square root of the variance.

You may use `math.sqrt()`.

EXAMPLES:
1) Input: [2.0, 4.0, 4.0, 4.0, 5.0, 5.0, 7.0, 9.0]
   Expected: Approx 2.0
PREREQUISITES TO STUDY:
- Exponents in Python (`** 2`)
- Appending items to arrays (`.append()`)
- Iterating with variables
- Importing libraries (`import math` and `math.sqrt()`)

HOW TO THINK ABOUT THIS:
1. Code this sequentially following the mathematical steps.
2. Step A: Compute the mean by summing the array and dividing by its length.
3. Step B: Create a new array (or running sum) of the squared differences: `(x - mean) ** 2` for each `x`.
4. Step C: Find the mean of those squared differences (variance).
5. Step D: Return the square root of that variance.

CODING STEPS FOR BEGINNERS:
1. Find length: `n = len(data)`
2. Calculate the mean: `mean = sum(data) / n`
3. Prepare a list for squared differences: `squared_diffs = []`
4. Loop through the data: `for x in data:`
5. Inside that loop:
   `diff = x - mean`
   `squared = diff ** 2`
   `squared_diffs.append(squared)`
6. Find variance: `variance = sum(squared_diffs) / n`
7. Return standard deviation: `return math.sqrt(variance)`
"""
import math

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
        {"input": [2.0, 4.0, 4.0, 4.0, 5.0, 5.0, 7.0, 9.0], "expected": 2.0},
        {"input": [1.0, 2.0, 3.0], "expected": 0.816496580927726},
        {"input": [5.0, 5.0, 5.0], "expected": 0.0}
    ]
    
    passed = 0
    for i, test in enumerate(tests):
        try:
            result = solve(test["input"])
            # Using math.isclose to handle float precision issues
            if result is not None and math.isclose(result, test["expected"], rel_tol=1e-5):
                print(f"<3 Test {i+1} Passed!")
                passed += 1
            else:
                print(f":( Test {i+1} Failed. Expected {test['expected']}, got {result}")
        except Exception as e:
            print(f"o_O Test {i+1} Error: {e}")
            
    print(f"\nScore: {passed}/{len(tests)}")
