class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    prev = None
    curr = head 
    while curr:
        print(f"curr: {curr.val}, prev: {prev.val if prev else None}, next: {curr.next.val if curr.next else None}")
        curr = curr.next
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
