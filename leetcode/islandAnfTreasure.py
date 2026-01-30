from collections import deque
from copy import deepcopy

inputs = [
        ([[2147483647,-1,0,2147483647],
          [2147483647,2147483647,2147483647,-1],
          [2147483647,-1,2147483647,-1],
          [0,-1,2147483647,2147483647]],
         [[3,-1,0,1],
          [2,2,1,-1],
          [1,-1,2,-1],
          [0,-1,3,4]]),
        ([[0,-1],
          [2147483647,2147483647]],
         [[0,-1],
          [1,2]])]

def islandTres(grid: list[list[int]]) -> list[list[int]]:
    zeros = deque([])
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 0:
                zeros.append((row, col, 0))
    visted = set()
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    m, n = len(grid), len(grid[0])
    
    while zeros:
        row, col, distance = zeros.popleft()
        for dr, dc in directions:
           nr, nc = row + dr, col + dc 
           if 0 <= nr < m and 0 <= nc < n:
               if grid[nr][nc] == 2147483647 and (nr, nc) not in visted:
                   grid[nr][nc] = distance + 1
                   visted.add((nr, nc))
                   zeros.append((nr, nc, distance + 1))
    return grid


GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def compare_grids(actual, expected):
    if len(actual) != len(expected):
        return [("size_mismatch", len(actual), len(expected))]
    mismatches = []
    for r in range(len(expected)):
        if len(actual[r]) != len(expected[r]):
            mismatches.append(("row_length", r, len(actual[r]), len(expected[r])))
            continue
        for c in range(len(expected[r])):
            if actual[r][c] != expected[r][c]:
                mismatches.append((r, c, actual[r][c], expected[r][c]))
    return mismatches

for idx, (grid, expec) in enumerate(inputs, start=1):
    g_copy = deepcopy(grid)
    result = islandTres(g_copy)
    actual = g_copy if result is None else result

    if actual == expec:
        print(f"example: {idx} => {GREEN}PASS{RESET}")
    else:
        mismatches = compare_grids(actual, expec)
        print(f"example: {idx} => {RED}FAIL{RESET} — mismatches: {mismatches[:10]}")
