class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(tree: Node) -> bool:
    # WRITE YOUR BRILLIANT CODE HERE
    def dfs(node):
        if node is None:
            return (-1, True)
        left_height, left_balanced = dfs(node.left)
        right_height, right_balanced = dfs(node.right)
        
        is_balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
        
        height = 1 + max(left_height, right_height)
        
        return (height, is_balanced)

    if tree is None:
        return True
    h, i = dfs(tree)
    return i


def build_tree_from_list(values, index=0):
    if not values or index >= len(values) or values[index] is None:
        return None
    
    root = Node(values[index])
    root.left = build_tree_from_list(values, 2 * index + 1)
    root.right = build_tree_from_list(values, 2 * index + 2)
    return root


inputs = [
    ([], True),
    ([1], True),
    ([1, 2, 3], True),
    ([1, 2, 3, 4, 5, 6, 7], True),
    ([1, 2, None, 3, None, None, None], False),
]

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (values, expected) in enumerate(inputs, start=1):
    root = build_tree_from_list(values) if values else None
    result = is_balanced(root)
    
    if result == expected:
        print(f"example: {idx} => {result} == {expected} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} != {expected} => {RED}FAIL{RESET}")
