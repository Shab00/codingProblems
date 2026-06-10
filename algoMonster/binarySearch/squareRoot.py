inputs = [(16, 4), (8, 2)]

def find(num: int) -> int:
    l, r = 0, num

    ans = -1
    while l <= r:
        mid = (r + l) // 2
        if mid * mid <= num:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1

    return ans 

        

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (n, expec) in enumerate(inputs, start=1):
    result = find(n)
    if result == expec:
        print(f"example: {idx} => {result} == {expec} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} != {expec} => {RED}FAIL{RESET}")

