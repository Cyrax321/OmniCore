"""
=========================================================
Quest: Activation Function (ReLU vs Sigmoid mock)
Topic: Control Flow & Logic
Difficulty: Easy
=========================================================

INSTRUCTIONS:
Activation functions decide if a neuron fires.
Write a function that takes a number `x` and a string `func_type`.
- If func_type is "relu": return x if x > 0 else 0
- If func_type is "linear": return x
- For any other string: return "Unknown Function"

EXAMPLES:
1) Input: x = -5, func_type = "relu"
   Expected: 0
2) Input: x = 10, func_type = "linear"
   Expected: 10

PREREQUISITES TO STUDY:
- If / Elif / Else statements
- Conditional checking (`>`)
- String equality (`==`)

HOW TO THINK ABOUT THIS:
1. We check `func_type` first.
2. If it is "relu", we do an internal check: is `x` greater than 0? If so, give `x`, else give `0`.
3. If it varies to "linear", we strictly give `x` as is.
4. Finally, an `else` catch-all intercepts bad inputs.

CODING STEPS FOR BEGINNERS:
1. Set up your first condition: `if func_type == "relu":`
2. Inside that block, add another if/else: `if x > 0: return x` otherwise `return 0`
3. Outside, set up the next condition: `elif func_type == "linear":`
4. Inside there, `return x`
5. Finally, `else:`
6. Inside there, `return "Unknown Function"`
"""

def solve(x, func_type):
    # ==========================================
    # WRITE YOUR CODE HERE
    # ==========================================
    pass


# ==========================================
# TEST RUNNER (Do not modify anything below)
# ==========================================
if __name__ == "__main__":
    tests = [
        {"input": (-5, "relu"), "expected": 0},
        {"input": (10, "relu"), "expected": 10},
        {"input": (-5, "linear"), "expected": -5},
        {"input": (4, "sigmoid"), "expected": "Unknown Function"}
    ]
    
    passed = 0
    for i, test in enumerate(tests):
        try:
            result = solve(test["input"][0], test["input"][1])
            if result is not None and result == test["expected"]:
                print(f"💖 Test {i+1} Passed!")
                passed += 1
            else:
                print(f"🥺 Test {i+1} Failed. Expected {test['expected']}, got {result}")
        except Exception as e:
            print(f"🐾 Test {i+1} Error: {e}")
            
    print(f"\nScore: {passed}/{len(tests)}")
