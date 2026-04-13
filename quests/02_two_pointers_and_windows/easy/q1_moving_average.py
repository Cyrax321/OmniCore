"""
=========================================================
Quest: Moving Average (Time Series)
Topic: Two Pointers & Sliding Window
Difficulty: Easy
=========================================================

INSTRUCTIONS:
A moving average is used to smooth out short-term fluctuations in time series data (e.g. stock prices, or loss patterns in ML loops).
Given an array of floats `data` and an integer `window_size`, return an array representing the moving average of size `window_size`.

If window_size is larger than the data length, return an empty array.

EXAMPLES:
1) Input: data = [1.0, 2.0, 3.0, 4.0], window_size = 2
   Averages: [(1+2)/2, (2+3)/2, (3+4)/2]
   Expected: [1.5, 2.5, 3.5]
HOW TO THINK ABOUT THIS:
1. A sliding window looks at a continuous block of array elements at once.
2. Start by calculating the sum of the very first window (e.g., indices 0 to window_size - 1).
3. Instead of recalculating the entire sum for the next window, just subtract the element that "fell off" the left side and add the element that "entered" on the right.
4. Calculate the average for each window and append it to your results array.

"""

def solve(data, window_size):
    # ==========================================
    # WRITE YOUR CODE HERE
    # ==========================================
    pass


# ==========================================
# TEST RUNNER (Do not modify anything below)
# ==========================================
if __name__ == "__main__":
    tests = [
        {"input": ([1.0, 2.0, 3.0, 4.0], 2), "expected": [1.5, 2.5, 3.5]},
        {"input": ([10, 20, 30], 3), "expected": [20.0]},
        {"input": ([5.0, 5.0, 5.0], 1), "expected": [5.0, 5.0, 5.0]},
        {"input": ([1.0, 2.0], 5), "expected": []}
    ]
    
    passed = 0
    for i, test in enumerate(tests):
        try:
            result = solve(test["input"][0], test["input"][1])
            if result == test["expected"]:
                print(f"✅ Test {i+1} Passed!")
                passed += 1
            else:
                print(f"❌ Test {i+1} Failed. Expected {test['expected']}, got {result}")
        except Exception as e:
            print(f"⚠️ Test {i+1} Error: {e}")
            
    print(f"\nScore: {passed}/{len(tests)}")
