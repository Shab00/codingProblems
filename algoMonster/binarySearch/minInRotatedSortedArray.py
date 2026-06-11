inputs = [([30, 40, 50, 10, 20], 3),
          ([3, 5, 7, 11, 13, 17, 19, 2], 7),
          ([5, 1, 2, 3, 4], 1),
          ([100, 200, 300, 400, 500, 1, 10, 20, 30, 40, 50, 60, 70, 80, 90], 5),
          ([5, 1, 2, 3, 4], 1)]

def find(arr: list[int]) -> int:

    left, right = 0, len(arr) - 1
    boundary_index = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= arr[-1]:
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
