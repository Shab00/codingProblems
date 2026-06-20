inputs = [([0, 0, 1, 1, 1, 2, 2], 3)]

def remove(arr: list[int]) -> int:
    l, r = 0, 0
    d = set(arr)
    while r < len(arr):
        print(arr[r])

        r += 1
        l += 1
    return len(d)


GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (n, expec) in enumerate(inputs, start=1):
    result = remove(n)
    if result == expec:
        print(f"example: {idx} => {result} == {expec} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} != {expec} => {RED}FAIL{RESET}")

