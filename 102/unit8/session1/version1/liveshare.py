##

"""
Problem 1
You are grafting different varieties of apple onto the same root tree can produce many different varieties of apples! Given the following TreeNode class, create the binary tree depicted below. The text representing each node should should be used as the value.

The root, or topmost node in the tree TreeNode("Trunk") has been provided for you.

             Trunk
          /         \
      Mcintosh   Granny Smith
      /     \       /     \
    Fuji   Opal   Crab   Gala
"""
from collections import deque

def print_tree(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    print(result)

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

root = TreeNode("Trunk")

fuji = TreeNode("Fuji")
opal = TreeNode("Opal")
crab = TreeNode("Crab")
gala = TreeNode("Gala")

mcintosh = TreeNode("Mcintosh", left=fuji, right = opal)
granny_smith = TreeNode("Granny Smith", left = crab, right = gala)
root.left = mcintosh
root.right =granny_smith

# Using print_tree() included at the top of this page
print_tree(root)


['Trunk', 'Mcintosh', 'Granny Smith', 'Fuji', 'Opal', 'Crab', 'Gala']

"""You have a fruit tree represented as a binary tree with exactly three nodes: the root and its two children. Given the root of the tree, evaluate the amount of fruit your tree will yield this year. The tree has the following form:

Leaf nodes have an integer value.
The root has a string value of either "+", "-", "*", or "-".
The yield of a the tree is calculated by applying the mathematical operation to the two children.

Return the result of evaluating the root node.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity."""

def calculate_yield(root):
    # root stores operation
    # left child and right child are the numbers that the operation should be applied to
    # conditions to compare with operation
    left_val = root.left.val
    right_val = root.right.val

    if root.val == "+":
        return left_val + right_val
    elif root.val == "-":
        return left_val - right_val
    elif root.val == "*":
        return left_val * right_val
    elif root.val == "/":
        # we know it's divide
        return left_val / right_val

apple_tree = TreeNode("+", TreeNode(7), TreeNode(5))
print(calculate_yield(apple_tree))

divide = TreeNode("/", TreeNode(7), TreeNode(5))
print(calculate_yield(divide))


"""

"""

def right_vine(root):
    # keep going to right until you can't
    # if there is no right, go left 
    #IF there's no children, stop
    path = []
    current = root
    while current:
        path.append(current.val)
        current = current.right

    return path

    

"""
        Root
      /      \
    Node1    Node2
  /         /  
Leaf1    Leaf2
"""

"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""
ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

# funkyvine = TreeNode("Root", 
 #               TreeNode("Node1", TreeNode("Leaf1")),
   #             TreeNode("Node2", TreeNode("Leaf2")))

print(right_vine(ivy1))
print(right_vine(ivy2))
# print(right_vine(funkyvine))

"""

Recursive Approach

1. Base case
    If you have no right child, return 
    blank
    When Node is None
    or when Node has None value
    
2. Recursive case
    If you have a right child, return an array with
    [Your value | right_vine on your right child]
    

"""

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def right_vine_recurse(root):
    if not root:
        return []
    return [root.val] + right_vine(root.right)

print(right_vine_recurse(ivy1))
print(right_vine_recurse(ivy2)) 

def count_leaves(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    return count_leaves(root.left) + count_leaves(root.right)

# count_leaves(Root)
# count_leaves(1) + count_leaves(node2)
# 

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


"""
Base cases:
When Node is None
    return 0

In case you are a leaf -
    return 1
    
else if you have children
    return sum count_leaves for your children (that exist)
"""

