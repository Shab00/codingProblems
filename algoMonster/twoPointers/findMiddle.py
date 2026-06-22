inputs = [
    ([0, 1, 2, 3, 4], 2),
    ([0, 1, 2, 3, 4, 5], 3),
]

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def middle_of_linked_list(head: Node) -> int:
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow.val

def build_linked_list(arr: list[int]) -> Node:
    if not arr:
        return None

    head = Node(arr[0])
    current = head

    for value in arr[1:]:
        current.next = Node(value)
        current = current.next

    return head

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (arr, expec) in enumerate(inputs, start=1):
    head = build_linked_list(arr)
    result = middle_of_linked_list(head)

    if result == expec:
        print(f"example: {idx} => {result} == {expec} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} != {expec} => {RED}FAIL{RESET}")
