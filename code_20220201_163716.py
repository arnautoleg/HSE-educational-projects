import math


def fastest_escape_length(maze, i=0, j=0):
    n = len(maze)
    m = len(maze[0])
    if i == n - 1 and j == m - 1 and maze[i][j] == 0:
        return 1
    maze[i][j] = 1
    result = math.inf

    for a, b in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
         if 0 <= a < n and 0 <= b < m and maze[a][b] == 0:
                result = min(result, (fastest_escape_length(maze, a, b)+1))

    maze[i][j] = 0
    return result
