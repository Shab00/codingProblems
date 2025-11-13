from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(7)
root.right.right = TreeNode(9)
root.right.left = TreeNode(6)

def invertTreeDFS(root: TreeNode) -> TreeNode:
    if not root:
        return None

    stack = [root]
    while stack:
        cur = stack.pop()
        cur.left, cur.right = cur.right, cur.left
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)
    return root 

def invertTreeBFS(root: TreeNode) -> TreeNode:
    if not root:
        return None

    q = deque([root])
    while q:
        cur = q.popleft()
        cur.left, cur.right = cur.right, cur.left
        if cur.right:
            q.append(cur.right)
        if cur.left:
            q.append(cur.left)
    return root

def print_level(root):
    if not root:
        print([])
        return
    q = deque([root])
    out = []
    while q:
        n = q.popleft()
        out.append(n.val)
        if n.left: q.append(n.left)
        if n.right: q.append(n.right)
    print(out)

resultDFS = invertTreeDFS(root)
resultBFS = invertTreeBFS(root)
print_level(resultDFS)
print_level(resultBFS)
