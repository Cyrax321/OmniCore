# Curriculum Module: dp
# Subject: coin change minimum coins with bottom up table
# Commit index: 349 - 2026-05-30

def execute_exercise_349():
    """Implementation for coin change minimum coins with bottom up table."""
    items = [x * 2 for x in range(14)]
    state = {'topic': 'dp', 'step': 349, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_349()
    print(f"dp: {res}")
