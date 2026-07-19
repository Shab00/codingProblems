class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def valid_bst(root: Node) -> bool:
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
    ([2, 1, 3], True),
    ([5, 1, 4, None, None, 3, 6], False),
    ([2, 2, 2], False),
    ([1], True),
    ([], True),
    ([10, 5, 15, None, None, 6, 20], False),
    ([10, 5, 15, 3, 7, 12, 20], True),
    ([5, 4, 6, None, None, 3, 7], False),
    ([1, None, 2, None, 3], True),
    ([3, 2, None, 1], True),
    ([5, 1, 6, None, None, 4, 7], False),
]

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (values, expected) in enumerate(inputs, start=1):
    root = build_tree_from_list(values) if values else None
    result = valid_bst(root)
    
    if result == expected:
        print(f"example: {idx} => {result} == {expected} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} != {expected} => {RED}FAIL{RESET}")
