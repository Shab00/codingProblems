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

def preorderTraversal(root: TreeNode) -> list[int]:
    if not root:
        return []

    stack = [root]
    result = [] 
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result

def inorderTraversal(root: TreeNode) -> list[int]:
    if not root:
        return []

    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)

def postorderTraversal(root: TreeNode) -> list[int]:
    if not root:
        return []

    return postorderTraversal(root.left) + postorderTraversal(root.right) + [root.val]

pre = preorderTraversal(root)
ino = inorderTraversal(root)
post = postorderTraversal(root)

pre = preorderTraversal(root)
print(pre,ino,post)
