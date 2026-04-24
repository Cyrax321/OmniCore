"""
=========================================================
🧪 NESTED DATA X-RAY DRILLS
=========================================================
GOAL: Learn to "dig" through layers of Dictionaries and Lists.
=========================================================
"""

def drill_1_warehouse(inventory, item_name):
    """
    STRUCTURE: A List of Dictionaries.
    DATA: inventory = [{"name": "Laptop", "price": 1000}, {"name": "Mouse", "price": 50}]
    MISSION: Find the item_name and return its PRICE. If not found, return 0.
    """
    # WRITE CODE HERE
    pass

def drill_2_phone(settings, search_app):
    """
    STRUCTURE: A Dictionary containing a List of Dictionary.
    DATA: settings = {
        "apps": [
            {"title": "Instagram", "version": 2.1},
            {"title": "WhatsApp", "version": 5.0}
        ]
    }
    MISSION: Find the search_app title and return its VERSION. If not found, return -1.
    """
    # WRITE CODE HERE
    pass

def drill_3_cinema(database, movie_title):
    """
    STRUCTURE: A Dictionary containing a Dictionary of Lists! (High Complexity)
    DATA: database = {
        "cinema_a": {
            "movies": ["Batman", "Superman"],
            "rating": 5
        },
        "cinema_b": {
            "movies": ["Inception", "Interstellar"],
            "rating": 4
        }
    }
    MISSION: Find which cinema (key) is playing 'movie_title'.
    HINT: You need to loop through the CINEMAS (keys) and check the "movies" list inside each.
    """
    # WRITE CODE HERE
    pass


# ==========================================
# AUTOMATED TEST RUNNER
# ==========================================
if __name__ == "__main__":
    score = 0
    
    # Drill 1 Test
    inv = [{"name": "Laptop", "price": 1000}, {"name": "Mouse", "price": 50}]
    if drill_1_warehouse(inv, "Mouse") == 50 and drill_1_warehouse(inv, "Pizza") == 0:
        print("<3 Drill 1 Passed!")
        score += 1
    else: print(":( Drill 1 Failed.")

    # Drill 2 Test
    sets = {"apps": [{"title": "Instagram", "version": 2.1}, {"title": "WhatsApp", "version": 5.0}]}
    if drill_2_phone(sets, "Instagram") == 2.1 and drill_2_phone(sets, "TikTok") == -1:
        print("<3 Drill 2 Passed!")
        score += 1
    else: print(":( Drill 2 Failed.")

    # Drill 3 Test
    db = {
        "cinema_a": {"movies": ["Batman", "Superman"]},
        "cinema_b": {"movies": ["Inception", "Interstellar"]}
    }
    if drill_3_cinema(db, "Inception") == "cinema_b" and drill_3_cinema(db, "Batman") == "cinema_a":
        print("<3 Drill 3 Passed!")
        score += 1
    else: print(":( Drill 3 Failed.")

    if score == 3:
        print("\n(★‿★) X-RAY VISION UNLOCKED! You are a Nested Data Master.")
    else:
        print(f"\nScore: {score}/3. The wrappers are still tricky!")
