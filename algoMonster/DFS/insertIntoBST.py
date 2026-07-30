class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert_bst(bst: Node, val: int) -> Node:
    if bst is None:
        return Node(val)

    if val == bst.val:
        return bst

    if val < bst.val:
        bst.left = insert_bst(bst.left, val)
    else:
        bst.right = insert_bst(bst.right, val)

    return bst

def build_tree_from_list(values, index=0):
    if not values or index >= len(values) or values[index] is None:
        return None
    root = Node(values[index])
    root.left = build_tree_from_list(values, 2 * index + 1)
    root.right = build_tree_from_list(values, 2 * index + 2)
    return root


def tree_to_list(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


inputs = [
    ([2, 1, 3], 4, [2, 1, 3, None, None, None, 4]),
    ([2, 1, 3], 0, [2, 1, 3, 0]),
    ([2, 1, 3], 2, [2, 1, 3]),
    ([], 5, [5]),
    ([5, 3, 7, 2, 4, 6, 8], 9, [5, 3, 7, 2, 4, 6, 8, None, None, None, None, None, None, None, 9]),
    ([5, 3, 7, 2, 4, 6, 8], 1, [5, 3, 7, 2, 4, 6, 8, 1]),
]

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (values, val, expected) in enumerate(inputs, start=1):
    root = build_tree_from_list(values) if values else None
    result_root = insert_bst(root, val)
    result_list = tree_to_list(result_root)
    if result_list == expected:
        print(f"example: {idx} => {result_list} == {expected} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result_list} != {expected} => {RED}FAIL{RESET}")
