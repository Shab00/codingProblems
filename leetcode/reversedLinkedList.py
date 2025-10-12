class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: ListNode) -> ListNode:
    pass

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
    [1,2,3,4,5],
    [1,2],
    []
]

for case in test_cases:
    head = list_to_linkedlist(case)
    reversed_head = reverseList(head) 
    output = linkedlist_to_list(reversed_head)
    print(f"Input: {case} -> Output: {output}")
