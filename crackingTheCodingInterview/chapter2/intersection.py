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


def attach(values, tail):
    """Build a list from values, then hook its end onto tail."""
    if not values:
        return tail
    head = build_list(values)
    n = head
    while n.next is not None:
        n = n.next
    n.next = tail
    return head


def build_intersecting(a_values, b_values, shared_values):
    """Two lists sharing the same tail nodes. Returns (head_a, head_b, shared_head)."""
    shared = build_list(shared_values)
    return attach(a_values, shared), attach(b_values, shared), shared

def intersection(l1: Node, l2: Node) -> Node:

    nodes = set()

    while l1 is not None:
        nodes.add(l1)
        l1 = l1.next

    while l2 is not None:
        if l2 in nodes:
            return l2
        l2 = l2.next

    return None

GREEN, RED, RESET = "\033[92m", "\033[91m", "\033[0m"

tests = [
    # (A's own nodes, B's own nodes, shared tail)

    # 1. Book-style example
    ([3, 1, 5, 9], [4, 6], [7, 2, 1]),

    # 2. Same values but separate nodes: no intersection
    ([1, 2, 3], [1, 2, 3], []),

    # 3. Different lengths, no intersection
    ([1, 2, 3, 4, 5], [9], []),

    # 4. Meet only at the last node
    ([1, 2], [3], [9]),

    # 5. Same length before meeting
    ([1, 2], [3, 4], [5, 6]),

    # 6. A is entirely shared (A's head is the intersection)
    ([], [1, 2], [7, 8]),

    # 7. Both entirely shared (they're the same list)
    ([], [], [1, 2, 3]),

    # 8. Both empty
    ([], [], []),

    # 9. One empty, one not
    ([], [1, 2], []),

    # 10. Big difference in length
    (list(range(20)), [100], [5, 6, 7]),

    # 11. Repeated values: the right node is the shared one
    ([7, 7], [7], [7, 7]),

    # 12. Single shared node
    ([], [], [42]),
]

for i, (a_vals, b_vals, shared_vals) in enumerate(tests, 1):
    a, b, shared = build_intersecting(a_vals, b_vals, shared_vals)
    result = intersection(a, b)
    if result is shared:
        print(f"Test {i}: {GREEN}PASS{RESET}")
    else:
        got = None if result is None else result.data
        want = None if shared is None else shared.data
        print(f"Test {i}: {RED}FAIL{RESET}  expected node {want}, got node {got}")
