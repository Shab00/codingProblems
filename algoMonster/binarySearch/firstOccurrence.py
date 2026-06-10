inputs = [([1, 3, 3, 3, 3, 6, 10, 10, 10, 100], 3, 1),
          ([2, 3, 5, 7, 11, 13, 17, 19], 6, -1),
          ([4], 4, 0),
          ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1, 0)]

def find(arr: list[int], target: int) -> int:
    first, last = 0, len(arr) - 1

    while first <= last:
        mid = (last + first) // 2
        if arr[mid] == target:
            while arr[mid] == target and mid > 0:
                if arr[mid - 1] != target:
                    return mid
                mid -= 1
            return mid
        elif arr[mid] < target:
            first = mid + 1
        else:
            last = mid - 1
    return -1

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (n, t, expec) in enumerate(inputs, start=1):
    result = find(n, t)
    if result == expec:
        print(f"example: {idx} => {result} == {expec} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} != {expec} => {RED}FAIL{RESET}")

