def longest(nums: list[int]) -> int:
    nums = list(set(nums))
    print(nums)



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
