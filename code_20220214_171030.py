import math


def find_percentile(a, b, p):

    n, m = len(a), len(b)
    min_index, max_index = 0, n

    while (min_index <= max_index):
        i = int(math.ceil((min_index + max_index) / (100/p)))
        j = int(((n + m + 1) / (100/p)) - i)

        if (i < n and j > 0 and b[j - 1] > a[i]):
            min_index = i + 1

        elif (i > 0 and j < m and b[j] < a[i - 1]):
            max_index = i - 1
        else:
            if (i == 0):
                return b[j - 1]
            elif (j == 0):
                return a[i - 1]
            else:
                return max(a[i - 1], b[j - 1])
