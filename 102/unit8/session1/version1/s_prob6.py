class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def survey_tree(root):
    if not root:
        return []
    return survey_tree(root.left) + survey_tree(root.right) + [root.val]

"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""
sample = TreeNode('Root', TreeNode('Node1', TreeNode('Leaf1')), TreeNode('Node2', TreeNode('Leaf2'), TreeNode('Leaf3')))

print(survey_tree(sample))
