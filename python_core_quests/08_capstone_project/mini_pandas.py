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
