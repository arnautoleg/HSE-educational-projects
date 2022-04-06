import math


def inorder(curr, prev):
    global ans
    if (curr == None):
        return
    inorder(curr.left, prev)
    if (prev != None):
        ans = min(curr.data - prev.data, ans)
    prev = curr
    inorder(curr.right, prev)


def min_diff(T):
    prev = None
    global ans
    ans = math.inf
    inorder(T, prev)
    return ans
