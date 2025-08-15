def comboSum(can: list[int], target: int) -> list[list[int]]:

    if not can:
        return []

    sol = []
    ret = []
    n = len(can)

    def backtrack(i=0):
        if i == n:
            total = sum(sol[:])
            if total == target:

                ret.append(sol[:])
            return

        backtrack(i+1)

        sol.append(can[i])
        backtrack(i+1)
        sol.pop()
    backtrack()
    return ret




inputs = [([2], 4),([2,3,6,7],7), ([2,3,5], 8)]
for i in inputs:
    result = comboSum(*i)
    print(f"input and target: {i} || output: {result}")
