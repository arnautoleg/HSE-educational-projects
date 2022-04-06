import math


def tj(L, W):
    n = len(W)
    tbl = [math.inf] * (n + 1)
    split = [0] * (n + 1)
    tbl[0] = 0
    for i in range(1, n + 1):
        length = - 1
        for j in range(i-1, -1, -1):
            length += 1 + len(W[j])
            if length > L:
                P = math.inf
            else:
                P = (L - length)**3
            if tbl[j] + P < tbl[i]:
                tbl[i] = tbl[j] + P
                split[i] = j
    result = []
    last = n
    while last > 0:
        result.append(W[split[last]:last])
        last = split[last]

    final = ""
    for line in result[::-1]:
        final += " ".join(line)
        if line != result[0]:
            final += "\n"

    return final
