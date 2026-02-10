from collections import deque

inputs = [([["X","X","X","X"],
            ["X","O","O","X"],
            ["X","X","O","X"],
            ["X","O","X","X"]],
           [["X","X","X","X"],
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","O","X","X"]]),
          ([["X"]],[["X"]])]

def solve(board: list[list[str]]) -> list[list[str]]:
    m, n = len(board), len(board[0])
    q = deque([])
    visted = set()
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for row in range(m):
        for col in range(n):
            if (row == 0 or col == 0 or row == m - 1 or col == n - 1) and board[row][col]=="O":
                q.append((row, col))
    while q:
        row, col = q.popleft()
        board[row][col] = "K"
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < m and 0 <= nc < n:
                if board[nr][nc] == "O" and (nr, nc) not in visted:
                    q.append((nr, nc))
                    visted.add((nr, nc))

    for row in range(m):
        for col in range(n):
            if board[row][col] == "K":
                board[row][col] = "O"
            elif board[row][col] == "O":
                board[row][col] = "X"
    return board

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (grid, expec) in enumerate(inputs, start=1):
    result = solve(grid)
    if result == expec:
        print(f"example: {idx} => {result} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} => {RED}FAIL{RESET}")
