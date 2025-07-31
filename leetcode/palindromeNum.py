def isPal(x: int) -> bool:
    pass

inputs = [(121, True), (-121, False), (10, False)]

for nums, b in inputs:
    result = isPal(nums)
    print(f"input: {nums} || output: {result} || expected: {b}")
