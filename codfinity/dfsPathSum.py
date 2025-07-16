class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(10)

def treeList(root: TreeNode, path: None):

    if path is None:
        path = []
    if not root:
        return
    path.append(root.val)
    if not root.left and not root.right:
        print(path)
    else:
        treeList(root.left, path[:])
        treeList(root.right, path[:])


def pathSum(root: TreeNode, target: int):
    if not root:
        return False

    if not root.left and not root.right:
        return root.val == target

    return (pathSum(root.left, target - root.val) or
            pathSum(root.right, target - root.val))

target = [22, 26, 18]

for x in target:
    result = pathSum(root, x)
    print(result)

result = treeList(root, [])
print(result)
