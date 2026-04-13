"""
=========================================================
🏆 CAPSTONE PROJECT: MINI PANDAS 🏆
=========================================================

INSTRUCTIONS:
You are building your own mini-Pandas DataFrame!
Build a class `DataFrame`.

1. `__init__(self, data_dict)`: 
   - Accepts a dictionary of lists (e.g., `{"age": [20, 25], "salary": [50000, 60000]}`).
   - Saves it to `self.data`.

2. `get_column(self, col_name)`:
   - Returns the list associated with `col_name`.
   - If not found, raises a KeyError with "Column not found".

3. `mean(self, col_name)`:
   - Uses `get_column` to get the list, then returns the average (sum / length).

4. `filter_greater_than(self, col_name, value)`:
   - Returns a NEW dictionary representing only the rows where `col_name > value`.
   - E.g. `df.filter_greater_than("age", 22)` -> Returns data dict but indices 0 removed because age[0] is 20.

HOW TO THINK ABOUT THIS:
1. This combines basically everything from Quests 01 to 07!
2. `get_column` is simple dictionary access + a Try/Except or `in` check.
3. `mean()` is basic math and list aggregation.
4. `filter_greater_than` is the tricky one. First, find all the *indices* in the target column where the value is greater than `value`.
5. Then, construct a brand new dictionary, looping over all keys in `self.data`, and building a new list containing only the elements at those valid indices.

CODING STEPS FOR BEGINNERS:
1. `class DataFrame:`
2. `def __init__(self, data_dict): self.data = data_dict`
3. `def get_column(self, col_name):` Check `if col_name not in self.data: raise KeyError(...)`, else `return self.data[col_name]`
4. `def mean(self, col_name):` Call `arr = self.get_column(col_name)`, return `sum(arr)/len(arr)`.
5. `def filter_greater_than(self, col_name, value):`
   - `col = self.get_column(col_name)`
   - Find valid indices using comprehensions: `valid_idx = [i for i, x in enumerate(col) if x > value]`
   - Build a new dict: `new_data = {}`
   - For every key in `self.data`: `new_data[key] = [self.data[key][i] for i in valid_idx]`
   - `return new_data`
"""

# ==========================================
# WRITE YOUR CODE HERE
# ==========================================
pass

# ==========================================
# TEST RUNNER (Do not modify anything below)
# ==========================================
if __name__ == "__main__":
    try:
        raw_data = {"age": [20, 25, 30], "salary": [50000, 60000, 100000]}
        df = DataFrame(raw_data)
        
        passed = 0
        if df.get_column("age") == [20, 25, 30]:
            print("✅ Test 1 (get_column) Passed!")
            passed += 1
        else:
            print("❌ Test 1 Failed.")
            
        try:
            df.get_column("invalid")
            print("❌ Test 2 (KeyError) Failed. Didn't raise error.")
        except KeyError:
             print("✅ Test 2 (KeyError on bad column) Passed!")
             passed += 1
             
        if df.mean("salary") == 70000.0:
            print("✅ Test 3 (mean) Passed!")
            passed += 1
        else:
            print(f"❌ Test 3 Failed. Got {df.mean('salary')}")
            
        filtered = df.filter_greater_than("age", 22)
        expected = {"age": [25, 30], "salary": [60000, 100000]}
        if filtered == expected:
            print("✅ Test 4 (filter_greater_than) Passed!")
            passed += 1
        else:
            print(f"❌ Test 4 Failed. Expected {expected}, got {filtered}")
        
        print(f"\nScore: {passed}/4!")

    except NameError:
        print("⚠️ Class 'DataFrame' not defined!")
    except Exception as e:
        print(f"⚠️ Test Error: {e}")
