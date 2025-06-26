class TreeNode:
    def __init__(self, value=0, right=None, left=None):
        self.value = value
        self.right = right
        self.left = left

def get_nodes(root):
    res = []

    def traverse(root):
        if root:
            traverse(root.left)
            res.append(root.value)
            traverse(root.right)
    
    traverse(root)

    return res


node1 = TreeNode(3)
node2 = TreeNode(2)
node3 = TreeNode(1)
node4 = TreeNode(34)
node5 = TreeNode(89)

node1.left=node2
node2.left = node3
node1.right = node4
node4.right = node5

print(get_nodes(node1))