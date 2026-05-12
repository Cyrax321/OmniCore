# Curriculum Module: python_core
# Subject: list comprehensions with conditional filters
# Commit index: 137 - 2026-05-12

def execute_exercise_137():
    """Implementation for list comprehensions with conditional filters."""
    items = [x * 2 for x in range(22)]
    state = {'topic': 'python_core', 'step': 137, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_137()
    print(f"python_core: {res}")
