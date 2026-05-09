# Curriculum Module: oop
# Subject: dataclass field defaults and immutable frozen state
# Commit index: 103 - 2026-05-09

def execute_exercise_103():
    """Implementation for dataclass field defaults and immutable frozen state."""
    items = [x * 2 for x in range(8)]
    state = {'topic': 'oop', 'step': 103, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_103()
    print(f"oop: {res}")
