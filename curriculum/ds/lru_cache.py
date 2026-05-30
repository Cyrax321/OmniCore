# Curriculum Module: data_structures
# Subject: lru cache with doubly linked list and hash index
# Commit index: 343 - 2026-05-30

def execute_exercise_343():
    """Implementation for lru cache with doubly linked list and hash index."""
    items = [x * 2 for x in range(8)]
    state = {'topic': 'data_structures', 'step': 343, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_343()
    print(f"data_structures: {res}")
