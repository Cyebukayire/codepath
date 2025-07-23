class TreeNode:

    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


from collections import deque

"""
Time complexity is: O(n), because we process every node once
Average Space Complexity is: O(w), w is the maximum width of the tree, presented by number of nodes at the widest level of the tree. The space complexity is O(w) becuase we are using BFS, so the worst case is when queue is holding all the nodes of the widest level, which are w
Worst case Space complexity is: O(n), the worst case is when the tree is a complete binary tree, the widest level is the last with 2^h nodes, 2^h == n/2 == n

"""
def harvest_berries(root, threshold):
    if not root:
        print("No root")
        return 0

    deque_ = deque([root])
    result = 0

    while deque_:
        node = deque_.popleft()
        if node.val > threshold:
            result += node.val
        # print("REACHED LOOP")
        if node.left:
            # print("Node ", node.val , " has left")
            deque_.append(node.left)
        if node.right:
            deque_.append(node.right)
    return result
  
"""
       4
     /   \
   10     6
  /  \     \
 5    8    20
 
"""
bush = TreeNode(4, TreeNode(10, TreeNode(5), TreeNode(8)), TreeNode(6, None, TreeNode(20)))

print(harvest_berries(bush, 6))
print(harvest_berries(bush, 30))