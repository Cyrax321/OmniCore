"""
=========================================================
Quest: Mean Squared Error (MSE)
Topic: ML Core Logic
Difficulty: Easy
=========================================================

INSTRUCTIONS:
Mean Squared Error (MSE) is a common loss function for regression tasks.
Given two lists of numbers of the same length, `actual` and `predicted`:
Calculate the MSE by taking the average of the squared differences between the actual and predicted values.

Formula:
MSE = (1/N) * sum((actual[i] - predicted[i])^2)

EXAMPLES:
1) Input: actual = [1.0, 2.0, 3.0], predicted = [1.0, 2.0, 3.0]
   Expected: 0.0 (Perfect prediction)
2) Input: actual = [1.0, 2.0, 3.0], predicted = [0.0, 1.0, 2.0]
   Expected: 1.0
PREREQUISITES TO STUDY:
- Iterating using indices (`for i in range(len(array))`)
- Accumulator variables updating iteratively (`total += new_value`)
- Accessing dual list values concurrently by index

HOW TO THINK ABOUT THIS:
1. You are comparing two lists index by index. A `for` loop using `range(len(actual))` or the `zip(actual, predicted)` function is ideal here.
2. Keep a running tally of your total error.
3. For each pair of (actual, predicted), subtract them, square the result, and add to your total.
4. Finally, divide the total error by the number of items 'N' to get the "Mean" Squared Error.

CODING STEPS FOR BEGINNERS:
1. Find total units: `n = len(actual)`
2. Initialize sum tally: `total_error = 0`
3. Loop through indices: `for i in range(n):`
4. Inside the loop, find difference: `diff = actual[i] - predicted[i]`
5. Square the difference: `squared_diff = diff ** 2`
6. Add to your total tally: `total_error = total_error + squared_diff`
7. Outside of the loop, compute final average: `mse = total_error / n`
8. `return mse`
"""

def solve(actual, predicted):
    # ==========================================
    # WRITE YOUR CODE HERE
    # ==========================================
    pass


# ==========================================
# TEST RUNNER (Do not modify anything below)
# ==========================================
if __name__ == "__main__":
    tests = [
        {"input": ([1.0, 2.0, 3.0], [1.0, 2.0, 3.0]), "expected": 0.0},
        {"input": ([1.0, 2.0, 3.0], [0.0, 1.0, 2.0]), "expected": 1.0},
        {"input": ([5.0, 10.0], [3.0, 8.0]), "expected": 4.0}
    ]
    
    passed = 0
    for i, test in enumerate(tests):
        try:
            result = solve(test["input"][0], test["input"][1])
            if result is not None and abs(result - test["expected"]) < 1e-5:
                print(f"<3 Test {i+1} Passed!")
                passed += 1
            else:
                print(f":( Test {i+1} Failed. Expected {test['expected']}, got {result}")
        except Exception as e:
            print(f"o_O Test {i+1} Error: {e}")
            
    print(f"\nScore: {passed}/{len(tests)}")
