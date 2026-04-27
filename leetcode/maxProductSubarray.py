inputs = [([2,3,-2,4], 6), ([-2,0,-1], 0), ([-2,3,-4], 24)]

def maxProd(nums: list[int]) -> int:
    res = nums[0]
    curMin, curMax = 1, 1

    for num in nums:
        tmp = curMax * num
        curMax = max(num * curMax, num * curMin, num)
        curMin = min(tmp, num * curMin, num)
        res = max(res, curMax)
    return res

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (n, expec) in enumerate(inputs, start=1):
    result = maxProd(n)
    if result == expec:
        print(f"example: {idx} => {result} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} => {RED}FAIL{RESET}")
