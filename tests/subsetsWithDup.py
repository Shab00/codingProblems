from collections import Counter

def subsets_with_dup(nums: list[int]) -> list[list[int]]:
    """
   - Sort nums first so duplicates become adjacent. This makes it easy to skip
      duplicate choices at the same recursion level.
    - Use backtracking with:
        res = []          # final list of subsets (list of lists)
        cur = []          # current partial subset (list)
        def dfs(start):
            # record a copy of the current subset (append cur[:])
            # loop j from start to len(nums)-1:
                # skip duplicates at this recursion level:
                #    if j > start and nums[j] == nums[j-1]: continue
                # choose nums[j] by cur.append(nums[j])
                # recurse dfs(j+1)
                # undo the choice by cur.pop()
    - Call dfs(0) and return res.
    - Make sure to append a COPY of cur when recording subsets (res.append(cur[:])).
    - Example behavior:
        nums = [1,2,2] -> subsets: [[], [1], [2], [1,2], [1,2,2], [2,2]]
    """

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

tests = [
    ([1,2,2], [[], [1], [2], [1,2], [1,2,2], [2,2]]),
    ([0],       [[], [0]]),
    ([],        [[]])
]

def valid_subset_for_input(subset, nums):
    # each element in subset must appear no more times than in nums
    cnt_sub = Counter(subset)
    cnt_nums = Counter(nums)
    for k, v in cnt_sub.items():
        if v > cnt_nums.get(k, 0):
            return False
    # preserve relative order assumption is not strictly enforced here,
    # but we ensure elements are from nums only and counts are respected.
    return True

def check_subsets_with_dup(nums, expected):
    try:
        result = subsets_with_dup(nums)
    except Exception as e:
        print(f"ERROR calling subsets_with_dup({nums!r}): {e}")
        return False

    if not isinstance(result, list):
        print("ERROR: subsets_with_dup must return a list")
        return False

    # basic validity checks
    for s in result:
        if not isinstance(s, (list, tuple)):
            print("FAIL - each subset must be a list/tuple:", s)
            return False
        if not valid_subset_for_input(s, nums):
            print("FAIL - invalid subset (uses elements too many times or unknown elements):", s)
            return False

    # compare as multisets of tuples so outer order doesn't matter
    res_count = Counter(tuple(s) for s in result)
    exp_count = Counter(tuple(s) for s in expected)

    if res_count == exp_count:
        print("PASS")
        return True
    else:
        print("FAIL")
        print(" expected (any order):", sorted([tuple(s) for s in expected]))
        print(" got      (any order):", sorted([tuple(s) for s in result]))
        # show differences
        missing = list((exp_count - res_count).elements())
        unexpected = list((res_count - exp_count).elements())
        if missing:
            print(" MISSING partitions:", missing)
        if unexpected:
            print(" UNEXPECTED partitions:", unexpected)
        return False

# Run tests
if __name__ == "__main__":
    for nums, expected in tests:
        print("nums =", nums)
        check_subsets_with_dup(nums, expected)
        print()
