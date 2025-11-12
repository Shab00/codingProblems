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

def invertTree(root: TreeNode) -> TreeNode:
    if not root:
        return []

    stack = []
    node = root
    stack.append(node)
    while stack:
        cur = stack.pop()
        print(cur.val)
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)

result = invertTree(root)
print(result)
