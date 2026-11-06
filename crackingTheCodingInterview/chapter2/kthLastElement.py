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

def kth_to_last(head: Node, k: int):
    
    if head is None:
        return

    length = 0
    walker = head

    while walker is not None:
        walker = walker.next
        length += 1

    target = length - k
    count = 0
    finder = head

    while finder is not None:
        if target == count:
            return finder.data

        finder = finder.next
        count += 1

GREEN, RED, RESET = "\033[92m", "\033[91m", "\033[0m"

tests = [
    # (values, k, expected)

    # 1. Last element
    ([1, 2, 3, 4, 5], 1, 5),

    # 2. Second to last
    ([1, 2, 3, 4, 5], 2, 4),

    # 3. Middle
    ([1, 2, 3, 4, 5], 3, 3),

    # 4. k equals the length (first element)
    ([1, 2, 3, 4, 5], 5, 1),

    # 5. k longer than the list
    ([1, 2, 3, 4, 5], 6, None),

    # 6. k is zero
    ([1, 2, 3, 4, 5], 0, None),

    # 7. k is negative
    ([1, 2, 3, 4, 5], -1, None),

    # 8. Empty list
    ([], 1, None),

    # 9. Single node, k = 1
    ([7], 1, 7),

    # 10. Single node, k too big
    ([7], 2, None),

    # 11. Two nodes, first one
    ([10, 20], 2, 10),

    # 12. Duplicate values
    ([1, 2, 1, 2], 2, 1),

    # 13. Strings
    (["a", "b", "c"], 1, "c"),

    # 14. Long list, first element
    (list(range(1, 101)), 100, 1),

    # 15. Long list, somewhere in the middle
    (list(range(1, 101)), 37, 64),
]

for i, (values, k, expected) in enumerate(tests, 1):
    head = build_list(values)
    result = kth_to_last(head, k)
    if result == expected:
        print(f"Test {i}: {GREEN}PASS{RESET}")
    else:
        print(f"Test {i}: {RED}FAIL{RESET}  expected {expected!r}, got {result!r}")
