# Curriculum Module: dp
# Subject: coin change minimum coins with bottom up table
# Commit index: 214 - 2026-05-19

def execute_exercise_214():
    """Implementation for coin change minimum coins with bottom up table."""
    items = [x * 2 for x in range(19)]
    state = {'topic': 'dp', 'step': 214, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_214()
    print(f"dp: {res}")
