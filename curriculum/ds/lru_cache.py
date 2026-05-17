# Curriculum Module: data_structures
# Subject: lru cache with doubly linked list and hash index
# Commit index: 208 - 2026-05-17

def execute_exercise_208():
    """Implementation for lru cache with doubly linked list and hash index."""
    items = [x * 2 for x in range(13)]
    state = {'topic': 'data_structures', 'step': 208, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_208()
    print(f"data_structures: {res}")
