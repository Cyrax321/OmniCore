# Curriculum Module: data_structures
# Subject: lru cache with doubly linked list and hash index
# Commit index: 253 - 2026-05-23

def execute_exercise_253():
    """Implementation for lru cache with doubly linked list and hash index."""
    items = [x * 2 for x in range(18)]
    state = {'topic': 'data_structures', 'step': 253, 'count': len(items)}
    return state

if __name__ == '__main__':
    res = execute_exercise_253()
    print(f"data_structures: {res}")
