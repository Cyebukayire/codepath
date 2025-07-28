from collections import deque 

# Tree Node class
class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
      self.val = value
      self.left = left
      self.right = right

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
    
def remove_species(ecosystem, name):
    if not ecosystem:
        return None
    if ecosystem.val == name:

        # If the node has no children
            # Remove the node by setting parent pointer to None
        if not ecosystem.left and not ecosystem.right:
            return None
        

        # If the node has one child
            # Replace the node with its child
        elif ecosystem.left and not ecosystem.right:
            return ecosystem.left
        
        elif ecosystem.right and not ecosystem.left:
            return ecosystem.right
        
        # If the node has two children
            # Find the inorder successor
            # Replace the node's value with inorder successor value
            # Remove inorder successor
        else:
            left = ecosystem.left
            curr = left
            while curr.right:
                curr = curr.right
            curr.right = ecosystem.right
            return left
        
    if ecosystem.left:
        ecosystem.left = remove_species(ecosystem.left, name)
    if ecosystem.right:
        ecosystem.right = remove_species(ecosystem.right, name)

    # Return root of updated tree
    return ecosystem
    
    


"""
                Dugong
             /         \
       Brain Coral   Lionfish
              \       /       \
         Clownfish Giant Clam  Seagrass
"""
# Use build_tree() function at top of page
values = ["Dugong", "Brain Coral", "Lionfish", None, "Clownfish", "Giant Clam", "Seagrass"]
ecosystem = build_tree(values)
print_tree(ecosystem)
# Using print_tree() function at top of page
print_tree(remove_species(ecosystem, "Brain Coral"))

"""Result
                Dugong
             /         \
       Clownfish     Lionfish
                      /       \
                Giant Clam  Seagrass
"""

print_tree(remove_species(ecosystem, "Lionfish"))
"""Result
                Dugong
             /         \
       Clownfish     Giant Clam
                         \
                      Seagrass
"""