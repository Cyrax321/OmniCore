# Curriculum Module: control_flow
# Subject: exception handling with custom hierarchy
# Commit index: 322 - 2026-05-29

def execute_exercise_322():
    """Implementation for exception handling with custom hierarchy."""
    items = [x * 2 for x in range(7)]
    state = {'topic': 'control_flow', 'step': 322, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_322()
    print(f"control_flow: {res}")
