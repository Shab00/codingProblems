class TreeNode:
    def __init__(self, val = 0, right = None, left = None):
        self.val = val
        self.right = right
        self.left = left

#    1
#   / \
#  2   3
p1 = TreeNode(1)
p1.left = TreeNode(2)
p1.right = TreeNode(3)
q1 = TreeNode(1)
q1.left = TreeNode(2)
q1.right = TreeNode(3)

# p2:
#    1
#   /
#  2
# q2:
#    1
#     \
#      2
p2 = TreeNode(1)
p2.left = TreeNode(2)
q2 = TreeNode(1)
q2.right = TreeNode(2)

# p3:
#    1
#   / \
#  2   1
# q3:
#    1
#   / \
#  1   2
p3 = TreeNode(1)
p3.left = TreeNode(2)
p3.right = TreeNode(1)
q3 = TreeNode(1)
q3.left = TreeNode(1)
q3.right = TreeNode(2)

tests = [
    (p1, q1, True),
    (p2, q2, False),
    (p3, q3, False),
]

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
     pass
 

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"


for idx, (p, q, expected) in enumerate(tests, start=1):
    actual = isSameTree(p, q)
    if actual == expected:
        print(f"Test {idx}: {GREEN}PASS{RESET} result={actual} expected={expected}")
    else:
        print(f"Test {idx}: {RED}FAIL{RESET} result={actual} expected={expected}")
