# Curriculum Module: functions
# Subject: generator expressions and yield from pipelines
# Commit index: 102 - 2026-05-09

def execute_exercise_102():
    """Implementation for generator expressions and yield from pipelines."""
    items = [x * 2 for x in range(7)]
    state = {'topic': 'functions', 'step': 102, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_102()
    print(f"functions: {res}")
