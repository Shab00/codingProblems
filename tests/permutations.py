# Problem:
# Given a list of distinct integers `nums`, return all possible permutations.
# You may return the permutations in any order.
#
# - Make sure to append a COPY of the current permutation when recording.
# - Time complexity: O(n! * n) (n! permutations, copying costs O(n)).
# - Space complexity: O(n) recursion depth + output size.
#
# TODO: implement one of the above approaches and return res.
def permutations(nums: list[int]) -> list[list[int]]:
    nums = list(nums)
    res = []
    def dfs(start: int):
        # when start reaches len(nums), record a copy of the current order
        if start == len(nums):
            # TODO: append a COPY of nums to res (so later swaps don't mutate it)
            res.append(nums[:])
            return
        # try placing each candidate at index `start`
        for i in range(start, len(nums)):
            # TODO: swap the element at `start` with element at `i`
            # (this puts candidate i into position start)
            # e.g., perform a swap operation here
            # recurse to fix the next position
            nums[start], nums[i] = nums[i], nums[start]
            dfs(start + 1)

            # TODO: swap back to restore original order (undo the choice)
            nums[start], nums[i] = nums[i], nums[start]
            # (this is essential: backtracking / undo)

    dfs(0)
    return res

# ======= Checker and tests (do NOT modify) =======
from collections import Counter

tests = [
    ([1,2,3], [
        [1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]
    ]),
    ([0], [[0]]),
    ([], [[]])  # permutations of empty list is a list containing the empty list
]

def valid_permutation_for_input(perm, nums):
    # check shape, length and that elements come from nums and are unique in perm
    if not isinstance(perm, (list, tuple)):
        return False
    if len(perm) != len(nums):
        return False
    if len(set(perm)) != len(perm):
        return False
    nums_set = set(nums)
    for x in perm:
        if x not in nums_set:
            return False
    return True

def check_permutations(nums, expected):
    try:
        result = permutations(nums)
    except Exception as e:
        print(f"ERROR calling permutations({nums!r}): {e}")
        return False

    if not isinstance(result, list):
        print("ERROR: permutations must return a list")
        return False

    # basic validity checks
    for p in result:
        if not valid_permutation_for_input(p, nums):
            print("FAIL - invalid permutation returned:", p)
            return False

    # compare as multisets of tuples so outer order doesn't matter
    res_count = Counter(tuple(p) for p in result)
    exp_count = Counter(tuple(p) for p in expected)

    if res_count == exp_count:
        print("PASS")
        return True
    else:
        print("FAIL")
        print(" expected (any order):", sorted([tuple(s) for s in expected]))
        print(" got      (any order):", sorted([tuple(s) for s in result]))
        missing = list((exp_count - res_count).elements())
        unexpected = list((res_count - exp_count).elements())
        if missing:
            print(" MISSING permutations:", missing)
        if unexpected:
            print(" UNEXPECTED permutations:", unexpected)
        return False

# Run tests
if __name__ == "__main__":
    for nums, expected in tests:
        print("nums =", nums)
        check_permutations(nums, expected)
        print()
