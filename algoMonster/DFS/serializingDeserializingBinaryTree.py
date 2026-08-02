class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    def dfs(node, res):
        if node is None:
            res.append("x")
            return
        res.append(str(node.val))
        dfs(node.left, res)
        dfs(node.right, res)
    
    result = []
    dfs(root, result)
    return " ".join(result)


def deserialize(s):
    def dfs(nodes):
        val = next(nodes)
        if val == "x":
            return None
        node = Node(int(val))
        node.left = dfs(nodes)
        node.right = dfs(nodes)
        return node
    
    return dfs(iter(s.split()))


if __name__ == "__main__":
    def build_tree_from_level_order(values, idx=0):
        if not values or idx >= len(values) or values[idx] is None:
            return None
        root = Node(values[idx])
        root.left = build_tree_from_level_order(values, 2*idx+1)
        root.right = build_tree_from_level_order(values, 2*idx+2)
        return root
    
    def tree_to_preorder_string(root):
        def helper(node):
            if not node:
                return ["x"]
            return [str(node.val)] + helper(node.left) + helper(node.right)
        return " ".join(helper(root))
    
    test_cases = [
        [1, 2, 3],
        [1, 2, 3, 4, 5],
        [1],
        [],
        [1, 2, None, 3],
        [1, None, 2, None, 3],
    ]
    
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"
    
    for idx, level_vals in enumerate(test_cases, start=1):
        root = build_tree_from_level_order(level_vals) if level_vals else None
        serialized = serialize(root)
        deserialized_root = deserialize(serialized)
        serialized_again = serialize(deserialized_root)
        
        if serialized == serialized_again:
            print(f"test {idx}: round-trip OK => {GREEN}PASS{RESET}")
        else:
            print(f"test {idx}: round-trip FAIL => {RED}FAIL{RESET}")
            print(f"  original serial: {serialized}")
            print(f"  re-serialized:   {serialized_again}")
