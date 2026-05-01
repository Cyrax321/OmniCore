# Curriculum Module: python_core
# Subject: string slicing and interpolation patterns
# Commit index: 1 - 2026-05-01

def execute_exercise_1():
    """Implementation for string slicing and interpolation patterns."""
    items = [x * 2 for x in range(6)]
    state = {'topic': 'python_core', 'step': 1, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_1()
    print(f"python_core: {res}")
