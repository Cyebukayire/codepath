from utils.design import build_tree

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def non_bst_find_flower(root, name):
    if root is None:
        return False
    if root.val == name:
        return True
    return non_bst_find_flower(root.left, name) or non_bst_find_flower(root.right, name)

"""
         Daisy
        /    \
      Lily   Tulip
     /  \       \
  Rose  Violet  Lilac
"""

# using build_tree() function at top of page
values = ["Rose", "Lily", "Tulip", "Daisy", "Lilac", None, "Violet"]
garden = build_tree(values)

print(non_bst_find_flower(garden, "Lilac"))  
print(non_bst_find_flower(garden, "Sunflower")) 

"""
Solution: The sol in prob2 differs from non-bst solution in prob3 becuase in prob2 we are aware of the bst's ordering of nodes. The left nodes are smaller than the parent and
right nodes are greater than the parent. So at every step, we cut our search options into half, and follow one spefic path that we are certain it might contain our search value. 
Everytime we find that current parent is not what we are looking for, we choose one path to take, either right or left. 
So in prob2 time complexity is O(log n) while for prob3 time complexity is O(n) SINCE WE traverse through the whole tree and reach every one to find the search value we are looking for.

For DFS approach: Space complexity for both bst and non-bst structure depends on the call stack of the recursive algorithm. They both have same space complexity of O(h)
For BFS approach: Space complexity relies on the stack consumed by the queue used to store the nodes. Space depends on the Max width of the tree, so they both have same complexity of O(w)

For BFS: Either searching from bst or non-bst, the balanced tree takes more space because the usually the nodes on the same level can get to n/2 nodes on a same level, making space O(n), while in 
a non balanced tree, it can be skewed to 1 one on each level, leading to queue holding only one node at a time, which is O(1) space complexity.

For DFS approach: Space can only dependo on the call stack, so either the bst, or non-bst, space consumed stays as O(h)
"""


"""
Solution:
The solution in Problem 2 differs from the one in Problem 3 because in Problem 2, 
we are working with a binary search tree (BST), which has a well-defined ordering: 
left child nodes are smaller than the parent, and right child nodes are greater. 
This structure allows us to eliminate half of the tree at each step, following only 
one path (either left or right) based on comparisons. This reduces the time 
complexity to O(log n) in a balanced BST.

In contrast, the tree in Problem 3 is not a BST, so we cannot make any assumptions 
about the node ordering. As a result, we must traverse every node in the tree to find 
the target value, leading to a time complexity of O(n).

Space Complexity (DFS):
For the DFS approach, space complexity depends on the call stack, which is 
determined by the height h of the tree. So, whether the tree is a BST or not, 
the space complexity remains O(h).

Space Complexity (BFS):
For BFS, space complexity depends on the maximum number of nodes stored in the queue, 
which is determined by the maximum width of the tree (w):

In a balanced tree, the width can be large (up to n/2 at the bottom level), so the 
space complexity becomes O(n).

In a skewed or unbalanced tree, each level may have only one node, so the queue 
holds at most one node at a time — leading to O(1) space in the best case.

Therefore, BFS uses more space in balanced trees than in skewed ones, and the 
worst-case space complexity for BFS is O(n).

 Summary Table:
Aspect	            BST (Balanced)	    Non-BST or Skewed Tree
Time (DFS/BFS)	       O(log n)	            O(n)
Space (DFS)	           O(h)	                O(h)
Space (BFS)	           O(n) (due to width)	O(1) to O(n)

"""

