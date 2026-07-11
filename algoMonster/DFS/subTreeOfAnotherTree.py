class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_same_tree(tree1, tree2):
    result = False
    if tree1 is None and tree2 is None:
        result = True
    elif tree1 is None or tree2 is None:
        result = False
    elif tree1.val != tree2.val:
        result = False
    elif not is_same_tree(tree1.left, tree2.left):
        result = False
    else:
        result = is_same_tree(tree1.right, tree2.right)
    return result

def subtree_of_another_tree(root: Node, sub_root: Node) -> bool:
    result = False
    if sub_root is None:
        result = True
    elif root is None:
        result = False
    elif is_same_tree(root, sub_root):
        result = True
    elif subtree_of_another_tree(root.left, sub_root):
        result = True
    else:
        result = subtree_of_another_tree(root.right, sub_root)
    return result

def build_tree_from_list(values, index=0):
    if not values or index >= len(values) or values[index] is None:
        return None
    
    root = Node(values[index])
    root.left = build_tree_from_list(values, 2 * index + 1)
    root.right = build_tree_from_list(values, 2 * index + 2)
    return root


inputs = [
    ([1, 2, 3], [2], True),
    ([1, 2, 3], [4], False),
    ([1, 2, 3, 4, 5], [2, 4, 5], True),
    ([1, 2, 3, 4, 5], [2, 4, None], False),
    ([1, 2, 3, 4, 5], [2, None, 4], False),
    ([1, 2, 3], [], True),
    ([], [], True),
    ([1, 2, 3, 4], [1, 2, 3, 4], True),
]

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (root_vals, sub_vals, expected) in enumerate(inputs, start=1):
    root = build_tree_from_list(root_vals) if root_vals else None
    sub_root = build_tree_from_list(sub_vals) if sub_vals else None
    result = subtree_of_another_tree(root, sub_root)
    
    if result == expected:
        print(f"example: {idx} => {result} == {expected} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} != {expected} => {RED}FAIL{RESET}")
