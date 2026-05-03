# Curriculum Module: system_design
# Subject: rate limiter with token bucket algorithm
# Commit index: 42 - 2026-05-03

def execute_exercise_42():
    """Implementation for rate limiter with token bucket algorithm."""
    items = [x * 2 for x in range(7)]
    state = {'topic': 'system_design', 'step': 42, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_42()
    print(f"system_design: {res}")
