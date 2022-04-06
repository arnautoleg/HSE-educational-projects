import math


def check_BST(T, l=None, r=None):

    if (T == None):
        return True
    if (l != None and T.data <= l.data):
        return False
    if (r != None and T.data >= r.data):
        return False
    return check_BST(T.left, l, T) and \
        check_BST(T.right, T, r)
