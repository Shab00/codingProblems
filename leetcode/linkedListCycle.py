class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head: ListNode) -> bool:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

def list_to_linkedlist_with_cycle(lst, pos):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    nodes = [head]
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
        nodes.append(current)
    if pos != -1:
        current.next = nodes[pos]
    return head

test_cases = [
    ([3,2,0,-4], 1),
    ([1,2], 0),
    ([1], -1)
]

for case, position in test_cases:
    head = list_to_linkedlist_with_cycle(case, position)
    cycle = hasCycle(head)
    print(f"Input: {case}, cycle at: {position} -> Has cycle? {cycle}")
