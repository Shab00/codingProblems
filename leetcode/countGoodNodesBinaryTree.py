class TreeNode:
    def __init__(self, val = 0, right = None, left = None):
        self.val = val
        self.right = right
        self.left = left


# Example 1

# Input: `root = [3,1,4,3,null,1,5]`  
# Output: `4`

# Tree (level-order array -> drawn):

# Level-order: [3, 1, 4, 3, null, 1, 5]

#      3
#     / \
#    1   4
#   /   / \
#  3   1   5

root1 = TreeNode(3)
root1.left = TreeNode(1)
root1.left.left = TreeNode(3)
root1.right = TreeNode(4)
root1.right.right = TreeNode(5)
root1.right.left = TreeNode(1)

# Explanation:
# - Root Node (3) is always a good node.
# - Node 4 -> path (3, 4) — 4 is the maximum in this path.
# - Node 5 -> path (3, 4, 5) — 5 is the maximum in this path.
# - Node 3 (left leaf) -> path (3, 1, 3) — 3 is the maximum in this path.

# Example 2

# Input: `root = [3,3,null,4,2]`  
# Output: `3`

# Tree (level-order array -> drawn):

#Level-order: [3, 3, null, 4, 2]

#     3
#    /
#   3
#  / \
# 4   2

root2 = TreeNode(3)
root2.left = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(2)

# Explanation:
# - Node 2 -> path (3, 3, 2) is not good because there is a node (3) greater than 2 on the path.

# Example 3

# Input: `root = [1]`  
# Output: `1`

# Tree:

# 1

root3 = TreeNode(1)

# Explanation:
# - Root is considered good.

inputs = [(root1, [3,1,4,3,None,1,5], 4),
          (root2, [3,3,None,4,2], 3),
          (root3, [1], 1)]

def countGoodNodes(root: TreeNode) -> int:

    if root is None:
        return 0

    stack = [(root, root.val)]
    count = 0
    while stack:
        node, curMax = stack.pop()
        if node.val >= curMax:
            count += 1
        new_max = max(curMax, node.val)
        if node.right:
            stack.append((node.right, new_max))
        if node.left:
            stack.append((node.left, new_max))
    return count

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (root, inputs, expec) in enumerate(inputs, start=1):
    result = countGoodNodes(root)
    if result == expec:
        print(f"Example {idx}: {GREEN}PASS{RESET} output=>{result}, expected=>{expec}")
    else:
        print(f"Example {idx}: {RED}FAIL{RESET} output=>{result}, expected=>{expec}")
