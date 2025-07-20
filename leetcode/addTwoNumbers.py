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

    current1, current2 = l1, l2
    temp1, temp2 = [], []
    while current1 and current2:
        temp1.append(str(current1.val))
        temp2.append(str(current2.val))
        current1 = current1.next
        current2 = current2.next
    temp1.reverse()
    temp2.reverse()
    num1 = ''.join(temp1)
    num2 = ''.join(temp2)
    total = int(num1) + int(num2)
    strTotal = str(total)
    l3 = list(strTotal)
    l3.reverse()
    return l3

result = addTwoNumbers(l1, l2)
print(result)
