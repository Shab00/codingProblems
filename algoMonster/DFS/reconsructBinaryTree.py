class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def construct_binary_tree(preorder: list[int], inorder: list[int]) -> Node:
    inorder_index = {val: i for i, val in enumerate(inorder)}
    
    def build(pre_left, pre_right, in_left, in_right):
        if pre_left > pre_right or in_left > in_right:
            return None
        
        root_val = preorder[pre_left]
        root = Node(root_val)
        
        root_in_idx = inorder_index[root_val]
        
        left_size = root_in_idx - in_left
        
        root.left = build(
            pre_left + 1,
            pre_left + left_size,
            in_left,
            root_in_idx - 1
        )
        
        root.right = build(
            pre_left + left_size + 1,
            pre_right,
            root_in_idx + 1,
            in_right   
        )
        
        return root
    
    return build(0, len(preorder)-1, 0, len(inorder)-1)


def format_tree(node):
    if node is None:
        yield "x"
        return
    yield str(node.val)
    yield from format_tree(node.left)
    yield from format_tree(node.right)


def build_tree_from_list(values, index=0):
    if not values or index >= len(values) or values[index] is None:
        return None
    root = Node(values[index])
    root.left = build_tree_from_list(values, 2 * index + 1)
    root.right = build_tree_from_list(values, 2 * index + 2)
    return root


inputs = [
    ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7], [3, 9, 20, None, None, 15, 7]),  # Example
    ([1, 2, 3], [3, 2, 1], [1, 2, None, 3]),  # Skewed left
    ([1, 2, 3], [1, 2, 3], [1, None, 2, None, 3]),  # Skewed right
    ([1], [1], [1]),  # Single node
]

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

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

for idx, (pre, ino, expected_level) in enumerate(inputs, start=1):
    root = construct_binary_tree(pre, ino)
    result_level = tree_to_list(root)
    if result_level == expected_level:
        print(f"example: {idx} => {result_level} == {expected_level} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result_level} != {expected_level} => {RED}FAIL{RESET}")
