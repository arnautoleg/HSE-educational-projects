def check_BST(root):
    compare = lambda _: True
    if not root:
        return True
    else:
        return compare(root.key) \
           and check_BST(root.left, lambda l: compare(l) and l < root.key) \
           and check_BST(root.right, lambda r: compare(r) and r > root.key)
