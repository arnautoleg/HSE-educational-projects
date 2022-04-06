from collections import deque

def sliding_window_min(a, k):
    Qi = deque()
    result = []
    for i in range(k):
        while Qi and a[i] < a[Qi[-1]]:
            Qi.pop()
        Qi.append(i);
    for i in range(k, len(a)):
        result.append(a[Qi[0]])
        while Qi and Qi[0] <= i-k:
            Qi.popleft()
        while Qi and a[i] < a[Qi[-1]]:
            Qi.pop()
        Qi.append(i)
    result.append(a[Qi[0]])   
    return result
