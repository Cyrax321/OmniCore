# Curriculum Module: python_core
# Subject: variables and type casting in python runtime
# Commit index: 180 - 2026-05-16

def execute_exercise_180():
    """Implementation for variables and type casting in python runtime."""
    items = [x * 2 for x in range(5)]
    state = {'topic': 'python_core', 'step': 180, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_180()
    print(f"python_core: {res}")
