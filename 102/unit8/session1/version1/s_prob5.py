class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

""""
Using an iterative Breadth First Search(BFS)
deque ==> holds nodes of the tree we need to check for; from left to the right
counter = 0
              Root
            /     \
          Node1  Node2
          /         \
        Node3       Node4

while loops until deque is empty
counter increments when node has no children
Time complexity is O(h), h = the degree of the tree
Space complexity is O(n), n = number of nodes
"""
from collections import deque
def count_leaves(root):
    counter = 0
    deque_ = deque([root])

    while deque_:
        node = deque_.popleft()
        if not node.right and not node.left:
            counter += 1
            continue
        if node.left:
            deque_.append(node.left)
        if node.right:
            deque_.append(node.right)
        
    return counter


"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""
oak1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
oak2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))


print(count_leaves(oak1))
print(count_leaves(oak2))