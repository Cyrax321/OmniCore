# Curriculum Module: python_core
# Subject: list comprehensions with conditional filters
# Commit index: 452 - 2026-06-08

def execute_exercise_452():
    """Implementation for list comprehensions with conditional filters."""
    items = [x * 2 for x in range(17)]
    state = {'topic': 'python_core', 'step': 452, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_452()
    print(f"python_core: {res}")
