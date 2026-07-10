class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(tree: Node) -> bool:
    # WRITE YOUR BRILLIANT CODE HERE
    return False


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
    ([1, 2, 3, 4, None, None, None], False),
    ([1, 2, 3, None, 4, None, None], False),
    ([1, 2, 3, 4, 5, 6, 7], True),
    ([1, 2, None, 3, None, None, None], False),
    ([1, None, 2, None, 3, None, None], False),
    ([1, 2, 3, None, None, 4, 5], False),
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
