GREEN, RED, RESET = "\033[92m", "\033[91m", "\033[0m"

def two_sum(nums, target):

    seen = {}

    for i, num in enumerate(nums):

        complement = target - num 

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

tests = [
    ([2, 7, 11, 15], 9,  [0, 1]),
    ([3, 2, 4],      6,  [1, 2]),
    ([3, 3],         6,  [0, 1]),
    ([1, 2, 3, 4],   7,  [2, 3]),
    ([0, 4, 3, 0],   0,  [0, 3]),
    ([-1, -2, -3],  -5,  [1, 2]),
    ([1, 5, 3, 2],   4,  [0, 2]),
]

for i, (nums, target, expected) in enumerate(tests, 1):
    result = two_sum(nums, target)
    if sorted(result) == sorted(expected):
        print(f"Test {i}: {GREEN}PASS{RESET}")
    else:
        print(f"Test {i}: {RED}FAIL{RESET}  expected {expected}, got {result}")
