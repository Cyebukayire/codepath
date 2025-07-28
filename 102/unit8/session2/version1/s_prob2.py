from utils.design import build_tree

class TreeNode():
    def __init__ (self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

# BFS
from collections import deque
def find_flower_bfs(inventory, name):
    if not inventory:
        return False
    
    deque_ = deque([inventory])

    while deque_:
        node = deque_.popleft()
        if node.val == name:
            return True
        if name > node.val and node.right:
            deque_.append(node.right)
        elif name < node.val and node.left :
            deque_.append(node.left)

    return False

values = ["Rose", "Lilac", "Tulip", "Daisy", "Lily", None, "Violet"]
garden = build_tree(values)

print(find_flower_bfs(garden, "Lilac"))  
print(find_flower_bfs(garden, "Sunflower")) 

# DFS
def find_flower_dfs(inventory, name):
    if inventory is None:
        return False
    
    if inventory.val == name:
        return True
    
    elif name < inventory.val:
        return find_flower_dfs(inventory.left, name)

    elif name > inventory.val:
        return find_flower_dfs(inventory.right, name)

print(find_flower_dfs(garden, "Lilac"))  
print(find_flower_dfs(garden, "Sunflower")) 


