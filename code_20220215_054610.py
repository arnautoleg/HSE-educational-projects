def find_percentile(a, b, p):

    global median, i, j
    n = len(a)
    m = len(b)
    min_index = 0
    max_index = n-1
    while (min_index <= max_index):
        i = int((min_index + max_index) / 2)
        j = int(((n + m + 1) * p * 0.01) - i)

        if (i < n and j > 0 and b[j - 1] > a[i]):
            min_index = i + 1
        elif (i > 0 and j < m and b[j] < a[i - 1]):
            max_index = i - 1
        else:
            if (i == 0):
                median = b[j]
            elif (j == 0):
                median = a[i-1]
            else:
                median = max(a[i-1], b[j-1])
            break
    return median
