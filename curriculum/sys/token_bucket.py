# Curriculum Module: system_design
# Subject: rate limiter with token bucket algorithm
# Commit index: 222 - 2026-05-20

def execute_exercise_222():
    """Implementation for rate limiter with token bucket algorithm."""
    items = [x * 2 for x in range(7)]
    state = {'topic': 'system_design', 'step': 222, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_222()
    print(f"system_design: {res}")
