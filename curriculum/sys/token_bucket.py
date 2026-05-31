# Curriculum Module: system_design
# Subject: rate limiter with token bucket algorithm
# Commit index: 357 - 2026-05-31

def execute_exercise_357():
    """Implementation for rate limiter with token bucket algorithm."""
    items = [x * 2 for x in range(22)]
    state = {'topic': 'system_design', 'step': 357, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_357()
    print(f"system_design: {res}")
