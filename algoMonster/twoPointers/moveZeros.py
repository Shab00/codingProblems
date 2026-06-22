inputs = [([1, 0, 2, 0, 0, 7], [1, 2, 7, 0, 0, 0]),]

def move(arr: list[int]) -> None:
    l, r = 0, 0
    while r < len(arr):
        temp = None 
        if arr[r] != 0:
            temp = arr[l]
            arr[l] = arr[r]
            arr[r] = temp
            l += 1

        r += 1

    return arr

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (n, expec) in enumerate(inputs, start=1):
    result = move(n)
    if result == expec:
        print(f"example: {idx} => {result} == {expec} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} != {expec} => {RED}FAIL{RESET}")

