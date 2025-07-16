from typing import List

def solve(weights:List[int])->str:
    total = sum(weights)
    ones = weights.count(1)
    twos = weights.count(2)
    if total % 2 != 0:
        return "NO"
    half = total // 2
    if half % 2 != 0 and ones == 0:
        return "NO"
    return "YES"
inputs = [[1, 1], [1, 2]]

for i in inputs:
    result = solve(i)
    print(result)
