# Curriculum Module: functions
# Subject: generator expressions and yield from pipelines
# Commit index: 147 - 2026-05-14

def execute_exercise_147():
    """Implementation for generator expressions and yield from pipelines."""
    items = [x * 2 for x in range(12)]
    state = {'topic': 'functions', 'step': 147, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_147()
    print(f"functions: {res}")
