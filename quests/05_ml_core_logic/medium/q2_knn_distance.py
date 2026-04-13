"""
=========================================================
Quest: K-Nearest Neighbors (KNN) Distance sorting
Topic: ML Core Logic
Difficulty: Medium
=========================================================

INSTRUCTIONS:
In K-Nearest Neighbors, we find the 'K' points closest to our target point.
Given a list of points (each is an [x, y] coordinate pair), and a target point [target_x, target_y],
return the `k` closest points based on Euclidean distance.

Euclidean Distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)

Return the `k` closest points in ascending order of distance. If there's a tie, order doesn't matter.

EXAMPLES:
1) Input: points = [[1, 3], [-2, 2]], target = [0, 0], k = 1
   Expected: [[-2, 2]]
   Reason: Dist to [1, 3] is sqrt(10) = 3.16. Dist to [-2, 2] is sqrt(8) = 2.82. [-2, 2] is closer!
HOW TO THINK ABOUT THIS:
1. You need to calculate the distance from every point in the list to the target point.
2. Create a list of tuples or sub-lists where each element looks like: `(distance, point)`.
3. Loop through `points`, compute the Euclidean distance to `target`, and append it to your list.
4. Sort this new list. Since the distance is the first element, Python will sort by distance automatically!
5. Extract and return just the `point` coordinates from the first `k` elements of your sorted list.

"""
import math

def solve(points, target, k):
    # ==========================================
    # WRITE YOUR CODE HERE
    # ==========================================
    pass


# ==========================================
# TEST RUNNER (Do not modify anything below)
# ==========================================
if __name__ == "__main__":
    tests = [
        {"input": ([[1, 3], [-2, 2]], [0, 0], 1), "expected": [[-2, 2]]},
        {"input": ([[3, 3], [5, -1], [-2, 4]], [0, 0], 2), "expected": [[3, 3], [-2, 4]]},
        {"input": ([[0, 1], [1, 0]], [0, 0], 2), "expected": [[0, 1], [1, 0]]}
    ]
    
    passed = 0
    for i, test in enumerate(tests):
        try:
            points, target, k = test["input"]
            result = solve(points, target, k)
            
            # Use sets of tuples to compare if order doesn't strictly matter for ties
            # or simply sort them if sorting is part of the validation
            
            if result is not None and sorted([tuple(x) for x in result]) == sorted([tuple(x) for x in test["expected"]]):
                print(f"✅ Test {i+1} Passed!")
                passed += 1
            else:
                print(f"❌ Test {i+1} Failed. Expected {test['expected']}, got {result}")
        except Exception as e:
            print(f"⚠️ Test {i+1} Error: {e}")
            
    print(f"\nScore: {passed}/{len(tests)}")
