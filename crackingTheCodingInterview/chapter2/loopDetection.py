class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def build_loop(values, loop_index):
    """
    Build a list from values. If loop_index isn't None, the last node
    points back to the node at that position (0-based).
    Returns (head, loop_start_node).
    """
    if not values:
        return None, None
    nodes = [Node(v) for v in values]
    for a, b in zip(nodes, nodes[1:]):
        a.next = b
    if loop_index is None:
        return nodes[0], None
    nodes[-1].next = nodes[loop_index]
    return nodes[0], nodes[loop_index]

def detect_loop(head: Node) -> Node:
    slow = fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break

    if fast is None or fast.next is None:
        return None

    slow = head
    while slow is not fast:
        slow = slow.next
        fast = fast.next

    return slow

GREEN, RED, RESET = "\033[92m", "\033[91m", "\033[0m"

tests = [
    # (values, index the last node points back to, or None for no loop)

    # 1. Book example: loop starts at C
    (["A", "B", "C", "D", "E"], 2),

    # 2. No loop
    ([1, 2, 3], None),

    # 3. Empty list
    ([], None),

    # 4. Single node, no loop
    ([1], None),

    # 5. Single node pointing to itself
    ([1], 0),

    # 6. Two nodes, loop back to the head
    ([1, 2], 0),

    # 7. Two nodes, last points to itself
    ([1, 2], 1),

    # 8. The whole list is a loop
    ([1, 2, 3, 4, 5], 0),

    # 9. Loop is just the last node pointing to itself
    ([1, 2, 3, 4, 5], 4),

    # 10. Long lead-in, short loop
    (list(range(20)), 17),

    # 11. Short lead-in, long loop
    (list(range(20)), 1),

    # 12. Repeated values: must return the right NODE
    ([7, 7, 7, 7], 2),

    # 13. Long list, no loop
    (list(range(50)), None),
]

for i, (values, loop_index) in enumerate(tests, 1):
    head, expected = build_loop(values, loop_index)
    result = detect_loop(head)
    if result is expected:
        print(f"Test {i}: {GREEN}PASS{RESET}")
    else:
        got = None if result is None else result.data
        want = None if expected is None else expected.data
        print(f"Test {i}: {RED}FAIL{RESET}  expected node {want}, got node {got}")
