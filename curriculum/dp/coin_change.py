# Curriculum Module: dp
# Subject: coin change minimum coins with bottom up table
# Commit index: 124 - 2026-05-10

def execute_exercise_124():
    """Implementation for coin change minimum coins with bottom up table."""
    items = [x * 2 for x in range(9)]
    state = {'topic': 'dp', 'step': 124, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_124()
    print(f"dp: {res}")
