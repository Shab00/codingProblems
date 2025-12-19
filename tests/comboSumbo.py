# Problem:
# Given a list of distinct positive integers `candidates` and a target integer `target`,
# return all unique combinations of `candidates` where the chosen numbers sum to `target`.
# You may use the same candidate number unlimited times.
#
# Example:
#   candidates = [2,3,6,7], target = 7 -> [[7], [2,2,3]]
#
# Hints (leave these comments in place while you implement):
# - Sort candidates (optional but helps pruning and deterministic output).
# - Use backtracking with a start index to avoid duplicate combinations in different orders.
#     res = []
#     cur = []
#     def dfs(start, remaining):
#         # if remaining == 0: append a COPY of cur to res and return
#         # if remaining < 0: return (prune)
#         # for j in range(start, len(candidates)):
#             # choose: cur.append(candidates[j])
#             # recurse: dfs(j, remaining - candidates[j])   # allow reuse -> pass j, not j+1
#             # undo: cur.pop()
# - Call dfs(0, target) and return res.
# - Append a COPY of cur when recording (res.append(cur[:])).
# - Optional pruning: if candidates[j] > remaining: break (since sorted).
#
def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    res = []
    cur = []
    def dfs(start, remaining):
        if remaining == 0:
            res.append(cur[:])
            return
        if remaining < 0:
            return
        for j in range(start, len(candidates)):
            cur.append(candidates[j])
            dfs(j, remaining - candidates[j])
            cur.pop()
    dfs(0, target)
    return res

# ======= Checker and tests (do NOT modify) =======
from collections import Counter

tests = [
    # (candidates, target, expected)
    ([2,3,6,7], 7, [[7], [2,2,3]]),
    ([2,3,5], 8, [[2,2,2,2], [2,3,3], [3,5]]),
    ([2], 1, [])  # no solution
]

def valid_comb_for_input(combo, candidates, target):
    # check shape
    if not isinstance(combo, (list, tuple)):
        return False
    # elements must come from candidates (reuse allowed)
    cand_set = set(candidates)
    for x in combo:
        if x not in cand_set:
            return False
    # combination must sum to target
    if sum(combo) != target:
        return False
    return True

def check_combination_sum(candidates, target, expected):
    try:
        result = combination_sum(candidates, target)
    except Exception as e:
        print(f"ERROR calling combination_sum({candidates!r}, {target!r}): {e}")
        return False

    if not isinstance(result, list):
        print("ERROR: combination_sum must return a list")
        return False

    # basic validity checks
    for comb in result:
        if not valid_comb_for_input(comb, candidates, target):
            print("FAIL - invalid combination returned:", comb)
            return False

    # Compare as multisets of sorted tuples so inner order and outer order don't matter
    res_count = Counter(tuple(sorted(c)) for c in result)
    exp_count = Counter(tuple(sorted(c)) for c in expected)

    if res_count == exp_count:
        print("PASS")
        return True
    else:
        print("FAIL")
        print(" expected (any order/inner order):", sorted([tuple(sorted(s)) for s in expected]))
        print(" got      (any order/inner order):", sorted([tuple(sorted(s)) for s in result]))
        missing = list((exp_count - res_count).elements())
        unexpected = list((res_count - exp_count).elements())
        if missing:
            print(" MISSING combinations (as sorted tuples):", missing)
        if unexpected:
            print(" UNEXPECTED combinations (as sorted tuples):", unexpected)
        return False

# Run tests
if __name__ == "__main__":
    for candidates, target, expected in tests:
        print("candidates =", candidates, "target =", target)
        check_combination_sum(candidates, target, expected)
        print()
