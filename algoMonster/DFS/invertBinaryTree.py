class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_binary_tree(tree: Node) -> Node:
    def dfs(tree):
        if tree is None:
            return None
        
        tree.left, tree.right = tree.right, tree.left
        
        dfs(tree.left)
        dfs(tree.right)
        
        return tree

    if tree is None:
        return None

    return dfs(tree)


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
    ([1, 2, 3], [1, 3, 2]),
    ([1, 2, 3, 4, 5], [1, 3, 2, None, None, 5, 4]),
    ([1], [1]),
    ([], []),
    ([1, 2, None, 3], [1, None, 2, None, 3]),
    ([1, 2, 3, 4, 5, 6, 7], [1, 3, 2, 7, 6, 5, 4]),
]

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (values, expected) in enumerate(inputs, start=1):
    root = build_tree_from_list(values) if values else None
    result = invert_binary_tree(root)
    result_list = tree_to_list(result)
    
    if result_list == expected:
        print(f"example: {idx} => {result_list} == {expected} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result_list} != {expected} => {RED}FAIL{RESET}")
