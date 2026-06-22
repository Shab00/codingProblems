inputs = [
    ([1, 2, 3, 4], 1, [1, 2, 3]),
    ([1, 2, 3, 4], 2, [1, 2, 4]),
    ([1, 2, 3, 4], 4, [2, 3, 4]),
    ([1], 1, []),
    ([1, 2], 1, [1]),
    ([1, 2], 2, [2]),
]

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def remove_nth_from_end(head, n):
    length = 0
    node = head
    while node:
       node = node.next
       length += 1
    if length == n:
        return head.next
    cut = (length - n) - 1
    cur = head
    for i in range(cut):
        cur = cur.next
    cur.next = cur.next.next
    return head

def build_linked_list(arr: list[int]) -> Node:
    if not arr:
        return None

    head = Node(arr[0])
    current = head

    for value in arr[1:]:
        current.next = Node(value)
        current = current.next

    return head

def linked_list_to_list(head: Node) -> list[int]:
    result = []
    current = head

    while current is not None:
        result.append(current.val)
        current = current.next

    return result

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (arr, n, expec) in enumerate(inputs, start=1):
    head = build_linked_list(arr)
    result_head = remove_nth_from_end(head, n)
    result = linked_list_to_list(result_head)

    if result == expec:
        print(f"example: {idx} => {result} == {expec} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} != {expec} => {RED}FAIL{RESET}")
