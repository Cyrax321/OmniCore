# Curriculum Module: python_core
# Subject: variables and type casting in python runtime
# Commit index: 360 - 2026-05-31

def execute_exercise_360():
    """Implementation for variables and type casting in python runtime."""
    items = [x * 2 for x in range(5)]
    state = {'topic': 'python_core', 'step': 360, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_360()
    print(f"python_core: {res}")
