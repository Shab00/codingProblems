inputs = [
    ([1, 6, 3, 1, 2, 4, 5], 10, 4),
]

def find(nums: list[int], target: int) -> int:
    window_sum = 0
    length = 0
    left = 0
    for right in range(len(nums)):
        window_sum += nums[right]
        while window_sum > target:
            window_sum -= nums[left]
            left += 1
        length = max(length, right - left + 1)
    return length

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (arr, k, expec) in enumerate(inputs, start=1):
    result = find(arr, k)
    if result == expec:
        print(f"example: {idx} => {result} == {expec} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} != {expec} => {RED}FAIL{RESET}")
