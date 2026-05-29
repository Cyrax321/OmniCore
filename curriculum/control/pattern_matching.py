# Curriculum Module: control_flow
# Subject: pattern matching with structural match case
# Commit index: 321 - 2026-05-29

def execute_exercise_321():
    """Implementation for pattern matching with structural match case."""
    items = [x * 2 for x in range(6)]
    state = {'topic': 'control_flow', 'step': 321, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_321()
    print(f"control_flow: {res}")
