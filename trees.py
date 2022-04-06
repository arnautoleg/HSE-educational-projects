import math

class Node:
    def __init__(self, key=0, parent = None):
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent

def insert(root, node):
    if root.key > node.key:
        if root.left == None:
            root.left = node
            node.parent = root
        else:
            insert(root.left, node)
    else:
        if root.right == None:
            root.right = node
            node.parent = root
        else:
            insert(root.right, node)

#######################################################

def tree_size(root):
    if root==None:
        return
    global occurence
    occurence[root.key]=1
    tree_size(root.left)
    tree_size(root.right)


def count_distinct(root):
    global occurence
    occurence={}
    tree_size(root)
    return len(occurence)

def tree_max(root):
    if root==None:
        return -math.inf
    res = root.key
    lres = tree_max(root.left)
    rres = tree_max(root.right)
    return max(res,lres,rres)

def _check_BST(root):
    pass

def check_BST(root):
    if (root == None):
        return True

    if (root.left != None and root.left.key > root.key):
        return False

    if (root.right != None and root.right.key < root.key):
        return False

    if (not(check_BST(root.left)) or not(check_BST(root.right))):
        return False

    return True

def _min_diff(curr,prev):
    global ans
    if (curr == None):
        return

    _min_diff(curr.left, prev)

    if (prev != None):
        ans = min(curr.key - prev.key, ans)
    prev = curr
    _min_diff(curr.right, prev)

def min_diff(root):
    prev = None
    global ans
    ans = math.inf
    _min_diff(root, prev)
    return ans

#################################################

if __name__ == "__main__":
    T = Node(3)
    insert(T, Node(1))
    insert(T, Node(2))
    # should print True
    print(check_BST(T))
    # should print 1
    print(min_diff(T))
    print(count_distinct(T))
