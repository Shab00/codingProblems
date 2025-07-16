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

def count_leaves(root: TreeNode) -> int:
    if not root:
        return 0

    stack = [(root)] 
    leafNode = 0
    while stack:
        node = stack.pop()
        if node.left == None and node.right == None:
            leafNode += 1
        else:
            stack.append(node.left)
            stack.append(node.right)

    return leafNode


result = count_leaves(root)
print(result) 
