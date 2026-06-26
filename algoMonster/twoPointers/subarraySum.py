from collections import defaultdict

inputs = [
    ([1, 2, 3, 7, 4, 1], 3, 14),
    ([10, 5, 2, 7, 1, 9], 1, 10)
]

def find(arr: list[int], k: int) -> int:
    if not arr or k <= 0:
        return 0
        
    window_sum = sum(arr[:k])
    max_num = window_sum
    
    for r in range(k, len(arr)):
        window_sum += arr[r] - arr[r - k]
        max_num = max(max_num, window_sum)
        
    return max_num

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (arr, k, expec) in enumerate(inputs, start=1):
    result = find(arr, k)
    if result == expec:
        print(f"example: {idx} => {result} == {expec} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} != {expec} => {RED}FAIL{RESET}")
