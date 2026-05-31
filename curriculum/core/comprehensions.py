# Curriculum Module: python_core
# Subject: list comprehensions with conditional filters
# Commit index: 362 - 2026-05-31

def execute_exercise_362():
    """Implementation for list comprehensions with conditional filters."""
    items = [x * 2 for x in range(7)]
    state = {'topic': 'python_core', 'step': 362, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_362()
    print(f"python_core: {res}")
