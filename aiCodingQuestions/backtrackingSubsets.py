def subsets(digits: int) -> list[list[int]]:
    if not digits:
        return []

    sol = []
    ret = []
    n = len(digits)

    def backtrack(i=0):
        if i == n:
            ret.append(sol[:])
            return

        backtrack(i+1)

        sol.append(digits[i])
        backtrack(i+1)
        sol.pop()
    backtrack()
    return ret

inputs = [[1,2,3], [4,5,6]]
for i in inputs:
    result = subsets(i)
    print(result)
