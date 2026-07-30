class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lca_on_bst(bst: Node, p: int, q: int) -> int:
    current = bst
    while current:
        if p < current.val and q < current.val:
            current = current.left
        elif p > current.val and q > current.val:
            current = current.right
        else:
            return current.val
    return 0


def build_tree_from_list(values, index=0):
    if not values or index >= len(values) or values[index] is None:
        return None
    root = Node(values[index])
    root.left = build_tree_from_list(values, 2 * index + 1)
    root.right = build_tree_from_list(values, 2 * index + 2)
    return root


inputs = [
    ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8, 6),
    ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 3, 5, 4),
    ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 4, 2),
    ([2, 1, 3], 1, 3, 2),
    ([2, 1, 3], 1, 2, 2),
    ([5, 3, 7, 2, 4, 6, 8], 2, 8, 5),
    ([5, 3, 7, 2, 4, 6, 8], 2, 4, 3),
    ([5, 3, 7, 2, 4, 6, 8], 6, 8, 7),
    ([1], 1, 1, 1),
]

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (values, p, q, expected) in enumerate(inputs, start=1):
    root = build_tree_from_list(values) if values else None
    result = lca_on_bst(root, p, q)
    if result == expected:
        print(f"example: {idx} => {result} == {expected} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} != {expected} => {RED}FAIL{RESET}")
