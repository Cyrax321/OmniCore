# Curriculum Module: dp
# Subject: coin change minimum coins with bottom up table
# Commit index: 79 - 2026-05-08

def execute_exercise_79():
    """Implementation for coin change minimum coins with bottom up table."""
    items = [x * 2 for x in range(24)]
    state = {'topic': 'dp', 'step': 79, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_79()
    print(f"dp: {res}")
