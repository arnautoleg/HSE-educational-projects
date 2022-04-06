def tree_size(root):
    if root is None:
        return 0
    global occurence
    occurence[root.key] = 1

    tree_size(root.left)
    tree_size(root.right)


def count_distinct(root):
    global occurence
    occurence = {}
    tree_size(root)
    return len(occurence)
