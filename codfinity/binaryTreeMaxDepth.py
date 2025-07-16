class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val     
        self.left = left    
        self.right = right 

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

def solve(root: TreeNode) -> int:
    if not root:
        return 0

    stack = [(root, 1)]
    max_depth = 0
    while stack:
        node, depth = stack.pop()
        if node:
            max_depth = max(max_depth, depth)
            stack.append((node.left, depth + 1))
            stack.append((node.right, depth + 1))

    return max_depth

result = solve(root)
print(result)
