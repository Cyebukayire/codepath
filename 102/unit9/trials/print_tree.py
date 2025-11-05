from collections import deque
class Node:
    def __init__(self,val,l=None, r=None):
        self.val = val
        self.left=l
        self.right=r

# DFS
def print_tree_dfs_inorder(root):
    res = []
    # stack = [root]
    stack=deque([root])
    while stack:
        node = stack.popleft()
        if not node:
            res.append(None)
        else:
            res.append(node.val)
            stack.appendleft(node.right)
            stack.appendleft(node.left)

    while not res[-1]:
        res.pop(-1)

    return res

def print_tree_dfs_preorder(root):
    pass
def print_tree_dfs_postorder(root):
    pass

# TEST DFS
node = Node(5,Node(3,Node(2),Node(4)),Node(7,Node(6),Node(8)))
print(print_tree_dfs_inorder(node))


# BFS