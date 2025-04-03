from typing import List

def solve(problems: List[List[int]]) -> int:

    probSum = 0
    result = []

    for sublist in problems:
        result += sublist
        for i in sublist:
            probSum += i
    print(result)
    return probSum

inputs = [[[ 1, 0, 1], [1, 1, 1], [0, 0, 0]],
          [[0, 1, 1], [0, 0, 1], [1, 1, 1], [1, 1, 0]]]

for list in inputs:
    result = solve(list)
    print(result)
