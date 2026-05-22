# Curriculum Module: functions
# Subject: generator expressions and yield from pipelines
# Commit index: 237 - 2026-05-22

def execute_exercise_237():
    """Implementation for generator expressions and yield from pipelines."""
    items = [x * 2 for x in range(22)]
    state = {'topic': 'functions', 'step': 237, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_237()
    print(f"functions: {res}")
