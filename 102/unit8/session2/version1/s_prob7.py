from utils.design import build_tree

class Pearl:
    def __init__(self, size=0, left=None, right=None):
        self.val = size
        self.left = left
        self.right = right

def min_diff_in_pearl_sizes(root):
    """
    Ex: [1, None, 4, None, 6, None, 8, None, 19] => 2

            1
             \
              4
               \
                6
                 \
                  8
                   \
                    19

    Ex: [4, 2, 6, 1, 3, None, 8] => 1
        4
       / \
      2   6
     / \   \
    1   3   8

    Ex: [3, None 9] => 6

    cases:
    if not root:
        return
    if root.right and root.left:
        curr_min = min(root.val - root.left.val, root.right.val - root.val)
        left_min = min_diff_in_pearl_sizes(root.left)
        right_min = min_diff_in_pearl_sizes(root.right)
        if not left_min and not right_min:
            return curr_min
        elif not left_min:
            return min(curr_min, right_min)
        elif not right_min:
            return min(curr_min, left_min)
        else:
            return min(curr_min, min(left_min, right_min))

    elif root.left:
        curr_min = root.val - root.right.val
        left_min = min_diff_in_pearl_sizes(root.left)
        if left_min:
            return min(curr_min, left_min)
        else:
            return curr_min

    elif root.right:
        curr_min = root.right.val - root.val
        right_min = min_diff_in_pearl_sizes(root.right)
        if right_min:
            return min(curr_min, right_min)
        else:
            return curr_min

    else:
        return

    """
    if not root:
        return
    if root.right and root.left:
        curr_min = min(root.val - root.left.val, root.right.val - root.val)
        left_min = min_diff_in_pearl_sizes(root.left)
        right_min = min_diff_in_pearl_sizes(root.right)
        if not left_min and not right_min:
            return curr_min
        elif not left_min:
            return min(curr_min, right_min)
        elif not right_min:
            return min(curr_min, left_min)
        else:
            return min(curr_min, min(left_min, right_min))

    elif root.left:
        curr_min = root.val - root.right.val
        left_min = min_diff_in_pearl_sizes(root.left)
        if left_min:
            return min(curr_min, left_min)
        else:
            return curr_min

    elif root.right:
        curr_min = root.right.val - root.val
        right_min = min_diff_in_pearl_sizes(root.right)
        if right_min:
            return min(curr_min, right_min) 
        else:
            return curr_min

    else:
        return

# Use build_tree() function at top of page
values = [4, 2, 6, 1, 3, None, 8]
pearls = build_tree(values)
print(min_diff_in_pearl_sizes(pearls)) # 1

pearls1 = build_tree([3, None, 9])
print(min_diff_in_pearl_sizes(pearls1))  #6

pearls2 = build_tree([1, None, 4, None, 6, None, 8, None, 19])
print(min_diff_in_pearl_sizes(pearls2))  #2


