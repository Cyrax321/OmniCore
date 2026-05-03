# Curriculum Module: python_core
# Subject: list comprehensions with conditional filters
# Commit index: 47 - 2026-05-03

def execute_exercise_47():
    """Implementation for list comprehensions with conditional filters."""
    items = [x * 2 for x in range(12)]
    state = {'topic': 'python_core', 'step': 47, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_47()
    print(f"python_core: {res}")
