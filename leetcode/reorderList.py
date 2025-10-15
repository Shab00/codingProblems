class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head: ListNode) -> None:
    """
    Reorders the list as described in the problem statement.
    Do not return anything, modify head in-place instead.
    """
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
    [1,2,3,4],
    [1,2,3,4,5]
]

for case in test_cases:
    head = list_to_linkedlist(case)
    reorderList(head)  # The function modifies the list in-place
    output = linkedlist_to_list(head)
    print(f"Input: {case} -> Output: {output}")
