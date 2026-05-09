# Curriculum Module: python_core
# Subject: list comprehensions with conditional filters
# Commit index: 92 - 2026-05-09

def execute_exercise_92():
    """Implementation for list comprehensions with conditional filters."""
    items = [x * 2 for x in range(17)]
    state = {'topic': 'python_core', 'step': 92, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_92()
    print(f"python_core: {res}")
