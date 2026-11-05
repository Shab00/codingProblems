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


def delete_node(head: Node, data) -> Node:
    """Delete the first node with this value. Returns the (possibly new) head."""
    if head is None:
        return None
    if head.data == data:
        return head.next          # head moved
    n = head
    while n.next is not None:
        if n.next.data == data:
            n.next = n.next.next  # skip over it
            return head
        n = n.next
    return head

def remove_dups(head: Node) -> None:
    if head is None:
        return

    seen = {head.data}
    prev = head
    current = head.next

    while current is not None:
        if current.data in seen:
            prev.next = current.next
        else:
            seen.add(current.data)
            prev = current
        current = current.next


GREEN, RED, RESET = "\033[92m", "\033[91m", "\033[0m"

def build_list(values):
    """Python list → linked list. Returns the head (None if empty)."""
    if not values:
        return None
    head = Node(values[0])
    for v in values[1:]:
        head.append_to_tail(v)
    return head

def to_list(head):
    """Linked list → Python list, so results are easy to compare."""
    out = []
    while head is not None:
        out.append(head.data)
        head = head.next
    return out

tests = [
    # (input, expected)

    # 1. Empty list
    ([], []),

    # 2. Single node
    ([1], [1]),

    # 3. No duplicates
    ([1, 2, 3], [1, 2, 3]),

    # 4. Two the same
    ([1, 1], [1]),

    # 5. Duplicate not next to each other
    ([1, 2, 1], [1, 2]),

    # 6. All the same
    ([1, 1, 1, 1], [1]),

    # 7. Book-style example
    ([3, 1, 3, 2, 1], [3, 1, 2]),

    # 8. Duplicate at the very end
    ([1, 2, 3, 3], [1, 2, 3]),

    # 9. First value repeated at the end
    ([5, 4, 3, 2, 1, 5], [5, 4, 3, 2, 1]),

    # 10. Pairs side by side
    ([2, 2, 3, 3, 4, 4], [2, 3, 4]),

    # 11. Repeating pattern
    ([1, 2, 1, 2, 1, 2], [1, 2]),

    # 12. Negatives and zero
    ([-1, 0, -1, 0], [-1, 0]),

    # 13. Strings
    (["a", "b", "a"], ["a", "b"]),

    # 14. Several duplicates spread out
    ([7, 8, 9, 7, 8, 9, 10], [7, 8, 9, 10]),
]

for i, (values, expected) in enumerate(tests, 1):
    head = build_list(values)
    remove_dups(head)               # should modify the list in place
    result = to_list(head)
    if result == expected:
        print(f"Test {i}: {GREEN}PASS{RESET}")
    else:
        print(f"Test {i}: {RED}FAIL{RESET}  expected {expected}, got {result}")
