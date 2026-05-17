# Curriculum Module: oop
# Subject: property getters setters and descriptor protocol
# Commit index: 196 - 2026-05-17

def execute_exercise_196():
    """Implementation for property getters setters and descriptor protocol."""
    items = [x * 2 for x in range(21)]
    state = {'topic': 'oop', 'step': 196, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_196()
    print(f"oop: {res}")
