# Curriculum Module: python_core
# Subject: list comprehensions with conditional filters
# Commit index: 407 - 2026-06-06

def execute_exercise_407():
    """Implementation for list comprehensions with conditional filters."""
    items = [x * 2 for x in range(12)]
    state = {'topic': 'python_core', 'step': 407, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_407()
    print(f"python_core: {res}")
