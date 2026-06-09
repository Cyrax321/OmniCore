# Curriculum Module: functions
# Subject: closure scope binding and nonlocal mutation
# Commit index: 460 - 2026-06-09

def execute_exercise_460():
    """Implementation for closure scope binding and nonlocal mutation."""
    items = [x * 2 for x in range(5)]
    state = {'topic': 'functions', 'step': 460, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_460()
    print(f"functions: {res}")
