inputs = [([7,2,5,10,8], 2, 18),
          ([2,3,5,7], 3, 7)]

def find(arr: list[int], target: int) -> int:
    l = max(arr)
    r = sum(arr)
    ans = r
    while l <= r:
        mid = (l + r) // 2

        if fun(arr, target, mid):
            ans = mid
            r = mid - 1
        else:
            l = mid + 1

    return ans
        
def fun(arr, k, limit):
    workers = 1
    current_sum = 0

    for time in arr:
        if current_sum + time <= limit:
            current_sum += time
        else:
            workers += 1
            current_sum = time

    return workers <= k

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (n, t, expec) in enumerate(inputs, start=1):
    result = find(n, t)
    if result == expec:
        print(f"example: {idx} => {result} == {expec} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} != {expec} => {RED}FAIL{RESET}")

