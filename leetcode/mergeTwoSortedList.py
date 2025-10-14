class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeList(lst1: ListNode, lst2: ListNode) -> ListNode:
    if lst1 == None and lst2 == None:
        return None
    dummy = ListNode()
    curr = dummy
    head1, head2 = lst1, lst2
    while head1 and head2:
        if head1.val > head2.val:
            curr.next = head2
            head2 = head2.next
        else:
            curr.next = head1
            head1 = head1.next
        curr = curr.next

    if head1:
        curr.next = head1
    if head2:
        curr.next = head2

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
    ([1,2,4], [1,3,4]),
    ([], []),
    ([], [0])
]

for fcase, scase in test_cases:
    lst1 = list_to_linkedlist(fcase)
    lst2 = list_to_linkedlist(scase)
    merged = mergeList(lst1, lst2)  
    output = linkedlist_to_list(merged)
    print(f"Input: {fcase, scase} -> Output: {output}")
