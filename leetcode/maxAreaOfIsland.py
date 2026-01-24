from collections import deque

def maxIsle(grid: list[list[str]]) -> int:

    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])
    visted = set()
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    result = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and (i, j) not in visted:
                area = 0
                q = deque()
                q.append((i, j))
                visted.add((i, j))

                while q:
                    r, c = q.popleft()
                    area += 1
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < m and 0 <= nc < n:
                            if grid[nr][nc] == 1 and (nr, nc) not in visted:
                                visted.add((nr, nc))
                                q.append((nr, nc))
                result = max(result, area)
    return result 


inputs = [
        ([[0,0,1,0,0,0,0,1,0,0,0,0,0],
          [0,0,0,0,0,0,0,1,1,1,0,0,0],
          [0,1,1,0,1,0,0,0,0,0,0,0,0],
          [0,1,0,0,1,1,0,0,1,0,1,0,0],
          [0,1,0,0,1,1,0,0,1,1,1,0,0],
          [0,0,0,0,0,0,0,0,0,0,1,0,0],
          [0,0,0,0,0,0,0,1,1,1,0,0,0],
          [0,0,0,0,0,0,0,1,1,0,0,0,0]], 6),
        ([[0,0,0,0,0,0,0,0]], 0),
        ([[1,1,0,0,0],
          [1,1,0,0,0],
          [0,0,0,1,1],
          [0,0,0,1,1]], 4)]


GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (grid, expec) in enumerate(inputs, start=1):
    result = maxIsle(grid)
    if result == expec:
        print(f"example: {idx} => {result} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} => {RED}FAIL{RESET}")
