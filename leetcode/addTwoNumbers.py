class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:

    stack = []
    stack.append(l1)
    result = []
    while stack:
        node = stack.pop()
        result.append(node)
        if node.next:
            stack.append(node.val)

    return result

result = addTwoNumbers(l1, l2)
print(result)
