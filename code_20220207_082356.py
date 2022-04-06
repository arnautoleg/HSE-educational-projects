def edistance(A, B):
    m = len(A)+1
    n = len(B)+1
    D = [[0 for x in range(n)] for x in range(m)]

    for i in range(m):
        for j in range(n):
            if i == 0:
                D[i][j] = j
            elif j == 0:
                D[i][j] = i
            elif A[i-1] == B[j-1]:
                D[i][j] = D[i-1][j-1]
            else:
                D[i][j] = 1 + min(D[i][j-1], D[i-1][j], D[i-1][j-1])
    return D[m-1][n-1]
