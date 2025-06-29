def sumList(nums: list) -> int:
    if not nums:
        return 0
    
    return nums[0] +  sumList(nums[1:])


result = sumList([1, 2, 3, 4])
print(result)
