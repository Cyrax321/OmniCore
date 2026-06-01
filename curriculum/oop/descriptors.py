# Curriculum Module: oop
# Subject: property getters setters and descriptor protocol
# Commit index: 376 - 2026-06-01

def execute_exercise_376():
    """Implementation for property getters setters and descriptor protocol."""
    items = [x * 2 for x in range(21)]
    state = {'topic': 'oop', 'step': 376, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_376()
    print(f"oop: {res}")
