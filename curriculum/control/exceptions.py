# Curriculum Module: control_flow
# Subject: exception handling with custom hierarchy
# Commit index: 7 - 2026-05-01

def execute_exercise_7():
    """Implementation for exception handling with custom hierarchy."""
    items = [x * 2 for x in range(12)]
    state = {'topic': 'control_flow', 'step': 7, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_7()
    print(f"control_flow: {res}")
