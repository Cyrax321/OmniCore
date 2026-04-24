"""
=========================================================
🚀 OMNI-AGENDA // MISSION 01: THE TASK LOOP
=========================================================
🔨 BUILD THIS: 
Loop through a list of 10 tasks and print them with numbering.

⚡ UNFAIR ADVANTAGE: 
Learn 10 variations of the 'Counting Loop' pattern.
=========================================================
"""

def solve():
    tasks = [
        "Debug the Matrix", "Audit the Logs", "Optimise the API",
        "Train the Model", "Prune the Tree", "Clean the Data",
        "Deploy the Script", "Draft the Paper", "Review the Code",
        "Unlock God Mode"
    ]
    
    # --- VARIATION 1: THE COUNTER (Traditional) ---
    print("Variation 1: The Manual Counter")
    i = 1
    for task in tasks:
        print(f"{i}. {task}")
        i += 1
    print("-" * 20)

    # --- VARIATION 2: ENUMERATE (The Pythonic Way) ---
    print("Variation 2: Enumerate (Standard)")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
    print("-" * 20)

    # --- VARIATION 3: RANGE & LENGTH (The Index Way) ---
    # WRITE THIS ONE BELOW!
    pass

if __name__ == "__main__":
    solve()
