def count_distinct(root):
    global occurence
    occurence = {}
    tree_size(root)
    return len(occurence)
