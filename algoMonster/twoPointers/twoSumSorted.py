inputs = [([2, 3, 4, 5, 8, 11, 18], 8, [1, 3])]

def find(arr: list[int], target: int) -> int:
    res = []
    l, r = 0, len(arr) - 1

    while l < r:
        s = arr[l] + arr[r]
        if s == target:
            items = [l, r]
            return items
        elif s > target:
            r -= 1
        elif s < target:
            l += 1
    return res
        
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (n, t, expec) in enumerate(inputs, start=1):
    result = find(n, t)
    if result == expec:
        print(f"example: {idx} => {result} == {expec} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} != {expec} => {RED}FAIL{RESET}")

