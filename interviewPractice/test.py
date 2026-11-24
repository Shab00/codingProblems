GREEN, RED, RESET = "\033[92m", "\033[91m", "\033[0m"

# ─── Problem 1: Valid Parentheses ─────────────────────────────────────────────
# Given a string containing just '(', ')', '{', '}', '[', ']'
# determine if the input string is valid.
# A string is valid if:
# - Open brackets are closed by the same type of bracket
# - Open brackets are closed in the correct order
#
# Input:  "()[]{}"  → True
# Input:  "([)]"    → False
# Input:  "{[]}"    → True

def is_valid(s):
    stack = []
    close_to_open = {")": "(", "]": "[", "}": "{"}

    for char in s:
        if char in close_to_open:
            if stack and stack[-1] == close_to_open[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)

    return not stack

paren_tests = [
    ("()",       True),
    ("()[]{}",   True),
    ("(]",       False),
    ("([)]",     False),
    ("{[]}",     True),
    ("",         True),
    ("{",        False),
    ("}}",       False),
    ("([{}])",   True),
]

print("=== Valid Parentheses ===")
for i, (s, expected) in enumerate(paren_tests, 1):
    result = is_valid(s)
    if result == expected:
        print(f"Test {i}: {GREEN}PASS{RESET}")
    else:
        print(f"Test {i}: {RED}FAIL{RESET}  expected {expected}, got {result}")


# ─── Problem 2: Maximum Subarray ─────────────────────────────────────────────
# Given an integer array, find the contiguous subarray
# with the largest sum and return that sum.
#
# Input:  [-2, 1, -3, 4, -1, 2, 1, -5, 4]  → 6  (subarray [4,-1,2,1])
# Input:  [1]                                → 1
# Input:  [-1]                               → -1

def max_subarray(nums):
    max_sum = nums[0]
    current_sum = 0

    for num in nums:
        if current_sum < 0:
            current_sum = 0
        
        current_sum += num
        max_sum = max(max_sum, current_sum)

    return max_sum

subarray_tests = [
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    ([1],                               1),
    ([-1],                             -1),
    ([-2, -1],                         -1),
    ([5, 4, -1, 7, 8],                 23),
    ([1, 2, 3, 4, 5],                  15),
    ([-1, -2, -3],                     -1),
]

print("\n=== Maximum Subarray ===")
for i, (nums, expected) in enumerate(subarray_tests, 1):
    result = max_subarray(nums)
    if result == expected:
        print(f"Test {i}: {GREEN}PASS{RESET}")
    else:
        print(f"Test {i}: {RED}FAIL{RESET}  expected {expected}, got {result}")
