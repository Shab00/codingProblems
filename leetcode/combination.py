inputs = [
        ([2,3,6,7], 7, [[2,2,3],[7]]),
        ([2,3,5], 8, [[2,2,2,2],[2,3,3],[3,5]]),
        ([2], 1, [])
        ]

def combSum(nums: list, target: int) -> list[list[int]]:

    res = []

    def dfs(i, cur, total):
        if total == target:
            res.append(cur.copy())
            return
        if i >= len(nums) or total > target:
            return

        cur.append(nums[i])
        dfs(i, cur, total + nums[i])
        cur.pop()
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
