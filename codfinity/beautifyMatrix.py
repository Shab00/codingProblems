from collections import deque
from typing import List

def solve(matrix: List[List[int]]) -> int:
    start = None
    end = (2, 2)
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 1:
                start = (row, col)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    path = deque([(start, [start])])
    visted = set()
    visted.add(start)
    while path:
        (curRow, curCol), pathSoFar = path.popleft()
        if (curRow, curCol) == end:
            return len(pathSoFar) - 1
        for dr, dc in directions:
            nr, nc = curRow + dr, curCol + dc
            if (0 <= nr < len(matrix) and
                0 <= nc < len(matrix[0]) and
                (nr, nc) not in visted):
                path.append(((nr, nc), pathSoFar + 
                             [(nr, nc)]))
                visted.add((nr, nc))
    return None

def manhattan(matrix: List[List[int]]) -> int:
    start = None
    end = (2, 2)
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 1:
                start = (row, col)

    return abs((end[0] - start[0])) + abs((end[1] - start[1]))

matrix = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1], 
        [0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0]
        ]

result = solve(matrix)
man = manhattan(matrix)
print(man)
print(result)
