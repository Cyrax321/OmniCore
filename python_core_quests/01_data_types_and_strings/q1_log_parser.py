"""
=========================================================
Quest: Log Parser (Text Cleaning)
Topic: Data Types & Strings
Difficulty: Easy
=========================================================

INSTRUCTIONS:
In ML text cleaning, strings need deep parsing.
You are given a raw server log string formatted exactly like this:
"ERROR_CODE: 404 | MSG: NOT FOUND | IP: 192.168.1.1"

Your goal is to parse this string and return the ERROR_CODE as an integer.

EXAMPLES:
1) Input: "ERROR_CODE: 404 | MSG: NOT FOUND | IP: 192.168.1.1"
   Expected: 404 (as an integer)
2) Input: "ERROR_CODE: 500 | MSG: CRASH | IP: 10.0.0.1"
   Expected: 500 (as an integer)

"""

def solve(log_string):
    # ==========================================
    # WRITE YOUR CODE HERE
    # ==========================================
    pass


# ==========================================
# TEST RUNNER (Do not modify anything below)
# ==========================================
if __name__ == "__main__":
    tests = [
        {"input": "ERROR_CODE: 404 | MSG: NOT FOUND | IP: 192.168.1.1", "expected": 404},
        {"input": "ERROR_CODE: 500 | MSG: CRASH | IP: 10.0.0.1", "expected": 500},
        {"input": "ERROR_CODE: 200 | MSG: OK | IP: 127.0.0.1", "expected": 200}
    ]
    
    passed = 0
    for i, test in enumerate(tests):
        try:
            result = solve(test["input"])
            if result is not None and result == test["expected"] and isinstance(result, int):
                print(f"✅ Test {i+1} Passed!")
                passed += 1
            else:
                print(f"❌ Test {i+1} Failed. Expected INT {test['expected']}, got {type(result)} {result}")
        except Exception as e:
            print(f"⚠️ Test {i+1} Error: {e}")
            
    print(f"\nScore: {passed}/{len(tests)}")
