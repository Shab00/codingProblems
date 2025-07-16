from typing import List

def solve(problems: List[List[int]]) -> int:

        count = 0
        result = []

        for sublist in problems:
            if sum(sublist) > 1:
                count += 1
        return count

inputs = [[[1,1,0],[1,1,1],[1,0,0]],
          [[1,0,0],[0,1,1]],
          [[1,0,0]],
          [[1,0,0],[0,1,0],[1,1,1],[0,0,1],[0,0,0]],
          [[0,1,0],[0,1,0],[1,1,0],[1,1,0],[1,0,0],[0,0,1],[0,1,1],
           [1,1,1],[1,1,0],[0,0,0],[0,0,0]]
         ]

for list in inputs:
    result = solve(list)
    print(result)
