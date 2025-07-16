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

def solve(root: TreeNode, num: int) -> bool:
    if not root:
        return False 
    
    if root.left == None and root.right == None:
        if root.val == num:
            return True
        else:
            return False


    num -= root.val

    return solve(root.left, num) or solve(root.right, num)

num = 30
result = solve(root, num)
print(result)
