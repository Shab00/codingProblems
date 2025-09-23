def findMin(nums: list[int]) -> int:

    l = 0
    r = len(nums) - 1
    while l < r:
        m = (l + r) // 2
        if nums[m] >= nums[r]:
            l = m + 1
        else:
            r = m

    return nums[l]

inputs = [([3,4,5,1,2], 1),
          ([4,5,6,7,0,1,2], 0),
          ([11,13,15,17], 11)]

for i, e in inputs:
    result = findMin(i)
    print(
            f"inputs:\n{i}\n"
            f"outputs:\n{result}\n"
            f"expected:\n{e}\n"
            f"{'-'*50}"
            )
