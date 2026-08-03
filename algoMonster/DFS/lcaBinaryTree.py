class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lca(root: Node, node1: Node, node2: Node) -> Node:
    if root is None or root == node1 or root == node2:
        return root

    left = lca(root.left, node1, node2)
    right = lca(root.right, node1, node2)

    if left and right:
        return root

    return left if left else right


def build_tree_from_level_order(values, idx=0):
    if not values or idx >= len(values) or values[idx] is None:
        return None
    root = Node(values[idx])
    root.left = build_tree_from_level_order(values, 2*idx + 1)
    root.right = build_tree_from_level_order(values, 2*idx + 2)
    return root


def find_node(root, target_val):
    if root is None:
        return None
    if root.val == target_val:
        return root
    left = find_node(root.left, target_val)
    return left if left else find_node(root.right, target_val)


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
    ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1, 3),
    ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4, 5),
    ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 6, 4, 5),
    ([1, 2, 3], 2, 3, 1),
    ([1, 2, None], 2, 1, 1),
    ([1], 1, 1, 1),
]

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (level_vals, val1, val2, expected_val) in enumerate(inputs, start=1):
    root = build_tree_from_level_order(level_vals) if level_vals else None
    node1 = find_node(root, val1)
    node2 = find_node(root, val2)
    result_node = lca(root, node1, node2)
    result_val = result_node.val if result_node else None

    if result_val == expected_val:
        print(f"test {idx}: LCA({val1}, {val2}) = {result_val} => {GREEN}PASS{RESET}")
    else:
        print(f"test {idx}: LCA({val1}, {val2}) = {result_val} != {expected_val} => {RED}FAIL{RESET}")
