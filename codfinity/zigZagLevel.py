from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

root = TreeNode(8)
root.left = TreeNode(4)
root.right = TreeNode(10)
root.left.left = TreeNode(2)
root.left.right = TreeNode(6)
root.right.right = TreeNode(20)

def solve(root: TreeNode) -> list:
    
    if not root:
        return []
    queue = deque([root])
    result = []
    step = 0
    while queue:
        levelSize = len(queue)
        level = []
        for _ in range(levelSize):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if step % 2 == 0:
            result.append(level)
        else:
            result.append(level[::-1])
        step += 1

    return result

result = solve(root)
print(result)
