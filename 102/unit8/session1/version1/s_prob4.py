from print_tree import print_tree

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque

def right_vide(root):
    if not root or not root.val:
        return []
    
    res = [root.val]
    res.extend(right_vide(root.right))
    return res

ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))
# print_tree(ivy1)
node = TreeNode("Node1")
print(node.val)
print(right_vide(node))
print(right_vide(ivy1))