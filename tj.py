import math


def tj(L, W):
    n = len(W)
    tbl = [math.inf] * (n + 1)
    tbl[0] = 0
    splt = [math.inf] * (n + 1)
    splt[0] = 0
    for i in range(1, n + 1):
        length = -1
        for j in range(i-1, -1, -1):
            length += 1 + len(W[j])
            if length > L:
                P = math.inf
            elif i == n:
                P = 0
            else:
                P = (L - length) ** 3
            if tbl[j] + P < tbl[i]:
                tbl[i] = tbl[j] + P
                splt[i] = j
    lines = W
    splt = [i for i in splt if i != 0]
    temp = ['\n'] * len(splt)
    assert(len(splt) == len(temp))
    acc = 0
    for i in range(len(splt)):
        lines.insert(splt[i]+acc, temp[i])
        acc += 1
    return str(''.join(lines))
