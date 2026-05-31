# Curriculum Module: control_flow
# Subject: pattern matching with structural match case
# Commit index: 366 - 2026-05-31

def execute_exercise_366():
    """Implementation for pattern matching with structural match case."""
    items = [x * 2 for x in range(11)]
    state = {'topic': 'control_flow', 'step': 366, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_366()
    print(f"control_flow: {res}")
