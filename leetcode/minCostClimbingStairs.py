inputs = [([10,15,20], 15),
          ([1,100,1,1,1,100,1,1,100,1], 6)]

def minCost(cost: list[int]) -> int:
    n = len(cost)
    dp = [0] * (n + 2)
    i = n - 1
    while i >= 0:
        dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
        i -= 1
    return min(dp[0], dp[1])

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (n, expec) in enumerate(inputs, start=1):
    result = minCost(n)
    if result == expec:
        print(f"example: {idx} => {result} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} => {RED}FAIL{RESET}")
