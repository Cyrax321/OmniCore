# Curriculum Module: control_flow
# Subject: nested loop break and continue conditions
# Commit index: 365 - 2026-05-31

def execute_exercise_365():
    """Implementation for nested loop break and continue conditions."""
    items = [x * 2 for x in range(10)]
    state = {'topic': 'control_flow', 'step': 365, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_365()
    print(f"control_flow: {res}")
