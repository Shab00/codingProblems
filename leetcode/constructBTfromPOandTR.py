from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# Example 1
# Input:
#   preorder = [3,9,20,15,7]
#   inorder  = [9,3,15,20,7]
# Output tree (level-order representation): [3,9,20,null,null,15,7]
#
# Level-order: [3, 9, 20, null, null, 15, 7]
#
#     3
#    / \
#   9  20
#      / \
#     15  7
#
pre1 = [3,9,20,15,7]
ino1 = [9,3,15,20,7]
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)

# Example 2
# Input:
#   preorder = [-1]
#   inorder  = [-1]
# Output tree (level-order): [-1]
#
# Tree:
#  -1
#
pre2 = [-1]
ino2 = [-1]
root2 = TreeNode(-1)

example_cases = [
    (pre1, ino1, root1),  # Example 1: (preorder, inorder, expected_root)
    (pre2, ino2, root2),  # Example 2
]

def buildTree(pre: list, ino: list) -> TreeNode:

    preIdx = inIdx = 0
    def dfs(limit):
        nonlocal preIdx, inIdx
        if preIdx >= len(pre):
            return None
        if ino[inIdx] == limit:
            inIdx += 1
            return None

        root = TreeNode(pre[preIdx])
        preIdx += 1
        root.left = dfs(root.val)
        root.right = dfs(limit)
        return root
    return dfs(float('inf'))
    

def is_same_tree(a: TreeNode, b: TreeNode) -> bool:
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    if a.val != b.val:
        return False
    return is_same_tree(a.left, b.left) and is_same_tree(a.right, b.right)

def serialize_tree(root: TreeNode) -> list:
    if root is None:
        return []
    q = deque([root])
    out = []
    while q:
        node = q.popleft()
        if node is None:
            out.append(None)
            continue
        out.append(node.val)
        q.append(node.left)
        q.append(node.right)
    while out and out[-1] is None:
        out.pop()
    return out

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (pre, ino, expec) in enumerate(example_cases, start = 1):
    result = buildTree(pre, ino)
    if is_same_tree(result, expec):
        print(f"Example {idx}: {GREEN}PASS{RESET}")
    else:
        print(f"Example {idx}: {RED}FAIL{RESET}")
        print("  expected (level-order):", serialize_tree(expec))
        print("  got      (level-order):", serialize_tree(result))
