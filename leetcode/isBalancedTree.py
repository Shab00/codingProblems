from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(7)
root.right.right = TreeNode(9)
root.right.left = TreeNode(6)

#
#          4
#        /   \
#       2     7
#      / \   / \
#     1   3 6   9
#

rootTwo = TreeNode(1)
rootTwo.left = TreeNode(2)
rootTwo.right = TreeNode(3)
rootTwo.left.left = TreeNode(4)
rootTwo.left.left.left = TreeNode(5)

#
#         1
#        / \
#       2   3
#      /
#     4
#    /
#   5
#

def isBalanced(root: TreeNode) -> bool:
    pass

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

tests = [(root, True), (rootTwo, False)]

for idx, (tree, expected) in enumerate(tests, start=1):
    actual = isBalanced(tree)
    if actual == expected:
        print(f"Test {idx}: {GREEN}PASS{RESET} result={actual} expected={expected}")
    else:
        print(f"Test {idx}: {RED}FAIL{RESET} result={actual} expected={expected}")
