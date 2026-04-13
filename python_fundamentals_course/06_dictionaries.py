"""
=========================================================
LESSON 6: Dictionaries (Key-Value Pairs)
=========================================================

1. WHAT IS A DICTIONARY?
While a List `[]` stores items in a specific numbered order, a Dictionary `{}` stores items using Names (called "Keys").
They look like actual real-life dictionaries: you look up a word, and get the definition.

    player = {
        "name": "Cyrax",
        "level": 99,
        "is_alive": True
    }

2. READING DICTIONARIES
You don't grab index `0`. You grab the literal key!
    print(player["name"])  # Prints "Cyrax"

3. UPDATING DICTIONARIES
You can easily change values or add completely new keys.
    player["level"] = 100       # Updates an existing key
    player["gold"] = 500        # Creates a brand new key!

=========================================================
YOUR TURN (PRACTICE)
=========================================================
"""

def practice_one():
    # TODO:
    # Look at the user_data below. 
    user_data = {
        "email": "cyrax@mail.com",
        "login_count": 5
    }
    # Using dictionary targeting, return their email string!
    pass

def practice_two():
    # TODO:
    # Look at the player below.
    player = {"health": 50}
    # Increase their "health" key to 100! (e.g. player["health"] = ...)
    # Return the whole player dictionary.
    pass


# ==========================================
# TEST RUNNER (Do not modify!)
# ==========================================
if __name__ == "__main__":
    passed = 0
    try:
        if practice_one() == "cyrax@mail.com":
            print("<3 Practice 1 Passed! Reading dictionary keys.")
            passed += 1
        else: print(":( Practice 1 Failed.")
    except Exception: pass

    try:
        res = practice_two()
        if type(res) == dict and res.get("health") == 100:
            print("<3 Practice 2 Passed! Updating dictionary keys.")
            passed += 1
        else: print(":( Practice 2 Failed.")
    except Exception: pass
    
    if passed == 2:
        print("\n(*^▽^*) PERFECT! Dictionaries are how ALL internet APIs transfer data (JSON).")
