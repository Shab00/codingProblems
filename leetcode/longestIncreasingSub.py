inputs = [([10,9,2,5,3,7,101,18], 4),
          ([0,1,0,3,2,3], 4),
          ([7,7,7,7,7,7,7], 1)]

def length(nums: list[int]) -> int:
    def dfs(i, j):
        if i == len(nums):
            return 0

        LIS = dfs(i + 1, j)

        if j == -1 or nums[j] < nums[i]:
            LIS = max(LIS, 1 + dfs(i + 1, i))

        return LIS

    return dfs(0, -1)

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (s, expec) in enumerate(inputs, start=1):
    result = length(s)
    if result == expec:
        print(f"example: {idx} => {expec} => {result} => {GREEN}PASS{RESET}")
    else:
        print(f"example {idx}: => {expec} => {result} => {RED}FAIL{RESET}")
