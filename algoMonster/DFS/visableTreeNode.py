class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def visible_tree_node(root: Node) -> int:
    def dfs(root, max_sofar):
        if not root:
            return 0

        total = 0
        if root.val >= max_sofar:
            total += 1

        new_max = max(max_sofar, root.val)
        total += dfs(root.left, new_max)
        total += dfs(root.right, new_max)

        return total

    result = dfs(root, float('-inf'))
    return result

def build_tree_from_list(values, index=0):
    if not values or index >= len(values) or values[index] is None:
        return None
    
    root = Node(values[index])
    root.left = build_tree_from_list(values, 2 * index + 1)
    root.right = build_tree_from_list(values, 2 * index + 2)
    return root


inputs = [
    ([1, 2, 3, None, None, None, None], 3),
    ([1], 1),
    ([], 0),
]

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (values, expected) in enumerate(inputs, start=1):
    root = build_tree_from_list(values) if values else None
    result = visible_tree_node(root)
    
    if result == expected:
        print(f"example: {idx} => {result} == {expected} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} != {expected} => {RED}FAIL{RESET}")
