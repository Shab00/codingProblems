def product(nums: list[int]) -> list[int]:

    p = 0
    arr = len(nums) - 1
    result = []
    while p <= arr:
        cur = []
        for i, num in enumerate(nums):
            if i == p:
                continue
            else:
                cur.append(num)
        sums = 1
        for num in cur:
            sums *= num
        result.append(sums)
        p += 1
    return result




inputs = [
        ([1,2,3,4], [24,12,8,6]), 
        ([-1,1,0,-3,3], [0,0,9,0,0]),
        ([0,0], [0,0])
         ]

for i, e in inputs:
    result = product(i)
    print(
            f"intputs:\n{i}\n"
            f"outputs:\n{result}\n"
            f"expected:\n{e}\n"
            f"{'-'*50}\n"
            )

