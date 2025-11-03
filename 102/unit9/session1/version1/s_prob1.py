# from utils.print_tree import print_tree
from utils.design import build_tree
from collections import deque
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

class TreeNode():
     def __init__(self, quantity, left=None, right=None):
        self.val = quantity
        self.left = left
        self.right = right

def merge_orders(order1, order2):
    """
    if not order1 and not order2:
        return None

    elif not order1:
        return order2
    elif not order2:
        return order1
    
    else: # When both order1 and order2 are not null
        merged_order = TreeNone(order1.val + order2.val)
        merged_order.left = merge_orders(order1.left, order2.left)
        merged_order.right = merged_orders(order1.right, order2.right)
        return merged_order
        
    """

    if not order1:
        return order2
    elif not order2:
        return order1
    
    else: # When both order1 and order2 are not null
        merged_order = TreeNode(order1.val + order2.val)
        merged_order.left = merge_orders(order1.left, order2.left)
        merged_order.right = merge_orders(order1.right, order2.right)
        return merged_order


"""
     1             2         
    /  \         /   \       
   3    2       1     3   
 /               \      \   
5                 4      7   
"""
# Using build_tree() function included at top of page
cookies1 = [1, 3, 2, 5]
cookies2 = [2, 1, 3, None, 4, None, 7]
order1 = build_tree(cookies1)
order2 = build_tree(cookies2)

# Using print_tree() function included at top of page
print_tree(merge_orders(order1, order2))