inputs = [([1, 3, 3, 5, 8, 8, 10], 2, 1), ([2, 3, 5, 7, 11, 13, 17, 19], 6, 3)]

def find(arr: list, target: int) -> int:
    first, last = 0, len(arr) - 1
    temp = -1
    while first <= last:
        mid = (last + first ) // 2
        if arr[mid] >= target:
            temp = mid
            last = mid - 1
        else:
            first = mid + 1
    return temp


GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (n, t, expec) in enumerate(inputs, start=1):
    result = find(n, t)
    if result == expec:
        print(f"example: {idx} => {result} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} => {RED}FAIL{RESET}")

