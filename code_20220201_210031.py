import numpy as np
import math


def possible_escapes(maze, i=0, j=0):
    n = len(maze)
    m = len(maze[0])
    if i == n - 1 and j == m - 1:
        return [[(i, j)]]
    maze[i][j] = 1
    result = []
    for a, b in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
        if (0 <= a < n and 0 <= b < m) and maze[a][b] == 0:
            paths = possible_escapes(maze, a, b)
            for path in paths:
                result.append([(i, j), *path])

    maze[i][j] = 0
    return result


def weighted_escape_length(maze, w, length=0):
    n = len(maze)
    m = len(maze[0])

    paths = possible_escapes(np.zeros((n, m)))
    paths_length_list = []

    for path in paths:
        for _ in path:
            if maze[_[0]][_[1]] == 0:
                length += 1
            else:
                length += w
        paths_length_list.append(length)
        length = 0

    return min(paths_length_list)
