class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_max_depth(root: Node) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    def dfs(root):
        if not root:
            return 0
        left = dfs(root.left)
        right = dfs(root.right)
        return max(left, right) + 1

    if not root:
        return 0
    depth = dfs(root) - 1
    return depth

def build_tree_from_list(values, index=0):
    if not values or index >= len(values) or values[index] is None:
        return None
    
    root = Node(values[index])
    root.left = build_tree_from_list(values, 2 * index + 1)
    root.right = build_tree_from_list(values, 2 * index + 2)
    return root


inputs = [
    ([1, 2, 3, None, None, None, None], 1),
    ([1, 2, 3, 4, None, None, None], 2),
    ([1], 0),
    ([], 0),
    ([1, 2, None, 3, None, None, None], 2),
    ([1, 2, 3, 4, 5, None, None], 2),
]

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (values, expected) in enumerate(inputs, start=1):
    root = build_tree_from_list(values) if values else None
    result = tree_max_depth(root)
    
    if result == expected:
        print(f"example: {idx} => {result} == {expected} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} != {expected} => {RED}FAIL{RESET}")
