from utils.design import build_tree

class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right

from collections import deque

def count_odd_splits_BFS(root):
    """
            2
           / \
          3   5
         / \   \
        4  1    7 ==> 2^h nodes ==> (n/2) nodes
    res = [3, 5, 1, 7]
    time complexity: O(n)
    Space complexity: O(w)
    """
    if not root:
        return 0
    
    deque_ = deque([root])
    counter = 0

    while deque_:
        node = deque_.popleft()
        if node.val % 2 == 1:
            counter += 1
        if node.left:
            deque_.append(node.left)
        if node.right:
            deque_.append(node.right)

    return counter


def count_odd_split_DFS_inorder(root):
    """
    
            2
           / \
          3   5
         / \  / \
        4  1  6  7
    res = calls(4, 0), call(1, 1), return 1 call(5, 0), return 0

    time complexity: O(n)
    Space complexity: O(h)


    """

    if not root:
        return 0
    
    #     count += 1
    print(root.val)
    count = 0
    if root.val %2 == 1:
        count += 1
        
    return count_odd_split_DFS_inorder(root.left) + count + count_odd_split_DFS_inorder(root.right)
    
    # res.append(root.val)

    # return 


def count_odd_split_DFS_preorder(root):
    pass

def count_odd_split_DFS_postorder(root):
    pass


# TEST CASES
values = [2, 3, 5, 6, 7, None, 12]
monstera = build_tree(values)
monstor = build_tree([2,3,5,4,1,6,7])
"""
OHHH:
What do you do when you're absolutely stack on something you know is so simple?

"""

# BFS
# print(count_odd_splits_BFS(monstera))
# print(count_odd_splits_BFS(None))

# DFS
res = count_odd_split_DFS_inorder(monstor)
print("count: ", res)
