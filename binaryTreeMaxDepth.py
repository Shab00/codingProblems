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
    pass

result = solve(root)
print(result)
