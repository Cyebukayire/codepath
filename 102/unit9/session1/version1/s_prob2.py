class Puff():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

from collections import deque
def print_design(design):
    queue_ = deque([design])
    result = []
    while queue_:
        node = queue_.popleft()
        result.append(node.val)
        if node.left:
            queue_.append(node.left)
        if node.right:
            queue_.append(node.right)
    print(result)


"""
            Vanilla
           /       \
      Chocolate   Strawberry
      /     \
  Vanilla   Matcha  
"""
croquembouche = Puff("Vanilla", 
                    Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
                    Puff("Strawberry"))
print_design(croquembouche)