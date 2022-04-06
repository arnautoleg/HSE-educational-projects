import math


def check_BST(T):

    if (T == None):
        return True

    if (T.left != None and T.key < T.left.key):
        return False
    if (T.right != None and T.key > T.right.key):
        return False
    return check_BST(T.left) and check_BST(T.right)
