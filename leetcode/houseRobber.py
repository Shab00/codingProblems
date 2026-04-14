inputs = [([1,2,3,1], 4),
          ([2,7,9,3,1], 12)]

def rob(nums: list[int]) -> int:

    memo = {}
    def rob(i):
        if i >= len(nums):
            return 0
        if i in memo:
            return memo[i]
        robThis = nums[i] + rob(i + 2)
        skip = rob(i + 1)
        memo[i] = max(robThis, skip)
        return memo[i]

    return rob(0)

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (n, expec) in enumerate(inputs, start=1):
    result = rob(n)
    if result == expec:
        print(f"example: {idx} => {result} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} => {RED}FAIL{RESET}")
