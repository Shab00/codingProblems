inputs = [([7,2,5,10,8], 2, 18),
          ([2,3,5,7], 3, 7)]

def find(arr: list[int], target: int) -> int:
    l, r = 0, len(arr) - 1

    best = -1

    while l <= r:
        mid = (r + l) // 2

        leftside = sum(arr[:mid]) 
        rightside = sum(arr[mid:])
        if leftside > rightside:
            


GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (n, t, expec) in enumerate(inputs, start=1):
    result = find(n, t)
    if result == expec:
        print(f"example: {idx} => {result} == {expec} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} != {expec} => {RED}FAIL{RESET}")

