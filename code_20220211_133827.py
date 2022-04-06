def tree_size(root):
    if root is None:
        return 0
    return 1 + tree_size(root.left)


def count_distinct(root):
    global occurence
    occurence = {}
    tree_size(root)
    return len(occurence)
