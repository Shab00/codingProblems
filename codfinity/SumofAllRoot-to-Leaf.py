from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
root.right.right.left = TreeNode(7)

def solve(root: TreeNode) -> int:
    if not root:
        return 0 

    result = 0 
    queue = deque([(root, root.val)])
    
    while queue:
      curNode, currentNum = queue.popleft() 
      if curNode.left is None and curNode.right is None:
          result += currentNum

      if curNode.left:
        queue.append((curNode.left, currentNum * 10 + curNode.left.val))
      if curNode.right:
        queue.append((curNode.right, currentNum * 10 + curNode.right.val))     
    return result

result = solve(root)
print(result)
