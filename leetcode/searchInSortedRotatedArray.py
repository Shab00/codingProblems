def search(nums: list[int], target: int) -> int:

    l, r = 0, len(nums) - 1

    while l <= r:
        m = (l + r) // 2
        print(nums[l], nums[m], nums[r])
        if nums[m] == target:
            return m
        if nums[l] < nums[m]:
            r = m - 1
        else:
            l = m + 1
    return -1


inputs = [([4,5,6,7,0,1,2], 0, 4),
          ([4,5,6,7,0,1,2], 3, -1),
          ([1], 0, -1),
          ([4,5,6,7,8,1,2,3], 8, 4)]

for i, o, e in inputs:
    result = search(i, o)
    print(
            f"inputs:\n{i, o}\n"
            f"outputs:\n{result}\n"
            f"expected:\n{e}\n"
            f"{'-'*50}"
            )
