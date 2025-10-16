class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head: ListNode) -> None:
    """
    Reorders the list as described in the problem statement.
    Do not return anything, modify head in-place instead.
    """

    if not head or not head.next or not head.next.next:
        return

    slow, fast = head, head
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next = None

    prev2 = None
    curr = slow
    while curr:
        next_temp = curr.next
        curr.next = prev2
        prev2 = curr
        curr = next_temp
    second = prev2

    first = head
    while first and second:
        tmp1 = first.next
        tmp2 = second.next
        first.next = second
        if tmp1 is None:
            break
        second.next = tmp1
        first = tmp1
        second = tmp2

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
    [1,2,3,4],
    [1,2,3,4,5]
]
