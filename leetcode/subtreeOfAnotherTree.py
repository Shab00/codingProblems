class TreeNode:
    def __init__(self, val = 0, right = None, left = None):
        self.val = val
        self.right = right
        self.left = left


# Example 1:
# root = [3,4,5,1,2], subRoot = [4,1,2]
#
#    3
#   / \
#  4   5
# / \
#1   2

root1 = TreeNode(3)
root1.left = TreeNode(4)
root1.right = TreeNode(5)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(2)

subroot1 = TreeNode(4)
subroot1.left = TreeNode(1)
subroot1.right = TreeNode(2)


# Example 2:
# root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
#
# Level order indices: 0:3
# 1:4, 2:5
# 3:1, 4:2, 5:None, 6:None
# 7:None, 8:None, 9:0
#
#    3
#   / \
#  4   5
# / \
#1   2
#    /
#   0

root2 = TreeNode(3)
root2.left = TreeNode(4)
root2.right = TreeNode(5)
root2.left.left = TreeNode(1)
root2.left.right = TreeNode(2)
# 5's children are None by default
# attach the '0' as the left child of the node with value 2
root2.left.right.left = TreeNode(0)

subroot2 = TreeNode(4)
subroot2.left = TreeNode(1)
subroot2.right = TreeNode(2)

examples = [
    (root1, subroot1, True),
    (root2, subroot2, False),
]

def isSubtree(root: TreeNode, subroot: TreeNode) -> bool:
    pass

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (root, subroot, expec) in enumerate(examples, start=1):
    result = isSubtree(root, subroot)
    if result == expec:
        print(f"Test {idx}: {GREEN}PASS{RESET} result={result} expected={expec}")
    else:
        print(f"Test {idx}: {RED}FAIL{RESET} result={result} expected={expec}")
