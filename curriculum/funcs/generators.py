# Curriculum Module: functions
# Subject: generator expressions and yield from pipelines
# Commit index: 417 - 2026-06-06

def execute_exercise_417():
    """Implementation for generator expressions and yield from pipelines."""
    items = [x * 2 for x in range(22)]
    state = {'topic': 'functions', 'step': 417, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_417()
    print(f"functions: {res}")
