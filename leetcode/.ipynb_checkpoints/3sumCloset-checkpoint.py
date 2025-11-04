def threeSum(nums: list[int], target: int) -> int:
    nums.sort()
    result = float('inf')
    for index in range(len(nums)):
        l, r = index + 1, len(nums) - 1
        while l < r:
            tNum = nums[index] + nums[l] + nums[r]
            dif = abs(tNum - target)
            if tNum == target:
                return tNum
            elif abs(tNum - target) < abs(result - target):
                result = tNum

            if tNum < target:
                l += 1
            else:
                r -= 1
    return result

inputs = [([-1,2,1,-4], 1, 2), 
          ([0,0,0], 1, 0),
          ([1,1,1,0], 100, 3)]
for i, t, e in inputs:
    result = threeSum(i, t)
    print(f"inputs: {i, t} || outputs: {result} || expected: {e}")
