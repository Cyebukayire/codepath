class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

# ['Trunk', 'Mcintosh', 'Granny Smith', 'Fuji', 'Opal', 'Crab', 'Gala']
root = TreeNode('Trunk')

child1 = TreeNode('Mcintosh')
child2 = TreeNode('Granny Smith')
child3 = TreeNode('Fuji')
child4 = TreeNode('Opal')
child5 = TreeNode('Crab')
child6 = TreeNode('Gala')

root.left = child1
root.right = child2

child1.left = child3
child1.right = child4

child2.left = child5
child2.right = child6

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
print_tree(root)