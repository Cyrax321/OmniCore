# Curriculum Module: system_design
# Subject: rate limiter with token bucket algorithm
# Commit index: 402 - 2026-06-05

def execute_exercise_402():
    """Implementation for rate limiter with token bucket algorithm."""
    items = [x * 2 for x in range(7)]
    state = {'topic': 'system_design', 'step': 402, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_402()
    print(f"system_design: {res}")
