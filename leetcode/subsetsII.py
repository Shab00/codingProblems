inputs = [
        ([1,2,2], [[],[1],[1,2],[1,2,2],[2],[2,2]]),
        ([0], [[],[0]])
        ]

def subsets(nums):
    nums.sort()                     # sort first
    res = []
    cur = []

    def dfs(start):
        # record the current subset (append a copy)
        # TODO: append cur copy to res

        # iterate choices from start to end
        j = start
        while j < len(nums):
            # TODO: choose nums[j] (append to cur)
            # TODO: recurse with dfs(j + 1)
            # TODO: undo your choice (pop from cur)

            # skip duplicates at this recursion level:
            # move j forward while next equals current
            # (or use for-loop and `if j > start and nums[j] == nums[j-1]: continue`)
            j += 1

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
