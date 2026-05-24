# Curriculum Module: python_core
# Subject: list comprehensions with conditional filters
# Commit index: 272 - 2026-05-24

def execute_exercise_272():
    """Implementation for list comprehensions with conditional filters."""
    items = [x * 2 for x in range(17)]
    state = {'topic': 'python_core', 'step': 272, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_272()
    print(f"python_core: {res}")
