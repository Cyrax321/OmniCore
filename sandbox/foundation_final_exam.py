"""
=========================================================
🏆 FOUNDATION FINAL EXAM (LeetCode Style)
=========================================================
MISSION: Complete all 3 Quests to prove your mastery.
=========================================================
"""

def level_1_filter(numbers):
    ls10 = []
    for i in numbers:
        if i >= 10:
            ls10.append(i)
    return ls10

def level_2_validator(user_db, username):
    if username in user_db and user_db[username] == 'active':
        return True
    else:
        return False

def level_3_boss(a, b, operation):
    """
    QUEST: Build a mini calculator.
    Input: a=10, b=5, operation="add" -> 15
    Input: a=10, b=5, operation="mul" -> 50
    Input: a=10, b=5, operation="div" -> 2.0
    Any other operation -> "Error"
    """
    if operation == "add":
        return a + b
    elif operation == "mul":
        return a * b
    elif operation == "div":
        return a / b
    else:
        return "Error"


# ==========================================
# AUTOMATED TEST RUNNER
# ==========================================
if __name__ == "__main__":
    score = 0
    
    # Test Level 1
    if level_1_filter([5, 12, 3, 18, 10]) == [12, 18, 10]:
        print("<3 Level 1 Passed!")
        score += 1
    else: print(":( Level 1 Failed.")

    # Test Level 2
    db = {"cyrax": "active", "guest": "banned"}
    if level_2_validator(db, "cyrax") == True and level_2_validator(db, "guest") == False and level_2_validator(db, "stranger") == False:
        print("<3 Level 2 Passed!")
        score += 1
    else: print(":( Level 2 Failed.")

    # Test Level 3
    if level_3_boss(10, 5, "add") == 15 and level_3_boss(4, 2, "mul") == 8 and level_3_boss(10, 2, "div") == 5.0 and level_3_boss(1, 1, "??") == "Error":
        print("<3 Level 3 Passed!")
        score += 1
    else: print(":( Level 3 Failed.")

    if score == 3:
        print("\n(★‿★) GOD MODE UNLOCKED! Your foundations are unbreakable.")
    else:
        print(f"\nFinal Score: {score}/3. Keep practicing!")
