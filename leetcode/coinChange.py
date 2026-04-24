inputs = [([1,2,5], 11, 3), ([2], 3, -1), ([1], 0, 0)]

def change(coins: list[int], num: int) -> int:
    memo = {}
    def helper(amount):

        if amount == 0:
            return 0
        if amount < 0:
            return -1
        if amount in memo:
            return memo[amount]
        minCoin = float('inf')
        for c in coins:
            res = helper(amount - c)
            if res >= 0:
                minCoin = min(minCoin, res + 1)
        
        memo[amount] = -1 if minCoin == float('inf') else minCoin
        return memo[amount]
    return helper(num)

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (l, n, expec) in enumerate(inputs, start=1):
    result = change(l, n)
    if result == expec:
        print(f"example: {idx} => {result} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} => {RED}FAIL{RESET}")
