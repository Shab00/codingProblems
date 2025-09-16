def search(nums: list[int], target: int) -> int:

    l = 0
    r = len(nums) - 1
    while l <= r: 
        m = (l + r) // 2
        if nums[m] == target:
            return m
        elif nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
    return -1

inputs = [([-1,0,3,5,9,12], 9, 4),
          ([-1,0,3,5,9,12], 2, -1)]

for i, t, e in inputs:
    result = search(i, t)
    print(
            f"inputs:\n{i}\n"
            f"outputs:\n{result}\n"
            f"expected:\n{e}\n"
            f"{'-'*50}"
            )
