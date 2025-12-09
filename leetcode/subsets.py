inputs = [
        ([1,2,3], [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]),
        ([0], [[], [0]])
        ]

def subsets(nums: list[int]) -> list[list[int]]:
    pass


GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (nums, expec) in enumerate(inputs, start=1):
    result = subsets(nums)
    if result == expec:
        print(f"Test {idx}: {GREEN}PASS{RESET}\nresult={result}\nexpected={expec}")
    else:
        print(f"Test {idx}: {RED}FAIL{RESET}\nresult={result}\nexpected={expec}\n")
