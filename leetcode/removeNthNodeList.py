class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0, head)
    fast = dummy
    slow = dummy

    for _ in range(n + 1):
        if fast:
            fast = fast.next
        else:
            return head

    while fast:
        fast = fast.next
        slow = slow.next

    to_delete = slow.next
    if to_delete:
        slow.next = to_delete.next
        to_delete.next = None

    return dummy.next

def list_to_linkedlist(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linkedlist_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

test_cases = [
    ([1,2,3,4,5], 2),
    ([1], 1),
    ([1,2], 1)
]

for case, p in test_cases:
    head = list_to_linkedlist(case)
    remove = removeNthFromEnd(head, p)  
    output = linkedlist_to_list(remove)
    print(f"Input: {case, p} -> Output: {output}")
