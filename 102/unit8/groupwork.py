from collections import deque
def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1
  return root

class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
         
def count_odd_splits(root):
    """
    Given the root of a binary tree where each node represents the number of splits in a leaf of a Monstera plant, return the number of Monstera leaves that have an odd number of splits.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.

    base case:
        if root is None:
            return 0
    counter = 0

    # Check if the node is an odd split
    # If it is it should have two children


    recursive:
    when node is odd:
        counter += 1
        return counter + count_odd_splits(left node) +  count_odd_splits(right node) 
    
    when node is even:
        return: counter + count_odd_splits(left node) +  count_odd_splits(right node) 
    
    """

    if root is None:
            return 0
    
    is_a_leaf = (root.left is None and root.right is None)

    if is_a_leaf:
        if root.val % 2 == 1:
            return 1
        #elif root.val %2 == 0:
        else:
            return 0
        
    else:
        count_from_right = count_odd_splits(root.right)
        count_from_left = count_odd_splits(root.left)
    return count_from_left + count_from_right      
    # left_odd = count_odd_splits(root.left)

"""
      2
     / \
    /   \
   3     5
  / \     \
 6   7     12

 
"""
# Using build_tree() function included at top of page
values = [2, 3, 5, 6, 7, None, 12]
monstera = build_tree(values)
print(count_odd_splits(monstera))
print(count_odd_splits(None))
