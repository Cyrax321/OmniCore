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

PREREQUISITES TO STUDY:
- String Methods (`.split()`)
- Indexing into arrays
- Casting types into Integers (`int()`)

HOW TO THINK ABOUT THIS:
1. The string has different chunks separated by `" | "`.
2. The exact chunk we care about is the first one: `"ERROR_CODE: 404"`.
3. Within that first chunk, we want the number after the `: `
4. Once we slice out `"404"`, it is still a string. We must convert it to an integer.

CODING STEPS FOR BEGINNERS:
1. Split the massive string by `" | "` and save it to a variable: `chunks = log.split(" | ")`
2. Grab the first chunk (index 0): `first_chunk = chunks[0]`
3. Split the first chunk by `": "`: `parts = first_chunk.split(": ")`
4. The second of those two new parts is the number (index 1): `number_string = parts[1]`
5. Convert to an int and return: `return int(number_string)`
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
                print(f"🌸 Test {i+1} Passed!")
                passed += 1
            else:
                print(f"(╥﹏╥) Test {i+1} Failed. Expected INT {test['expected']}, got {type(result)} {result}")
        except Exception as e:
            print(f"(・_・;) Test {i+1} Error: {e}")
            
    print(f"\nScore: {passed}/{len(tests)}")
