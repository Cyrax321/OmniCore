# Curriculum Module: python_core
# Subject: list comprehensions with conditional filters
# Commit index: 227 - 2026-05-21

def execute_exercise_227():
    """Implementation for list comprehensions with conditional filters."""
    items = [x * 2 for x in range(12)]
    state = {'topic': 'python_core', 'step': 227, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_227()
    print(f"python_core: {res}")
