def longest(nums: list[int]) -> int:
    nums = set(nums)
    result = 0
    for i in nums:
        if i - 1 not in nums:
            curNum = i
            cur = 1
            while curNum + 1 in nums:
                curNum += 1
                cur += 1
            result = max(result, cur)

    return result


inputs = [
        ([100,4,200,1,3,2], 4), 
        ([0,3,7,2,5,8,4,6,0,1], 9),
        ([1,0,1,2], 3)
          ]

for i, e in inputs:
    result = longest(i)
    print(
            f"inputs:\n{i}\n"
            f"outputs:\n{result}\n"
            f"expected:\n{e}\n"
            f"{'-' * 50}"
            )
