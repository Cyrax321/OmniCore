# Curriculum Module: functions
# Subject: generator expressions and yield from pipelines
# Commit index: 372 - 2026-06-01

def execute_exercise_372():
    """Implementation for generator expressions and yield from pipelines."""
    items = [x * 2 for x in range(17)]
    state = {'topic': 'functions', 'step': 372, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_372()
    print(f"functions: {res}")
