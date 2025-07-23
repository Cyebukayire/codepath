from print_tree import print_tree

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque

def right_vide(root):
    if not root:
        return []
    
    res = []
    deque_ = deque([root])
    while deque_:
        node = deque_.popleft()
        res.append(node.val)
        if node.left:
            deque_.append(node.right)

    return res

ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))
# print_tree(ivy1)
print(right_vide(ivy1))