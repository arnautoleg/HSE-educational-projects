from collections import deque


def sliding_window_min(a, k):

    result, left, right = [], 0, k
    deque = a
    while len(deque) >= k:
        result.append(min(deque[left:right]))
        deque.pop(0)
    return result
