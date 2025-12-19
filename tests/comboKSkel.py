# Problem:
# Given a list of distinct integers `nums` and an integer `k`, return all possible
# combinations (subsets) of `nums` of size exactly `k`. The order of combinations
# does not matter, but the order inside each combination should follow the order
# of elements in `nums` (i.e., maintain relative order).
#
# Example:
#   nums = [1,2,3], k = 2  -> [[1,2],[1,3],[2,3]]
#
# Hints (leave these comments in place while you implement):
# - Use backtracking with a start index to avoid reordering:
#     res = []      # final list of combinations
#     cur = []      # current partial combination
#     def dfs(start):
#         # if len(cur) == k: append a COPY of cur to res and return
#         # for j in range(start, len(nums)):
#             # choose: cur.append(nums[j])
#             # recurse: dfs(j+1)
#             # undo: cur.pop()
# - Call dfs(0) and return res.
# - Ensure you append a copy of cur (res.append(cur[:])) when you record a solution.
# - You can optionally prune when remaining elements are insufficient:
#     if len(cur) + (len(nums) - start) < k: return
#
def combinations_k(nums: list[int], k: int) -> list[list[int]]:
    """
    Return all combinations of size k chosen from nums.
    TODO: implement using backtracking as described in the comments above.
    """
    res = []
    cur = []
    def dfs(start):
        if len(cur) == k:
            res.append(cur[:])
            return
        for j in range(start, len(nums)):
            cur.append(nums[j])
            dfs(j+1)
            cur.pop()
    dfs(0)
    return res

# ======= Checker and tests (do NOT modify) =======
from collections import Counter

tests = [
    # format: (nums, k, expected)
    ([1,2,3], 2, [[1,2], [1,3], [2,3]]),
    ([0], 1, [[0]]),
    ([1,2,3,4], 0, [[]])   # choose 0 elements -> one empty combination
]

def valid_combination_for_input(combo, nums, k):
    # check shape, length and that elements come from nums and are unique in combo
    if not isinstance(combo, (list, tuple)):
        return False
    if len(combo) != k:
        return False
    if len(set(combo)) != len(combo):
        return False
    # check elements are in nums
    nums_set = set(nums)
    for x in combo:
        if x not in nums_set:
            return False
    # optional: could check order-preserving property, but not enforced here
    return True

def check_combinations_k(nums, k, expected):
    try:
        result = combinations_k(nums, k)
    except Exception as e:
        print(f"ERROR calling combinations_k({nums!r}, {k!r}): {e}")
        return False

    if not isinstance(result, list):
        print("ERROR: combinations_k must return a list")
        return False

    # basic validity checks
    for c in result:
        if not valid_combination_for_input(c, nums, k):
            print("FAIL - invalid combination returned:", c)
            return False

    # compare as multisets of tuples so outer order doesn't matter
    res_count = Counter(tuple(c) for c in result)
    exp_count = Counter(tuple(c) for c in expected)

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
            print(" MISSING combinations:", missing)
        if unexpected:
            print(" UNEXPECTED combinations:", unexpected)
        return False

# Run tests
if __name__ == "__main__":
    for nums, k, expected in tests:
        print("nums =", nums, "k =", k)
        check_combinations_k(nums, k, expected)
        print()
