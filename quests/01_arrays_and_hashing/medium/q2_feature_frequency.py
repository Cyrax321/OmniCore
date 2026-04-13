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
PREREQUISITES TO STUDY:
- Dictionaries (Key-Value pairs)
- Python's `collections.Counter` module
- Tuples vs Lists
- List Comprehensions (`[x for x in data]`)

HOW TO THINK ABOUT THIS:
1. First, you need to count how many times each element appears. A hash map (dictionary) is perfect for this.
2. Next, you need a way to find the highest counts. 
3. You could sort the dictionary by values, but an even better pattern for "Top K" problems is using a Max-Heap or Bucket Sort.
4. Python's `collections.Counter` handles the counting easily, and `Counter.most_common(k)` uses an internal heap to give you the answer optimally. Try doing it manually first!

CODING STEPS FOR BEGINNERS:
1. Import Counter right above your function: `from collections import Counter`
2. Create a frequency map: `counts = Counter(data)` (Looks like: {1: 3, 2: 2, 3: 1})
3. Find the most common items: `top_k = counts.most_common(k)` (Looks like: [(1, 3), (2, 2)])
4. Use a python list comprehension to easily extract just the keys from those tuples: 
   `result = [item[0] for item in top_k]`
5. Return your `result` list.
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
                print(f"💖 Test {i+1} Passed!")
                passed += 1
            else:
                print(f"🥺 Test {i+1} Failed. Expected elements {test['expected']}, got {result}")
        except Exception as e:
            print(f"🐾 Test {i+1} Error: {e}")
            
    print(f"\nScore: {passed}/{len(tests)}")
