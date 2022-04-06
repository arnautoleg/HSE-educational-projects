import math


def tree_max(root):
    if root is None:
        return -math.inf

    result = root.key
    l_result = tree_max(root.left)
    r_result = tree_max(root.right)

    return max(result, l_result, r_result)
