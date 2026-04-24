"""
=========================================================
⚡ SEARCH PATTERN QUICK-FIRE DRILLS
=========================================================
GOAL: Build muscle memory for (Loop + If + Return).
=========================================================
"""

def find_salary(employees, target_name):
    for person in employees:
        if person["name"] == target_name:
            return person["salary"]

def find_car_color(cars, target_brand):
    for x in cars:
        if x["brand"] == target_brand:
            return x["color"]

def find_stock(storage, target_item):
    for x in storage:
        if x["item"] == target_item:
            return x["qty"]


# ==========================================
# TEST RUNNER
# ==========================================
if __name__ == "__main__":
    score = 0
    
    # Test 1
    emp_list = [{"name": "Cyrax", "salary": 5000}, {"name": "Neo", "salary": 9000}]
    if find_salary(emp_list, "Neo") == 9000:
        print("<3 Drill 1 Passed!")
        score += 1
    
    # Test 2
    car_list = [{"brand": "Tesla", "color": "Red"}, {"brand": "BMW", "color": "Black"}]
    if find_car_color(car_list, "BMW") == "Black":
        print("<3 Drill 2 Passed!")
        score += 1
        
    # Test 3
    store = [{"item": "Apple", "qty": 50}, {"item": "Banana", "qty": 100}]
    if find_stock(store, "Apple") == 50:
        print("<3 Drill 3 Passed!")
        score += 1

    if score == 3:
        print("\n(★‿★) SEARCH MUSCLE MEMORY UNLOCKED.")
    else:
        print(f"\nScore: {score}/3. Keep drilling!")
