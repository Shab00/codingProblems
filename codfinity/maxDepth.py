class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.right = TreeNode(7)
root.right.left = TreeNode(15)

def maxDepth(root: TreeNode) -> int:

    if not root:
        return 0

    stack = [(root, 1)] 
    maxDepth = 0
    while stack:
        node, curDep = stack.pop()
        maxDepth = max(maxDepth, curDep)
        if node.right:
            stack.append((node.right, curDep + 1))
        if node.left:
            stack.append((node.left, curDep + 1))

    return maxDepth

result = maxDepth(root)
print(result)
