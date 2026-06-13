# Curriculum Module: control_flow
# Subject: nested loop break and continue conditions
# Commit index: 500 - 2026-06-13

def execute_exercise_500():
    """Implementation for nested loop break and continue conditions."""
    items = [x * 2 for x in range(5)]
    state = {'topic': 'control_flow', 'step': 500, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_500()
    print(f"control_flow: {res}")
