class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def reverseList(self, head: ListNode) -> ListNode:
    cur = head
    prev = None

    while cur:
        nextNode = cur.next
        cur.next = prev
        prev = cur
        cur = nextNode
    return prev

def reverseListRecursive(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    newHead = reverseListRecursive(head.next)
    head.next.next = head
    head.next = None
    return newHead
