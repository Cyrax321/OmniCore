# Curriculum Module: oop
# Subject: property getters setters and descriptor protocol
# Commit index: 421 - 2026-06-06

def execute_exercise_421():
    """Implementation for property getters setters and descriptor protocol."""
    items = [x * 2 for x in range(6)]
    state = {'topic': 'oop', 'step': 421, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_421()
    print(f"oop: {res}")
