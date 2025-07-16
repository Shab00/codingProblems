from collections import deque

class TreeNode:
   def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode("A")
root.left = TreeNode("B")
root.right = TreeNode("C")
root.right.left = TreeNode("E")
root.right.right = TreeNode("F")
root.right.right.left = TreeNode("G")
root.left.left = TreeNode("D")

def solve(root: TreeNode) -> list:
    if not root:
        return []

    queue = deque([root])
    result = []
    while queue:
        node = queue.popleft()

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        if not node.left and not node.right:
            result.append(node.val)
    return result

result = solve(root)
print(result)
