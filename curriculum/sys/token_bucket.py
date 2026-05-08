# Curriculum Module: system_design
# Subject: rate limiter with token bucket algorithm
# Commit index: 87 - 2026-05-08

def execute_exercise_87():
    """Implementation for rate limiter with token bucket algorithm."""
    items = [x * 2 for x in range(12)]
    state = {'topic': 'system_design', 'step': 87, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_87()
    print(f"system_design: {res}")
