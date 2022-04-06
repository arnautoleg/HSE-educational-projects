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


def fastest_escapes(maze, i=0, j=0, fast_paths=[]):
    variants = possible_escapes(maze)
    if fastest_escape_length(maze) > 0:
        for _ in variants:
            if len(_) == fastest_escape_length(maze):
                fast_paths.append(_)
    return fast_paths

    maze[i][j] = 0
    return result
