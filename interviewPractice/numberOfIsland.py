from collections import deque

GREEN, RED, RESET = "\033[92m", "\033[91m", "\033[0m"

def num_islands(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()

    def bfs(r, c):
        q = deque([(r, c)])
        visited.add((r, c))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == "1":
                    visited.add((nr, nc))
                    q.append((nr, nc))

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                count += 1
                bfs(r, c)

    return count
    
tests = [
    (
        [["1","1","1","1","0"],
         ["1","1","0","1","0"],
         ["1","1","0","0","0"],
         ["0","0","0","0","0"]],
        1
    ),
    (
        [["1","1","0","0","0"],
         ["1","1","0","0","0"],
         ["0","0","1","0","0"],
         ["0","0","0","1","1"]],
        3
    ),
    (
        [["1"]],
        1
    ),
    (
        [["0"]],
        0
    ),
    (
        [["1","0","1","0","1"]],
        3
    ),
    (
        [["1","1"],
         ["1","1"]],
        1
    ),
    (
        [["1","0"],
         ["0","1"]],
        2
    ),
]

for i, (grid, expected) in enumerate(tests, 1):
    import copy
    result = num_islands(copy.deepcopy(grid))
    if result == expected:
        print(f"Test {i}: {GREEN}PASS{RESET}")
    else:
        print(f"Test {i}: {RED}FAIL{RESET}  expected {expected}, got {result}")
