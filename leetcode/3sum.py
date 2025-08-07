def threeSum(nums: list[int]) -> list[list]:
    result = []
    nums.sort()
    print(nums)

    for num in range(len(nums)):
        l, r = num + 1, len(nums) - 1
        if num > 0 and nums[num] == nums[num -1]:
            continue
        while l < r:
            isZero = nums[num] + nums[l] + nums[r]
                
            if isZero < 0:
                l += 1
            elif isZero > 0:
                r -= 1
            else:
                result.append([nums[num], nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
    return result



inputs = [([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
          ([0,1,1], []),
          ([0,0,0], [[0,0,0]])]

for i, e in inputs:
    result = threeSum(i)
    print(f"input: {i} || output: {result} || expected: {e}")
