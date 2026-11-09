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

def partition(head: Node, x: int) -> Node:

    pointer = head
    small_head = small_tail = None
    big_head = big_tail = None
    
    if pointer is None:
        return

    while pointer is not None:

        if pointer.data < x:
            if small_head is None:
                small_head = small_tail = pointer
            else:
                small_tail.next = pointer
                small_tail = pointer 

        else:
            if big_head is None:
                big_head = big_tail = pointer
            else:
                big_tail.next = pointer
                big_tail = pointer


        pointer = pointer.next

    if big_tail is not None:
        big_tail.next = None

    if small_head is None:
        return big_head

    small_tail.next = big_head
    return small_head       
        


GREEN, RED, RESET = "\033[92m", "\033[91m", "\033[0m"

def is_partitioned(values, x):
    seen_big = False
    for v in values:
        if v >= x:
            seen_big = True
        elif seen_big:          # a small value after a big one
            return False
    return True

tests = [
    # (values, x)

    # 1. Book example
    ([3, 5, 8, 5, 10, 2, 1], 5),

    # 2. Empty list
    ([], 5),

    # 3. Single small node
    ([1], 5),

    # 4. Single big node
    ([7], 5),

    # 5. All smaller than x
    ([1, 2, 3], 5),

    # 6. All bigger than x
    ([6, 7, 8], 5),

    # 7. All equal to x
    ([5, 5, 5], 5),

    # 8. Head is big, so the head must change
    ([9, 1], 5),

    # 9. Already partitioned
    ([1, 9], 5),

    # 10. Alternating
    ([5, 1, 5, 1], 5),

    # 11. x is in the list
    ([3, 1, 2], 2),

    # 12. Negatives and zero
    ([-1, 4, -5, 0], 0),

    # 13. x smaller than everything
    ([3, 4, 5], 1),

    # 14. x bigger than everything
    ([3, 4, 5], 10),

    # 15. Duplicates on both sides
    ([4, 1, 4, 1, 4], 3),

    # 16. Long list in reverse order
    (list(range(20, 0, -1)), 10),
]

for i, (values, x) in enumerate(tests, 1):
    head = build_list(values)
    new_head = partition(head, x)
    result = to_list(new_head)
    same_values = sorted(result) == sorted(values)
    if same_values and is_partitioned(result, x):
        print(f"Test {i}: {GREEN}PASS{RESET}")
    else:
        print(f"Test {i}: {RED}FAIL{RESET}  x={x}, input {values}, got {result}")
