inputs = [([2,3,2], 3),
          ([1,2,3,1], 4),
          ([1,2,3], 3)]

def rob(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    def rob_linear(houses):
        memo = {}
        def rob_from(i):
            if i >= len(houses):
                return 0
            if i in memo:
                return memo[i]
            robThis = houses[i] + rob_from(i + 2)
            skip = rob_from(i + 1)
            memo[i] = max(robThis, skip)
            return memo[i]
        return rob_from(0)

    money1 = rob_linear(nums[:-1])
    money2 = rob_linear(nums[1:])

    return max(money1, money2)

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (n, expec) in enumerate(inputs, start=1):
    result = rob(n)
    if result == expec:
        print(f"example: {idx} => {result} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} => {RED}FAIL{RESET}")
