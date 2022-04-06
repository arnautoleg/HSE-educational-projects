def find_percentile(a, b, p):

    n, m = len(a), len(b)
    low_index = 0
    if len(a) >= len(b):
        high_index = n
    else:
        high_index = m

    while (low_index <= high_index):

        left = (low_index + high_index)//2
        right = int(((n + m + 1) * (p/100)) - left)

        if left < n and right > 0 and b[right - 1] > a[left]:
            low_index = left + 1
        elif right < m and left > 0 and a[left - 1] > b[right]:
            high_index = left - 1
        else:
            if left == 0:
                percentile = b[right - 1]
            elif right == 0:
                percentile = a[left - 1]
            else:
                percentile = max(a[left - 1], b[right - 1])
            break
    return percentile
