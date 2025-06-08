from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(3)
root.left = TreeNode(9)
root.left.left = TreeNode(4)
root.right = TreeNode(8)
root.right.left = TreeNode(1)
root.right.left.right = TreeNode(2)
root.right.right = TreeNode(7)

def solve(root: TreeNode) -> list:

    if not root:
        return []

    queue = deque([(root, 0)])
    columns = {}
    while queue:
        node, col = queue.popleft()
        if col not in columns:
            columns[col] = []
        columns[col].append(node.val)
        if node.left:
            queue.append((node.left, col - 1))
        if node.right:
            queue.append((node.right, col + 1))
    result = []
    for c in sorted(columns):
        result.append(columns[c])
    return result

result = solve(root)
print(result)
