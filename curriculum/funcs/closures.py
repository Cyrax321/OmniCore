# Curriculum Module: functions
# Subject: closure scope binding and nonlocal mutation
# Commit index: 280 - 2026-05-24

def execute_exercise_280():
    """Implementation for closure scope binding and nonlocal mutation."""
    items = [x * 2 for x in range(5)]
    state = {'topic': 'functions', 'step': 280, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_280()
    print(f"functions: {res}")
