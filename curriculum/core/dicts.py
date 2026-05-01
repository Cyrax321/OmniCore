# Curriculum Module: python_core
# Subject: dictionary merging and default values
# Commit index: 3 - 2026-05-01

def execute_exercise_3():
    """Implementation for dictionary merging and default values."""
    items = [x * 2 for x in range(8)]
    state = {'topic': 'python_core', 'step': 3, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_3()
    print(f"python_core: {res}")
