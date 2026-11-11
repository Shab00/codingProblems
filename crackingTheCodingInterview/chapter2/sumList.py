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

def sum_lists(l1: Node, l2: Node) -> Node:
    
    p1, p2 = l1, l2
    dummy = Node(None)
    result = dummy
    carry = 0

    while p1 is not None or p2 is not None or carry:

        d1 = p1.data if p1 is not None else 0
        d2 = p2.data if p2 is not None else 0

        total = d1 + d2 + carry
        digit = total % 10
        carry = total // 10
        result.next = Node(digit)

        result = result.next

        if p1 is not None:
            p1 = p1.next
        if p2 is not None:
            p2 = p2.next

    return dummy.next


def sum_lists_forward(l1: Node, l2: Node) -> Node:
    # follow-up: forward order
    pass

GREEN, RED, RESET = "\033[92m", "\033[91m", "\033[0m"

tests = [
    # (l1 digits, l2 digits, expected digits)   — all in REVERSE order

    # 1. Book example: 617 + 295 = 912
    ([7, 1, 6], [5, 9, 2], [2, 1, 9]),

    # 2. Zero plus zero
    ([0], [0], [0]),

    # 3. Single digits, no carry: 1 + 2 = 3
    ([1], [2], [3]),

    # 4. Carry creates a new digit: 5 + 5 = 10
    ([5], [5], [0, 1]),

    # 5. Carry ripples all the way: 999 + 1 = 1000
    ([9, 9, 9], [1], [0, 0, 0, 1]),

    # 6. Same, other way round: 1 + 999 = 1000
    ([1], [9, 9, 9], [0, 0, 0, 1]),

    # 7. Classic example: 342 + 465 = 807
    ([2, 4, 3], [5, 6, 4], [7, 0, 8]),

    # 8. Adding zero: 321 + 0 = 321
    ([1, 2, 3], [0], [1, 2, 3]),

    # 9. Carry every step: 99 + 99 = 198
    ([9, 9], [9, 9], [8, 9, 1]),

    # 10. Trailing digits: 10 + 10 = 20
    ([0, 1], [0, 1], [0, 2]),

    # 11. Different lengths: 3 + 654 = 657
    ([3], [4, 5, 6], [7, 5, 6]),

    # 12. Short plus long with a carry chain: 9 + 9999 = 10008
    ([9], [9, 9, 9, 9], [8, 0, 0, 0, 1]),
]

for i, (a, b, expected) in enumerate(tests, 1):
    result = to_list(sum_lists(build_list(a), build_list(b)))
    if result == expected:
        print(f"Test {i}: {GREEN}PASS{RESET}")
    else:
        print(f"Test {i}: {RED}FAIL{RESET}  {a} + {b}: expected {expected}, got {result}")

forward_tests = [
    # (l1 digits, l2 digits, expected digits)   — all in FORWARD order

    # 1. Book example: 617 + 295 = 912
    ([6, 1, 7], [2, 9, 5], [9, 1, 2]),

    # 2. Zero plus zero
    ([0], [0], [0]),

    # 3. Carry creates a new digit: 5 + 5 = 10
    ([5], [5], [1, 0]),

    # 4. Carry ripples all the way: 999 + 1 = 1000
    ([9, 9, 9], [1], [1, 0, 0, 0]),

    # 5. Same, other way round
    ([1], [9, 9, 9], [1, 0, 0, 0]),

    # 6. 342 + 465 = 807
    ([3, 4, 2], [4, 6, 5], [8, 0, 7]),

    # 7. Different lengths: 123 + 4 = 127
    ([1, 2, 3], [4], [1, 2, 7]),

    # 8. Carry every step: 99 + 99 = 198
    ([9, 9], [9, 9], [1, 9, 8]),

    # 9. Different lengths: 654 + 3 = 657
    ([6, 5, 4], [3], [6, 5, 7]),

    # 10. Long carry chain: 9999 + 9 = 10008
    ([9, 9, 9, 9], [9], [1, 0, 0, 0, 8]),
]

#for i, (a, b, expected) in enumerate(forward_tests, 1):
#    result = to_list(sum_lists_forward(build_list(a), build_list(b)))
#    if result == expected:
#        print(f"Forward {i}: {GREEN}PASS{RESET}")
#    else:
#        print(f"Forward {i}: {RED}FAIL{RESET}  {a} + {b}: expected {expected}, got {result}")
