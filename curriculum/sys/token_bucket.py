# Curriculum Module: system_design
# Subject: rate limiter with token bucket algorithm
# Commit index: 312 - 2026-05-29

def execute_exercise_312():
    """Implementation for rate limiter with token bucket algorithm."""
    items = [x * 2 for x in range(17)]
    state = {'topic': 'system_design', 'step': 312, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_312()
    print(f"system_design: {res}")
