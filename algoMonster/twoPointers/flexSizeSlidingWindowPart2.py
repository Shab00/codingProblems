from collections import defaultdict

inputs = [
    ([1, 4, 1, 7, 3, 0, 2, 5], 10, 2),
    ([1, 1, 1], 3, 3)
]

def find(nums: list[int], target: int) -> int:
    min_len = float('inf')
    window_sum = 0
    l = 0

    for r in range(len(nums)):
        window_sum += nums[r]

        while window_sum >= target:
            min_len = min(min_len, r - l + 1)
            
            window_sum -= nums[l]
            l += 1

    return min_len

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (arr, k, expec) in enumerate(inputs, start=1):
    result = find(arr, k)
    if result == expec:
        print(f"example: {idx} => {result} == {expec} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} != {expec} => {RED}FAIL{RESET}")
