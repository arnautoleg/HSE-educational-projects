import math


def merge(a, b):
    result = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    while i < len(a):
        result.append(a[i])
        i += 1
    while j < len(b):
        result.append(b[j])
        j += 1
    return result


def mergesort(A):
        if len(A) <= 1:
            return A
        mid = len(A) // 2
        left = mergesort(A[:mid])
        right = mergesort(A[mid:])
        return merge(left, right)


def find_percentile(a, b, p):
    A = a + b
    B = mergesort(A)
    return B[int(math.ceil(((len(a) + len(b))*(p/100)))) - 1]
