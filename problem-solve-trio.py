from typing import List

def solve(problems: List[List[int]]) -> int:

    for i in problems:
        return i

inputs = [[[ 1, 0, 1  ], [1, 1, 1], [0, 0, 0]],
          [[0, 1, 1], [0, 0, 1], [1, 1, 1], [1, 1, 0]]]

for list in inputs:
    result = solve(list)
    print(result)
