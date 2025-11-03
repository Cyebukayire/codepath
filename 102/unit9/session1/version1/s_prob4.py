from utils.design import build_tree

class TreeNode():
     def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
from collections import deque

def max_tiers(cake):
    if not cake:
        return 0
    
    deque_ = deque([(cake, 1)])
    counter = 0
    level = 0

    while deque_:
        node, lvl = deque_.popleft()
        if lvl > level:
            level = lvl
            counter += 1

        if node.left: deque_.append((node.left, level + 1))
        if node.right: deque_.append((node.right, level + 1))
    return counter
    

        
"""
        Chocolate
        /        \
    Vanilla    Strawberry
                /     \
         Chocolate    Coffee
"""

# Using build_tree() function included at top of page
cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Coffee"]
cake = build_tree(cake_sections)

print(max_tiers(cake))