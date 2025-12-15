from collections import Counter

def subsets(nums: list[int]) -> list[list[int]]:
    nums.sort()          # keeps output deterministic (optional for distinct input)
    res = []
    cur = []

    def dfs(start):
        # record current subset (append a copy)
        # TODO: append cur copy to res

        res.append(cur[:])
        # try choices
        for j in range(start, len(nums)):
            # choose
            # TODO: append nums[j] to cur
            cur.append(nums[j])
            dfs(j + 1)
            # undo (backtrack)
            cur.pop()

    dfs(0)
    return res


tests = [
    ([1,2], [[], [1], [2], [1,2]]),
    ([0],   [[], [0]]),
    ([],    [[]])
]

def check_subsets(nums, expected):
    try:
        result = subsets(nums)
    except Exception as e:
        print(f"ERROR calling subsets({nums}): {e}")
        return False

    if not isinstance(result, list):
        print("ERROR: subsets must return a list")
        return False

    # quick validity: each subset should have elements from nums only
    sorted_nums = sorted(nums)
    for s in result:
        if not isinstance(s, (list, tuple)) or sorted(s) != sorted(s) or any(x not in nums for x in s):
            print("FAIL - invalid subset returned:", s)
            return False

    # compare as multisets of sorted tuples so outer order doesn't matter
    res_count = Counter(tuple(sorted(s)) for s in result)
    exp_count = Counter(tuple(sorted(s)) for s in expected)

    if res_count == exp_count:
        print("PASS")
        return True
    else:
        print("FAIL")
        print(" expected:", sorted([tuple(sorted(s)) for s in expected]))
        print(" got     :", sorted([tuple(sorted(s)) for s in result]))
        return False

# Run tests
for nums, expected in tests:
    print("nums =", nums)
    check_subsets(nums, expected)
    print()
