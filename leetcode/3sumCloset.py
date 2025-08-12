def threeSum(nums: list[int], target: int) -> int:
    nums.sort()
    result = 0
    for index in range(len(nums)):
        l, r = index + 1, len(nums) - 1
        while l < r:
            tNum = nums[index] + nums[l] + nums[r]
            if tNum < 0:
                tNum = tNum * -1
            dif = abs(tNum - target)
            print(tNum, dif)
            if tNum == target:
                return tNum
            else:
                result = min(result, tNum)

            if tNum < target:
                l += 1
            else:
                r -= 1
    return result

inputs = [([-1,2,1,-4], 1, 2), ([0,0,0], 1, 0)]
for i, t, e in inputs:
    result = threeSum(i, t)
    print(f"inputs: {i, t} || outputs: {result} || expected: {e}")
