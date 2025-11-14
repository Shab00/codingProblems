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

def diameterDFS(root: TreeNode) -> int:
    if not root:
        return 0


def diameterBFS(root: TreeNode) -> int:
    if not root:
        return 0

resultDFS = diameterDFS(root)
resultBFS = diameterBFS(root)
print(
        f"resultDFS: {resultDFS}\n"
        f"resultBFS: {resultBFS}\n"
        )
