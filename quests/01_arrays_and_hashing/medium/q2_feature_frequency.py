"""
=========================================================
Quest: Feature Frequency Counter (Top K Frequent)
Topic: Arrays & Hashing
Difficulty: Medium
=========================================================

INSTRUCTIONS:
In NLP (Natural Language Processing), finding the most common tokens/words is essential.
Given an integer array `data` and an integer `k`, return the `k` most frequent elements.
You may return the answer in any order.

EXAMPLES:
1) Input: data = [1, 1, 1, 2, 2, 3], k = 2
   Expected: [1, 2] (or [2, 1])
2) Input: data = [1], k = 1
   Expected: [1]
"""

def solve(data, k):
    # ==========================================
    # WRITE YOUR CODE HERE
    # ==========================================
    pass


# ==========================================
# TEST RUNNER (Do not modify anything below)
# ==========================================
if __name__ == "__main__":
    tests = [
        {"input": ([1, 1, 1, 2, 2, 3], 2), "expected": {1, 2}},
        {"input": ([1], 1), "expected": {1}},
        {"input": ([4, 4, 4, 4, 5, 5, 6, 6, 6, 6, 6], 1), "expected": {6}},
        {"input": ([7, 8, 9, 7, 8, 9, 7, 8, 9], 3), "expected": {7, 8, 9}}
    ]
    
    passed = 0
    for i, test in enumerate(tests):
        try:
            # We unpack the tuple input
            result = solve(test["input"][0], test["input"][1])
            # We use sets for comparison as order doesn't matter
            if result is not None and set(result) == test["expected"]:
                print(f"✅ Test {i+1} Passed!")
                passed += 1
            else:
                print(f"❌ Test {i+1} Failed. Expected elements {test['expected']}, got {result}")
        except Exception as e:
            print(f"⚠️ Test {i+1} Error: {e}")
            
    print(f"\nScore: {passed}/{len(tests)}")
