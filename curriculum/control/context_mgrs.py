# Curriculum Module: control_flow
# Subject: context manager implementation with contextlib
# Commit index: 8 - 2026-05-01

def execute_exercise_8():
    """Implementation for context manager implementation with contextlib."""
    items = [x * 2 for x in range(13)]
    state = {'topic': 'control_flow', 'step': 8, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_8()
    print(f"control_flow: {res}")
