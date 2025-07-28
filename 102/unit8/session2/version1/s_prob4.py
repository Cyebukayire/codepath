from utils.design import build_tree
from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

"""
            root
    left            right
left    right   left    right

time complexity: O(logn)
Space complexity: O(h), h: height of the tree

Approach: recursive
Base case: if root is None: return TreeNode(name)
recursive case:
compare and see if the new node should be located to the right or to the left of the subtree
"""
def add_plant(root, name):
    if root is None:
        print("HEREEEE")
        return TreeNode(name)
    else:
        if root.left is None and name < root.val:
            root.left = TreeNode(name)
        elif root.right is None and name > root.val:
            root.right = TreeNode(name)
        else:
            if name < root.val:
                add_plant(root.left, name)
            else:
                add_plant(root.right, name)


"""
            Money Tree
        /              \
Fiddle Leaf Fig    Snake Plant
"""

# Using build_tree() function at the top of page
values = ["Money Tree", "Fiddle Leaf Fig", "Snake Plant"]
root = build_tree(values)
print_tree(root)

add_plant(root, "Aloe")
print_tree(root)


root = TreeNode("M")
add_plant(root, "F")
add_plant(root, "Z")
print_tree(root)

add_plant(root, "A") 
print_tree(root)


def clean_add_plant(root, name):
    if not root:
        return TreeNode(name)
    
    if root.val > name:
        root.left = clean_add_plant(root.left, name)
    else:
        root.right = clean_add_plant(root.right, name)

    return root


values = ["Money Tree", "Fiddle Leaf Fig", "Snake Plant"]
root = build_tree(values)
print_tree(root)
print_tree(clean_add_plant(root, "Aloe"))
