def solve(ls: list) -> bool:
    duplicate = set(ls)

    if len(duplicate) == len(ls):
        return False
    
    return True

inputs = [[1, 2, 3, 1], [1, 2, 3, 4]]
for i in inputs:
    result = solve(i)
    print(result)
