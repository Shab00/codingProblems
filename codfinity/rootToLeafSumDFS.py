class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

def sum(node: TreeNode, num_so_far: int) -> int:
    if not node:
        return 0
    num_so_far = num_so_far * 10 + node.val
    if not node.left and not node.right:
        return num_so_far

    return sum(node.left, num_so_far) + sum(node.right, num_so_far)
   

result = sum(root, 0)
print(result)
