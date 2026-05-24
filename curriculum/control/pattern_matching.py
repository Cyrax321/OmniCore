# Curriculum Module: control_flow
# Subject: pattern matching with structural match case
# Commit index: 276 - 2026-05-24

def execute_exercise_276():
    """Implementation for pattern matching with structural match case."""
    items = [x * 2 for x in range(21)]
    state = {'topic': 'control_flow', 'step': 276, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_276()
    print(f"control_flow: {res}")
