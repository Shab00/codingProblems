inputs = [
    ([1, -20, -3, 30, 5, 4], 7, [1, 4]),
    ([3, 4, 7, 2, -3, 1, 4, 2], 7, [0, 2]),
]

def find(arr: list[int], target: int) -> list[int]:
    prefix_sums = {0: 0}
    cur_sum = 0
    for i in range(len(arr)):
        cur_sum += arr[i]
        complement = cur_sum - target
        if complement in prefix_sums:
            return [prefix_sums[complement], i + 1]
        prefix_sums[cur_sum] = i + 1
    return []

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (arr, target, expec) in enumerate(inputs, start=1):
    result = find(arr, target)

    if result == expec:
        print(f"example: {idx} => {result} == {expec} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} != {expec} => {RED}FAIL{RESET}")
