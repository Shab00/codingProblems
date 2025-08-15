def comboSum(can: list[int], target: int) -> list[list[int]]:
    pass

inputs = [([2], 4),([2,3,6,7],7), ([2,3,5], 8)]
for i in inputs:
    result = comboSum(*i)
    print(f"input and target: {i} || output: {result}")
