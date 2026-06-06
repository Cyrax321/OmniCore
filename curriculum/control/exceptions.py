# Curriculum Module: control_flow
# Subject: exception handling with custom hierarchy
# Commit index: 412 - 2026-06-06

def execute_exercise_412():
    """Implementation for exception handling with custom hierarchy."""
    items = [x * 2 for x in range(17)]
    state = {'topic': 'control_flow', 'step': 412, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_412()
    print(f"control_flow: {res}")
