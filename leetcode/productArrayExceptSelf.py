def product(nums: list[int]) -> list[int]:
    pass

inputs = [
        ([1,2,3,4], [24,12,8,6]), 
        ([-1,1,0,-3,3], [0,0,9,0,0])
         ]

for i, e in inputs:
    result = product(i)
    print(
            f"intputs:\n{i}\n"
            f"outputs:\n{result}\n"
            f"expected:\n{e}\n"
            f"{'-'*50}\n"
            )

