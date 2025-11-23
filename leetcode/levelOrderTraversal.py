from collections import deque

class TreeNode:
    def __init__(self, val = 0, right = None, left = None):
        self.val = val
        self.right = right
        self.left = left



# Test case 1
#    3
#   / \
#  9  20
#     / \
#    15  7

root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)

#Test case 2
#   1
root2 = TreeNode(1)

#Test case 3
root3 = TreeNode(None)

inputs = [(root1, [[3],[9,20],[15,7]]),
          (root2, [[1]]),
          (root3, [[None]])]

def levelOrder(root: TreeNode) -> list:
    if root is None:
        return []

    q = deque([root])
    result = []

    while q:
        levelLength = len(q)
        level = []
        for _ in range(levelLength):
            cur = q.popleft()
            level.append(cur.val)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        result.append(level)
    return result
        

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (root, expec) in enumerate(inputs, start=1):
    result = levelOrder(root)
    if result == expec:
        print(f"Test {idx}: {GREEN}PASS{RESET} result={result} expected={expec}")
    else:
        print(f"Test {idx}: {RED}FAIL{RESET} result={result} expected={expec}")
