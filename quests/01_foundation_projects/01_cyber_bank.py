"""
=========================================================
PROJECT 1: Cyber-Bank ATM Simulator
=========================================================
MISSION: Create a secure banking terminal.

OBJECTIVES:
1. Initialize a `balance` variable (e.g., 1000) and a `pin` (e.g., "1234").
2. Create a `while` loop that runs until the user chooses to "Exit".
3. Inside the loop, ask the user what they want to do:
   - [1] Check Balance
   - [2] Deposit Money
   - [3] Withdraw Money
   - [4] Exit
4. Use if/elif/else to handle the logic for each choice.
5. BONUS: Ask for the PIN before allowing access!
=========================================================
"""

# --- YOUR CODE STARTS HERE ---

balance = 1000
user_pin = "1234"

print("--- Welcome to OmniCore Cyber-Bank ---")

# Step 1: Secure PIN Check
entered_pin = input("Enter Your PIN: ")

if entered_pin == user_pin:
    print("Access Granted")
    
    # Step 2: Start the loop only if access is granted
    while True:
        print("\n[1] Balance | [2] Deposit | [3] Withdraw | [4] Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print(f"Your Account Balance is: ${balance}")
            
        elif choice == "2":
            try:
                dp = int(input("Enter the amount you want to deposit: "))
                balance += dp
                print(f"Your Deposit has been accepted! New balance: ${balance}")
            except ValueError:
                print("Error: Please enter a valid number.")

        elif choice == "3":
            try:
                wd = int(input("Enter the amount you want to withdraw: "))
                if wd > balance:
                    print("Insufficient funds! Transaction cancelled.")
                else:
                    balance -= wd
                    print(f"Transaction Successful! Your new balance is ${balance}")
            except ValueError:
                print("Error: Please enter a valid number.")

        elif choice == "4":
            print("Goodbye! Stay Secure.")
            break
        
        else:
            print("Invalid Choice.")
else:
    print("Locked Out: Incorrect PIN. Please check your credentials.")
