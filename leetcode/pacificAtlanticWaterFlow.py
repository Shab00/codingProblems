from collections import deque

inputs = [([[1,2,2,3,5],
            [3,2,3,4,4],
            [2,4,5,3,1],
            [6,7,1,4,5],
            [5,1,1,2,4]], 
           [[0,4],[1,3],
            [1,4],[2,2],
            [3,0],[3,1],[4,0]]),
          ([[1]],
           [[0,0]])]

def paciAtla(heights: list[list[int]]) -> list[list[int]]:
    m, n = len(heights), len (heights[0])
    result = []
    p_visted = set()
    a_visted = set()
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for row in range(m):
        for col in range(n):
            if (row == 0 or col == 0) and (row, col) not in p_visted:
                p_visted.add((row, col))
            if (row == m - 1 or col == n - 1) and (row, col) not in a_visted:
                a_visted.add((row, col))

    q1 = deque(p_visted)
    while q1:
        row, col = q1.popleft()
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < m and 0 <= nc < n:
                if heights[nr][nc] >= heights[row][col] and (nr, nc) not in p_visted:
                    q1.append((nr, nc))
                    p_visted.add((nr, nc))

    q2 = deque(a_visted)
    while q2:
        row, col = q2.popleft()
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < m and 0 <= nc < n:
                if heights[nr][nc] >= heights[row][col] and (nr, nc) not in a_visted:
                    q2.append((nr, nc))
                    a_visted.add((nr, nc))
    for row, col in a_visted:
        if (row, col) in p_visted:
            result.append([row, col])
    return result

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (grid, expec) in enumerate(inputs, start=1):
    result = paciAtla(grid)
    result_set = set(map(tuple, result)) if result else set()
    expec_set = set(map(tuple, expec))
    
    if result_set == expec_set:
        print(f"example: {idx} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {RED}FAIL{RESET}")
        missing = expec_set - result_set
        extra = result_set - expec_set
        if missing:
            print(f"missing: {missing}")
        if extra:
            print(f"  extra:   {extra}")
