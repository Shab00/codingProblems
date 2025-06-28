class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)


def solve(root: TreeNode, num: int) -> list[list[int]]:

    def dfs(node, path, target, result):

        if not node:
            return

        path.append(node.val)
        if not node.left and not node.right:
            if node.val == target:
                result.append(list(path))

        else:
            dfs(node.left, path, target - node.val, result)
            dfs(node.right, path, target - node.val, result)
        path.pop()

    result = []
    dfs(root, [], num, result)
    return result

num = 22
result = solve(root, num)
print(result)
