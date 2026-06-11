inputs = [([0, 1, 2, 3, 2, 1, 0], 3),
          ([0, 10, 3, 2, 1, 0], 1)]

def find(arr: list[int]) -> int:
    alen = len(arr)
    left = 0
    right = alen - 1
    boundary_index = -1

    while left <= right:
        mid = (left + right) // 2
        if mid == alen - 1 or arr[mid] > arr[mid + 1]:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary_index

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (n, expec) in enumerate(inputs, start=1):
    result = find(n)
    if result == expec:
        print(f"example: {idx} => {result} == {expec} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} != {expec} => {RED}FAIL{RESET}")
