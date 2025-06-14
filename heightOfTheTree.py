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

def solve(root: TreeNode) -> int:
    pass

result = solve(root)

print(result)

