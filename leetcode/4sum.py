def my_sum(nums:list[int], target: int) -> list[list[int]]:
    pass

inputs = [([1,0,-1,0,-2,2], 0, [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]),
          ([2,2,2,2,2], 8, [[2,2,2,2]])]

for i, t, e in inputs:
    result = my_sum(i, t)
    print(f"input: {i} || output: {result} || expected: {e}")
