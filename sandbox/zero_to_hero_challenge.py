"""
=========================================================
⚡ THE ZERO-TO-HERO CHALLENGE: OMNI-CYBER PROTOCOOL
=========================================================
MISSION: Protect the server by completing all 4 Stages.
=========================================================
"""

# --- STAGE 1: VARIABLES & MATH ---
def calculate_threat(failed_attempts, password_score):
    """
    GOAL: Calculate the 'Threat Score'.
    Logic: (failed_attempts * 10) - password_score
    Return: The score (integer)
    """
    Threat_score = (failed_attempts * 10) - password_score
    return Threat_score
    pass

# --- STAGE 2: LISTS & LOGIC ---
def is_ip_blocked(ip_address, blocked_ips):
    """
    GOAL: Check if the 'ip_address' is in the 'blocked_ips' list.
    Return: True if it is blocked, False if it is safe.
    """
    if ip_address in blocked_ips :
        return True
    else :
        return False
    pass

# --- STAGE 3: LOOPS & DICTS ---
def find_admin_tags(user_database):
    """
    GOAL: Look through a LIST of DICTIONARIES. 
    Find the user with role "ADMIN" and return their "tags".
    DATA: user_database = [{"name": "cyrax", "role": "USER", "tags": []}, {"name": "neo", "role": "ADMIN", "tags": ["#root"]}]
    Return: The tags list (e.g. ["#root"])
    """
    pass

# --- STAGE 4: THE MASTER PROTOCOL (SYNTHESIS) ---
def run_protocol(failed_attempts, password_score, ip, blocked_list, db):
    """
    THIS IS THE FINAL BOSS. Use the functions above!
    1. Calculate threat score using calculate_threat().
    2. If threat score is > 50, return "HIGH THREAT".
    3. Check if IP is blocked using is_ip_blocked().
    4. If IP is blocked, return "ACCESS DENIED".
    5. If safe, find the admin tags using find_admin_tags() and return them.
    """
    calculate_threat(failed_attempts,password_score)
    if Threat_score > 50 :
        return "HIGH THREAT"
    is_ip_blocked()


        
    pass


# ==========================================
# AUTOMATED TEST RUNNER (DO NOT MODIFY)
# ==========================================
if __name__ == "__main__":
    passed = 0
    
    # Test 1: Math
    if calculate_threat(5, 10) == 40:
        print("<3 Stage 1 Passed!")
        passed += 1
    
    # Test 2: Lists
    if is_ip_blocked("1.1.1.1", ["8.8.8.8", "1.1.1.1"]) == True:
        print("<3 Stage 2 Passed!")
        passed += 1
        
    # Test 3: Loops & Dicts
    db_sample = [{"id": 0, "role": "USER", "tags": []}, {"id": 1, "role": "ADMIN", "tags": ["#secure"]}]
    if find_admin_tags(db_sample) == ["#secure"]:
        print("<3 Stage 3 Passed!")
        passed += 1
        
    # Test 4: Master Synthesis
    if run_protocol(1, 10, "9.9.9.9", ["1.2.3.4"], db_sample) == ["#secure"]:
        if run_protocol(10, 5, "9.9.9.9", ["1.2.3.4"], db_sample) == "HIGH THREAT":
            print("<3 STAGE 4 PASSED! SYSTEM SECURE.")
            passed += 1

    if passed == 4:
        print("\n(★‿★) OMNI-HERO STATUS ACHIEVED. You are ready for any AI challenge.")
    else:
        print(f"\nScore: {passed}/4. One or more sectors are compromised!")
