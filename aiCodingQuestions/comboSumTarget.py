def comboSum(can: list[int], target: int) -> list[list[int]]:

    if not can:
        return []

    sol = []
    ret = []
    n = len(can)

    def backtrack(i=0, curSum=0):
        if curSum == target:
            ret.append(sol[:])
            return

        elif curSum > target or i == n:
            return 

        sol.append(can[i])
        backtrack(i, curSum + can[i])
        sol.pop()
        backtrack(i+1, curSum)
    backtrack(0, 0)
    return ret




inputs = [([2], 4),([2,3,6,7],7), ([2,3,5], 8)]
for i in inputs:
    result = comboSum(*i)
    print(f"input and target: {i} || output: {result}")
