def maxArea(height: list[int]) -> int:
    pass

inputs = [([1,8,6,2,5,4,8,3,7], 49), ([1,1], 1)]

for l, e in inputs:
    results = maxArea(l)
    print(f"input: {l} || output: {results} || expected: {e}")
