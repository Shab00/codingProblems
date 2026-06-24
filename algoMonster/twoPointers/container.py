inputs = [([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
          ([3, 2, 1, 3], 9)]

def find(arr: list[int]) -> int:
    l, r = 0, len(arr) - 1
    result = 0
    while l < r:
        if arr[l] > arr[r]:
            s = (r - l) * min(arr[r], arr[l])
            result = max(result, s)
            r -= 1
        elif arr[r] > arr[l]:
            s = (r - l) * min(arr[r], arr[l])
            result = max(result, s)
            l += 1
        else:
            s = (r - l) * min(arr[r], arr[l])
            result = max(result, s)
            r -= 1
            l += 1
    return result
        
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (n, expec) in enumerate(inputs, start=1):
    result = find(n)
    if result == expec:
        print(f"example: {idx} => {result} == {expec} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} != {expec} => {RED}FAIL{RESET}")

