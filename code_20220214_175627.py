def find_percentile(a, b, p):

    n, m = len(a), len(b)
    min_index, max_index = 0, n

    while min_index <= max_index:

        i = int((min_index + max_index) / 2)
        j = int(((n + m + 1) * p / 100) - i)

        if i < n and j > 0 and b[j - 1] > a[i]:
            min_index = i + 1
        elif i > 0 and j < m and b[j] < a[i - 1]:
            max_index = i - 1
        else:
            if (i == 0):
                percentile = b[j]
            elif (j == 0):
                percentile = a[i - 1]
            else:
                percentile = max(a[i - 1], b[j - 1])
            break
    return percentile
