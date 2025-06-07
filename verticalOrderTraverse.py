from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.left.right = TreeNode(7)
root.right.right = TreeNode(6)

def solve(root: TreeNode) -> list:

    if not root:
        return []
    queue = deque([(root, 0)])
    result = []
    columns = {}
    while queue:
        
        node, col = queue.popleft()
        queue([(root.left, -1), (root.right, 1)])


result = solve(root)
print(result)
