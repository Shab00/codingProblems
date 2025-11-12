class TreeNode:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
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
    pass

result = invertTree(root)
print(result)
