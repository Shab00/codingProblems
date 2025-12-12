from collections import Counter

tests = [
    ([1,2,3], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]),
    ([0,1], [[0,1],[1,0]]),
    ([1], [[1]])
]

def perm(nums: list) -> list[list[int]]:
    if len(nums) == 0:
            return [[]]

    perms = perm(nums[1:])
    res = []
    for p in perms:
        for i in range(len(p) + 1):
            p_copy = p.copy()
            p_copy.insert(i, nums[0])
            res.append(p_copy)
    return res 

GREEN = "\033[92m"
PURPLE = "\033[95m"
RED = "\033[91m"
RESET = "\033[0m"

def check_perm(nums, expected):
    result = perm(nums)

    if not isinstance(result, list):
        print(f"{PURPLE}ERROR{RESET}: perm must return a list of permutations, got {type(result).__name__}")
        return

    res_tuples = []
    for p in result:
        if not isinstance(p, (list, tuple)):
            print(f"{RED}FAIL{RESET} - each permutation must be a list/tuple; got {type(p).__name__}: {p}")
            return
        if len(p) != len(nums):
            print(f"{RED}FAIL{RESET} - permutation has wrong length for input {nums}: {p}")
            return
        if sorted(p) != sorted(nums):
            print(f"{RED}FAIL{RESET} - permutation has wrong elements for input {nums}: {p}")
            return
        res_tuples.append(tuple(p))

    exp_tuples = [tuple(p) for p in expected]

    if Counter(res_tuples) == Counter(exp_tuples):
        print(f"{GREEN}PASS{RESET} for {nums}")
    else:
        print(f"{RED}FAIL{RESET} for {nums}")
        print(" expected (any order):", sorted(exp_tuples))
        print(" got      (any order):", sorted(res_tuples))

for nums, expected in tests:
    check_perm(nums, expected)
