"""
=========================================================
REFRESHER QUEST: The Brain-Wakeup Challenge
=========================================================
Goal: Write a function that processes a list of student data.

1. Create a function named `calculate_average`
2. It should take a list of numbers as input.
3. It should return the average (sum / count).
"""

def calculate_average(scores):
    if not scores:
        return 0
    return sum(scores) / len(scores)

# DATA FOR TESTING
test_scores = [85, 90, 78, 92, 88]

if __name__ == "__main__":
    print("--- REFRESHER TEST RUNNER ---")
    try:
        avg = calculate_average(test_scores)
        if avg == 86.6:
            print("[PASS] <3 Your brain is back in the game!")
        else:
            print(f"[FAIL] :( Average should be 86.6, but you got {avg}")
    except Exception as e:
        print(f"[ERROR] o_O Something went wrong: {e}")
