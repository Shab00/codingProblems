from typing import List

def solve(athletes:List[int]) -> int:

    athletes.sort()
    results = []
    for i in range(1, len(athletes)):
        teama = athletes[:i]
        teamb = athletes[i:]
        results.append(min(teamb) - max(teama))
    return min(results)

inputs = [3,1,2,6,4]

results = solve(inputs)

print(results)
