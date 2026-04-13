"""
=========================================================
Quest: ML Model Base Class (OOP)
Topic: Object Oriented Programming
Difficulty: Medium
=========================================================

INSTRUCTIONS:
You are building the core backbone of an ML library like Scikit-Learn.
Build a Python class named `Model`.
1. `__init__(self, name)`: Set the `self.name` to the passed string, and `self.is_trained` to `False`.
2. `fit(self, data)`: A method that takes a list of data. 
   - It sets `self.is_trained = True`
   - It saves the length of the data to `self.data_size`
   - It returns `"Training Complete"`
3. `predict(self)`: A method.
   - If `self.is_trained` is False, return `"Model must be trained first!"`
   - If True, return `"Predicting based on {self.data_size} records"` (use f-string format).

EXAMPLES:
model = Model("MyKNN")
model.predict()   -> "Model must be trained first!"
model.fit([1, 2]) -> "Training Complete"
model.predict()   -> "Predicting based on 2 records"

"""

# ==========================================
# WRITE YOUR CLASS HERE
# ==========================================
pass


# ==========================================
# TEST RUNNER (Do not modify anything below)
# ==========================================
if __name__ == "__main__":
    try:
        model = Model("TestModel")
        
        passed = 0
        if getattr(model, "name", None) == "TestModel" and getattr(model, "is_trained", None) == False:
            print("✅ Test 1 (Init) Passed!")
            passed += 1
        else:
            print("❌ Test 1 (Init) Failed.")
            
        res1 = model.predict()
        if res1 == "Model must be trained first!":
            print("✅ Test 2 (Untrained Predict) Passed!")
            passed += 1
        else:
            print(f"❌ Test 2 (Untrained Predict) Failed. Got: {res1}")

        res2 = model.fit(["data1", "data2", "data3"])
        if res2 == "Training Complete" and getattr(model, "is_trained", None) == True and getattr(model, "data_size", None) == 3:
             print("✅ Test 3 (Fit method) Passed!")
             passed += 1
        else:
             print("❌ Test 3 (Fit method) Failed.")
             
        res3 = model.predict()
        if res3 == "Predicting based on 3 records":
            print("✅ Test 4 (Trained Predict) Passed!")
            passed += 1
        else:
            print(f"❌ Test 4 (Trained Predict) Failed. Got: {res3}")
            
        print(f"\nScore: {passed}/4")

    except NameError:
        print("⚠️ Class 'Model' not defined yet!")
    except Exception as e:
        print(f"⚠️ Test Error: {e}")
