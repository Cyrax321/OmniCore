"""
=========================================================
🛡️ THE CYBER-SECURITY MASTER AUDIT
=========================================================
GOAL: Combine ALL Foundation + Intermediate Core concepts.
=========================================================
"""

def audit_system(login_logs):
    """
    MISSION: Count how many times 'status' was 'FAIL'.
    
    DATA Structure: login_logs is a LIST of DICTIONARIES.
    Example: [
        {"user": "cyrax", "status": "SUCCESS"},
        {"user": "bot", "status": "FAIL"},
        {"user": "guest", "status": "FAIL"}
    ]
    
    EXPECTED RETURN: An integer (e.g., 2)
    """
    # 1. Create a variable to hold the 'failed_count' starting at 0
    
    # 2. Loop through the login_logs (for...in...)
    
    # 3. Check IF the current log["status"] is equal to "FAIL"
    
    # 4. If it matches, add 1 to your failed_count
    
    # 5. Return the final count after the loop ends
    pass


# ==========================================
# TEST RUNNER
# ==========================================
if __name__ == "__main__":
    logs = [
        {"user": "cyrax", "status": "SUCCESS"},
        {"user": "bot", "status": "FAIL"},
        {"user": "attacker", "status": "FAIL"},
        {"user": "it_admin", "status": "SUCCESS"},
        {"user": "guest", "status": "FAIL"}
    ]
    
    result = audit_system(logs)
    
    if result == 3:
        print("<3 MASTER AUDIT PASSED! You are a Python Adept.")
    else:
        print(f":( AUDIT FAILED. Expected 3, got {result}")
