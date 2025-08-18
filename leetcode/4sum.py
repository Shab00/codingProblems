def my_sum(nums:list[int], target: int) -> list[list[int]]:
    result = []
    nums.sort()
    for first in range(len(nums)):
        for second in range(first + 1, len(nums)):
            l, r = second + 1, len(nums) - 1

            while l < r:
                cur =  nums[first] + nums[second] + nums[l] + nums[r]
                if cur == target:
                    result.append([nums[first], nums[second], nums[l], nums[r]])
                if cur < target:
                    l += 1
                else:
                    r -= 1

    return result

inputs = [([1,0,-1,0,-2,2], 0, [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]),
          ([2,2,2,2,2], 8, [[2,2,2,2]])]

for i, t, e in inputs:
    result = my_sum(i, t)
    print(f"input: {i} || output: {result} || expected: {e}")
