class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# Example 1
# Input: root = [3,1,4,null,2], k = 1
#
# Level-order: [3, 1, 4, null, 2]
#
#     3
#    / \
#   1   4
#    \
#     2
#
root1 = TreeNode(3)
root1.left = TreeNode(1)
root1.right = TreeNode(4)
root1.left.right = TreeNode(2)
k1 = 1

# Example 2
# Input: root = [5,3,6,2,4,null,null,1], k = 3
#
# Level-order: [5, 3, 6, 2, 4, null, null, 1]
#
#         5
#        / \
#       3   6
#      / \
#     2   4
#    /
#   1
#
root2 = TreeNode(5)
root2.left = TreeNode(3)
root2.right = TreeNode(6)
root2.left.left = TreeNode(2)
root2.left.right = TreeNode(4)
root2.left.left.left = TreeNode(1)
k2 = 3

# Pack examples for tests
example_cases = [
    (root1, k1, 1),
    (root2, k2, 3),
]

def kthSmall(root: TreeNode, k: int) -> int:
    stack = []
    cur = root

    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        k -= 1
        if k == 0:
            return cur.val
        cur = cur.right


GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (root, k, expec)in enumerate(example_cases, start = 1):
    result = kthSmall(root, k)
    if result == expec:
        print(f"Example {idx}: {GREEN}PASS{RESET} output=>{result}, expected=>{expec}")
    else:
        print(f"Example {idx}: {RED}FAIL{RESET} output=>{result}, expected=>{expec}")
