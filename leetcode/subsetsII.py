inputs = [
        ([1,2,2], [[],[1],[1,2],[1,2,2],[2],[2,2]]),
        ([0], [[],[0]])
        ]

def subsets(nums):

    nums.sort()
    res = []
    cur = []

    def dfs(start):
        res.append(cur[:])

        for j in range(start, len(nums)):
            if j > start and nums[j] == nums[j-1]:
                continue
            cur.append(nums[j])
            dfs(j + 1)
            cur.pop()

    dfs(0)
    return res

def sort_key_tuple(t):
    return (len(t), t)

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (nums, expec) in enumerate(inputs, start=1):
    result = subsets(nums)
    res_set = set(tuple(s) for s in result)
    ex_set = set(tuple(s) for s in expec)

    if res_set == ex_set:
        print(f"Test {idx}: {GREEN}PASS{RESET}\nresult (any order)={result}\nexpected (any order)={expec}\n")
    else:
        print(f"Test {idx}: {RED}FAIL{RESET}")
        print("  expected (sorted view):", sorted([tuple(s) for s in expec], key=sort_key_tuple))
        print("  got      (sorted view):", sorted([tuple(s) for s in result], key=sort_key_tuple))
        print()
