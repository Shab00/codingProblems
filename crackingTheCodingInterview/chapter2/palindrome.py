class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def append_to_tail(self, data):
        end = Node(data)
        n = self
        while n.next is not None:
            n = n.next
        n.next = end


def build_list(values):
    if not values:
        return None
    head = Node(values[0])
    for v in values[1:]:
        head.append_to_tail(v)
    return head

def is_palindrome(head: Node) -> bool:

    if head is None:
        return True

    fast, slow = head, head
    stack = []

    while fast is not None and fast.next is not None:
        
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next

    if fast is not None:
        slow = slow.next

    while slow is not None and stack is not None:

        if slow.data != stack.pop():
            return False

        slow = slow.next

    return True

GREEN, RED, RESET = "\033[92m", "\033[91m", "\033[0m"

tests = [
    # (values, expected)

    # 1. Empty list
    ([], True),

    # 2. Single node
    ([1], True),

    # 3. Two the same
    ([1, 1], True),

    # 4. Two different
    ([1, 2], False),

    # 5. Odd length palindrome
    ([1, 2, 1], True),

    # 6. Even length palindrome
    ([1, 2, 2, 1], True),

    # 7. Not a palindrome
    ([1, 2, 3], False),

    # 8. Longer odd palindrome
    ([1, 2, 3, 2, 1], True),

    # 9. Ends match, middle doesn't
    ([1, 2, 3, 1], False),

    # 10. Strings
    (["r", "a", "c", "e", "c", "a", "r"], True),

    # 11. Starts the same, ends different
    ([1, 1, 2], False),

    # 12. All the same
    ([0, 0, 0, 0], True),

    # 13. Repeating pattern, not a palindrome
    ([1, 2, 1, 2], False),

    # 14. Negatives
    ([-1, 2, -1], True),

    # 15. Long even palindrome
    (list(range(10)) + list(range(9, -1, -1)), True),

    # 16. Long, wrong only near the end
    ([1, 2, 3, 4, 5, 4, 3, 2, 2], False),
]

for i, (values, expected) in enumerate(tests, 1):
    result = is_palindrome(build_list(values))
    if result == expected:
        print(f"Test {i}: {GREEN}PASS{RESET}")
    else:
        print(f"Test {i}: {RED}FAIL{RESET}  {values}: expected {expected}, got {result}")
