from collections import deque

class TreeNode:
    def __init__(self, val = 0, right = None, left= None):
        self.val = val
        self.right = right
        self.left = left

#Example 1:

#Input: root = [1,2,3]  
#Output: [1,3]

#Tree:
#  1
# / \
#2   3

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)

#Example 2:

#Input: root = [1,2,3,4,5,6,7]  
#Output: [1,3,7]

#Tree:
#       1
#     /   \
#    2     3
#   / \   / \
#  4  5  6  7
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)
root2.right = TreeNode(3)
root2.right.left = TreeNode(6)
root2.right.right = TreeNode(7)

inputs = [
        (root1, [1,2,3], [1,3]),
        (root2, [1,2,3,4,5,6,7], [1,3,7])
          ]

def rightSide(root: TreeNode) -> list[int]:
    if root is None:
        return []

    q = deque([root])
    result = []
    while q:

        levelLenght = len(q)
        level = []
        for _ in range(levelLenght):
            cur = q.popleft()
            level.append(cur.val)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        result.append(level[-1])

    return result


GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (root, inputs, expec) in enumerate(inputs, start=1):
    result = rightSide(root)
    if result == expec:
        print(f"Example {idx}: {GREEN}PASS{RESET} output=>{result}, expected=>{expec}")
    else:
        print(f"Example {idx}: {RED}FAIL{RESET} output=>{result}, expected=>{expec}")
