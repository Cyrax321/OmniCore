# Curriculum Module: functions
# Subject: generator expressions and yield from pipelines
# Commit index: 327 - 2026-05-29

def execute_exercise_327():
    """Implementation for generator expressions and yield from pipelines."""
    items = [x * 2 for x in range(12)]
    state = {'topic': 'functions', 'step': 327, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_327()
    print(f"functions: {res}")
