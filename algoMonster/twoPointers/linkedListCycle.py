class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head: ListNode) -> bool:
    slow = head
    fast = head

    while fast and fast.next:

        slow = slow.next 
        fast = fast.next.next

        if fast == slow:

            return True 

    return False


def build_linked_list(values: list[int], pos: int = -1) -> ListNode:
    """
    Builds a linked list from values.
    If pos >= 0, creates a cycle by connecting the last node to the node at index pos.
    """
    if not values:
        return None
    
    head = ListNode(values[0])
    curr = head
    nodes = [head]
    
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
        nodes.append(curr)
    
    if pos >= 0 and pos < len(nodes):
        curr.next = nodes[pos]
    
    return head


inputs = [
    ([1, 2, 3, 4], 0, True),
    ([1, 2, 3, 4], 1, True),
    ([1, 2, 3, 4], -1, False),
    ([1, 2], 0, True),
    ([1], -1, False), 
    ([1, 2, 3], 2, True),
    ([], -1, False),
]


GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (values, pos, expected) in enumerate(inputs, start=1):
    head = build_linked_list(values, pos)
    result = has_cycle(head)
    
    if result == expected:
        print(f"example: {idx} => {result} == {expected} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} != {expected} => {RED}FAIL{RESET}")
