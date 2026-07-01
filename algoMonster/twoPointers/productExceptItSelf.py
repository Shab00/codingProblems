inputs = [
    ([1, 2, 3, 4], [24, 12, 8, 6]),
    ([2, 3, 4, 5], [60, 40, 30, 24]),
    ]

def find(nums: list[int]) -> list[int]:
    length = len(nums)
    result = [1] * length

    left = 1
    for i in range(length):
        result[i] = left
        left *= nums[i]

    right = 1
    for i in reversed(range(length)):
        result[i] *= right
        right *= nums[i]

    return result

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (arr, expec) in enumerate(inputs, start=1):
    result = find(arr)

    if result == expec:
        print(f"example: {idx} => {result} == {expec} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} != {expec} => {RED}FAIL{RESET}")
