class TreeNode:
    def __init__(self, val = 0, right = None, left = None):
        self.val = val
        self.right = right
        self.left = left

# Example 1
# Input: root = [2,1,3]
# Output: true
#
# Level-order: [2, 1, 3]
#
#   2
#  / \
# 1   3
#
root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)
#
# Example 2
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
#
# Level-order: [5, 1, 4, null, null, 3, 6]
#
#     5
#    / \
#   1   4
#      / \
#     3   6
#
root2 = TreeNode(5)
root2.left = TreeNode(1)
root2.right = TreeNode(4)
root2.right.left = TreeNode(3)
root2.right.right = TreeNode(6)

inputs = [
    (root1, True),
    (root2, False)
    ]

def validate(root: TreeNode) -> bool:
    pass

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (root, expec) in enumerate(inputs, start=1):
    result = validate(root)
    if result == expec:
        print(f"Example {idx}: {GREEN}PASS{RESET} output=>{result}, expected=>{expec}")
    else:
        print(f"Example {idx}: {RED}FAIL{RESET} output=>{result}, expected=>{expec}")
