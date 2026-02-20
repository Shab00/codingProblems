class ListNode:
    def __init__(val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            next_temp = curr.next     
            curr.next = prev          
            prev = curr              
            curr = next_temp 
        return prev

def reverseListRecursive(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    new_head = reverseListRecursive(head.next)
    head.next.next = head
    head.next = None
    return new_head
