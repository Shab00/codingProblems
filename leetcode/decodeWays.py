inputs = [("12", 2), ("226", 3), ("06", 0)]

def numDecode(s: str) -> int:

    memo = {}

    def helper(i):
        if i == len(s):
            return 1
        if s[i] == '0':
            return 0
        if i in memo:
            return memo[i]

        count = helper(i + 1)
        if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
            count += helper(i + 2)

        memo[i] = count
        return count

    return helper(0)

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (n, expec) in enumerate(inputs, start=1):
    result = numDecode(n)
    if result == expec:
        print(f"example: {idx} => {result} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} => {RED}FAIL{RESET}")
