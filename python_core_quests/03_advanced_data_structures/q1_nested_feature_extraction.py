"""
=========================================================
Quest: Nested Feature Extraction (JSON parsing)
Topic: Advanced Data Structures
Difficulty: Medium
=========================================================

INSTRUCTIONS:
You are pulling data from a dummy Twitter API. The data structure is a dictionary 
containing lists of dictionaries. 
You are given `data` and a string `user_id`.
Find the user by their ID, and return a list of all their 'hashtags'.
If the user isn't found, return an empty list.

EXAMPLES:
1) Input: data = {"users": [{"id": "u1", "tags": ["#ml", "#ai"]}, {"id": "u2", "tags": ["#python"]}]}, user_id = "u2"
   Expected: ["#python"]

PREREQUISITES TO STUDY:
- Dictionary access (`dict["key"]`)
- Lists of Dictionaries
- For loops iterating through objects

HOW TO THINK ABOUT THIS:
1. Extract the main list of users from the `data` dictionary using the key `"users"`.
2. Loop over this list. Every element is itself a dictionary representing a `user`.
3. Check the user's `"id"`. If it matches `user_id`, we found our target.
4. Return that user's `"tags"`. 
5. If the loop ends and you found nothing, return empty list `[]`.

CODING STEPS FOR BEGINNERS:
1. Extract list: `user_list = data["users"]`
2. Loop through users: `for user in user_list:`
3. Check condition inside loop: `if user["id"] == user_id:`
4. Inside condition: `return user["tags"]`
5. At the very bottom outside loop: `return []`
"""

def solve(data, user_id):
    # ==========================================
    # WRITE YOUR CODE HERE
    # ==========================================
    pass


# ==========================================
# TEST RUNNER (Do not modify anything below)
# ==========================================
if __name__ == "__main__":
    sample_data = {
        "users": [
            {"id": "u1", "tags": ["#ml", "#ai"]},
            {"id": "u2", "tags": ["#python", "#pandas"]},
            {"id": "u3", "tags": []}
        ]
    }
    tests = [
        {"input": (sample_data, "u2"), "expected": ["#python", "#pandas"]},
        {"input": (sample_data, "u3"), "expected": []},
        {"input": (sample_data, "u99"), "expected": []}
    ]
    
    passed = 0
    for i, test in enumerate(tests):
        try:
            result = solve(test["input"][0], test["input"][1])
            if result is not None and result == test["expected"]:
                print(f"<3 Test {i+1} Passed!")
                passed += 1
            else:
                print(f":( Test {i+1} Failed. Expected {test['expected']}, got {result}")
        except Exception as e:
            print(f"o_O Test {i+1} Error: {e}")
            
    print(f"\nScore: {passed}/{len(tests)}")
