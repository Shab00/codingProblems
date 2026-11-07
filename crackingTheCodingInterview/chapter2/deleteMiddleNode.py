class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def append_to_tail(self, data):
        end = Node(data)
        n = self
        while n.next is not None:
            n = n.next
        n.next = end


def build_list(values):
    if not values:
        return None
    head = Node(values[0])
    for v in values[1:]:
        head.append_to_tail(v)
    return head

def to_list(head):
    out = []
    while head is not None:
        out.append(head.data)
        head = head.next
    return out

def get_node(head, index):
    """Return the node at this position (0-based)."""
    for _ in range(index):
        head = head.next
    return head

def delete_middle_node(node: Node) -> bool:
    if node is None or node.next is None:
        return False

    next_node = node.next
    node.data = next_node.data
    node.next = next_node.next
    return True

    

GREEN, RED, RESET = "\033[92m", "\033[91m", "\033[0m"

tests = [
    # (values, index of node to delete, expected list, expected return)

    # 1. Book example
    (["a", "b", "c", "d", "e", "f"], 2, ["a", "b", "d", "e", "f"], True),

    # 2. Shortest valid list
    ([1, 2, 3], 1, [1, 3], True),

    # 3. Exact middle
    ([1, 2, 3, 4, 5], 2, [1, 2, 4, 5], True),

    # 4. Second node
    ([1, 2, 3, 4, 5], 1, [1, 3, 4, 5], True),

    # 5. Second to last node
    ([1, 2, 3, 4, 5], 3, [1, 2, 3, 5], True),

    # 6. Duplicate value earlier in the list
    ([1, 2, 3, 2, 4], 3, [1, 2, 3, 4], True),

    # 7. All the same value
    ([5, 5, 5], 1, [5, 5], True),

    # 8. Strings
    (["x", "y", "z"], 1, ["x", "z"], True),

    # 9. Longer list
    (list(range(1, 11)), 5, [1, 2, 3, 4, 5, 7, 8, 9, 10], True),

    # 10. Last node: can't delete
    ([1, 2, 3], 2, [1, 2, 3], False),

    # 11. None passed in
    ([1, 2, 3], None, [1, 2, 3], False),
]

for i, (values, index, expected_list, expected_return) in enumerate(tests, 1):
    head = build_list(values)
    node = None if index is None else get_node(head, index)
    returned = delete_middle_node(node)
    result = to_list(head)
    if result == expected_list and returned == expected_return:
        print(f"Test {i}: {GREEN}PASS{RESET}")
    else:
        print(f"Test {i}: {RED}FAIL{RESET}  expected {expected_list} / {expected_return}, "
              f"got {result} / {returned}")
