from collections import deque

inputs = [([[2,1,1],
            [1,1,0],
            [0,1,1]], 4),
          ([[2,1,1],
            [0,1,1],
            [1,0,1]], -1),
          ([[0,2]], 0)]

def ornages(grid: list[list[int]]) -> int:

    if not grid or not grid[0]:
        return 0

    q = deque()
    m = len(grid)
    n = len(grid[0])
    visted = set()
    fresh = 0
    time = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for row in range(m):
        for col in range(n):
            if grid[row][col] == 1 and (row, col) not in visted:
                fresh += 1
            elif grid[row][col] == 2 and (row, col) not in visted:
                q.append((row, col))
                visted.add((row, col))

    if fresh == 0:
        return 0

    while q:
        infect = 0
        for _ in range(len(q)):
            row, col = q.popleft()
            for dr, dc in directions:
                nr, nc = dr + row, dc + col
                if 0 <= nr < m and 0 <= nc < n:
                    if grid[nr][nc] == 1 and (nr, nc) not in visted:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        visted.add((nr, nc))
                        fresh -= 1 
                        infect += 1
        if infect > 0:
            time += 1
        if fresh == 0:
            return time
    return -1

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (grid, expec) in enumerate(inputs, start=1):
    result = ornages(grid)
    if result == expec:
        print(f"example: {idx} => {result} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} => {RED}FAIL{RESET}")
