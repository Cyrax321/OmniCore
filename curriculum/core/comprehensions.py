# Curriculum Module: python_core
# Subject: list comprehensions with conditional filters
# Commit index: 497 - 2026-06-13

def execute_exercise_497():
    """Implementation for list comprehensions with conditional filters."""
    items = [x * 2 for x in range(22)]
    state = {'topic': 'python_core', 'step': 497, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_497()
    print(f"python_core: {res}")
