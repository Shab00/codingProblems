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

def solve(root: TreeNode) -> int:
    if not root:
        return []
    height = 0
    queue = deque([root])
    result = []
    while queue:
        level_size = len(queue)
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
        height += 1
    return height

        
        

result = solve(root)

print(result)

