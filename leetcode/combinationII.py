inputs = [
        ([10,1,2,7,6,1,5], 8, [[1,1,6],[1,2,5],[1,7],[2,6]]),
        ([2,5,2,1,2], 5,[[1,2,2],[5]])
        ]

def combSum(nums: list, target: int) -> list[list[int]]:
    res = []
    nums.sort()

    def dfs(i, cur, total):
        if total == target:
            res.append(cur[:])
            return
        if total > target or i == len(nums):
            return

        cur.append(nums[i])
        dfs(i + 1, cur, total + nums[i])
        cur.pop()
        while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
        dfs(i + 1, cur, total)

    dfs(0, [], 0)
    return res


GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def normalize(list_of_lists):
    return sorted(tuple(sorted(lst)) for lst in (list_of_lists or []))

def equal_combinations(result, expected):
    return normalize(result) == normalize(expected)

for nums, target, expec in inputs:
    res = combSum(nums, target)
    if equal_combinations(res, expec):
        print(f"{GREEN}PASS{RESET}")
    else:
        print(f"{RED}FAIL{RESET}")
        print("expected:", normalize(expec))
        print("got     :", normalize(res))
