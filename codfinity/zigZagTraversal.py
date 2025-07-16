from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode("A")
root.left = TreeNode("B")
root.right = TreeNode("C")
root.right.left = TreeNode("E")
root.right.right = TreeNode("F")
root.right.right.left = TreeNode("G")
root.left.left = TreeNode("D")

def solve(root: TreeNode) -> list:

    queue = deque([root])
    result = []
    layer = 0
    while queue:
        level = []
        levelLength = len(queue)
        for _ in range(levelLength):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if layer % 2 == 0:
            result.append(level)
        else:
            result.append(level[::-1])
        layer += 1
    return result
result = solve(root)
print(result)
