inputs = [([0, 0, 1, 1, 1, 2, 2], 3),
          ([1, 2, 3], 3),
          ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1)]

def remove(arr: list[int]) -> int:
    l, r = 0, 1
    while r < len(arr):
        if arr[l] != arr[r]:
            l += 1
            arr[l] = arr[r]
        r += 1

    return l + 1 

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (n, expec) in enumerate(inputs, start=1):
    result = remove(n)
    if result == expec:
        print(f"example: {idx} => {result} == {expec} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} != {expec} => {RED}FAIL{RESET}")

