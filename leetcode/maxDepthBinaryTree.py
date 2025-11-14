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

def maxDepthTreeDFS(root: TreeNode) -> int:
    if not root:
        return 0
    stack = [(root, 1)]
    maxDepth = 0
    while stack:
        cur, curDep = stack.pop()
        maxDepth = max(maxDepth, curDep)
        if cur.right:
            stack.append((cur.right, curDep + 1))
        if cur.left:
            stack.append((cur.left, curDep + 1))

    return maxDepth

def invertTreeBFS(root: TreeNode) -> int:
    pass

result = maxDepthTreeDFS(root)
print(result)
