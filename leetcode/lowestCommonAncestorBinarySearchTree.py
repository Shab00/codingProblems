class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.right = right
        self.left = left

# Example 1:
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Expected LCA value: 6
#
#        6
#       / \
#      2   8
#     / \ / \
#    0  4 7  9
#      / \
#     3   5
n6_1 = TreeNode(6)
n2_1 = TreeNode(2)
n8_1 = TreeNode(8)
n0_1 = TreeNode(0)
n4_1 = TreeNode(4)
n7_1 = TreeNode(7)
n9_1 = TreeNode(9)
n3_1 = TreeNode(3)
n5_1 = TreeNode(5)

n6_1.left = n2_1
n6_1.right = n8_1
n2_1.left = n0_1
n2_1.right = n4_1
n8_1.left = n7_1
n8_1.right = n9_1
n4_1.left = n3_1
n4_1.right = n5_1

root1, p1, q1 = n6_1, n2_1, n8_1


# Example 2:
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Expected LCA value: 2
#
# Same shape as Example 1 (separate nodes for independent tests)
m6_2 = TreeNode(6)
m2_2 = TreeNode(2)
m8_2 = TreeNode(8)
m0_2 = TreeNode(0)
m4_2 = TreeNode(4)
m7_2 = TreeNode(7)
m9_2 = TreeNode(9)
m3_2 = TreeNode(3)
m5_2 = TreeNode(5)

m6_2.left = m2_2
m6_2.right = m8_2
m2_2.left = m0_2
m2_2.right = m4_2
m8_2.left = m7_2
m8_2.right = m9_2
m4_2.left = m3_2
m4_2.right = m5_2

root2, p2, q2 = m6_2, m2_2, m4_2


# Example 3:
# Input: root = [2,1], p = 2, q = 1
# Expected LCA value: 2
#
#    2
#   /
#  1
r2_3 = TreeNode(2)
r1_3 = TreeNode(1)
r2_3.left = r1_3

root3, p3, q3 = r2_3, r2_3, r1_3

tests = [
    (root1, p1, q1, 6),
    (root2, p2, q2, 2),
    (root3, p3, q3, 2),
]

def lowestCommon(root: TreeNode, p: TreeNode,  q: TreeNode) -> TreeNode:
    pass

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (root, p, q, expec) in enumerate(tests, start = 1):
    result = lowestCommon(root, p, q)
    if result == expec:
        print(f"Test {idx}: {GREEN}PASS{RESET} result={result} expected={expec}")
    else:
        print(f"Test {idx}: {RED}FAIL{RESET} result={result} expected={expec}")
