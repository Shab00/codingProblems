inputs = [
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
         "ABCCED", True),
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
         "SEE", True),
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
         "ABCB", False)
        ]

def search(grid: list[list[str]], word: str) -> bool:
    if not grid or not grid[0]:
        return False
    m, n = len(grid), len(grid[0])

    def dfs(r, c, i):
        if i == len(word):
            return True
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != word[i]:
            return False

        tmp = grid[r][c]
        grid[r][c] = None

        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            if dfs(r + dr, c + dc, i + 1):
                grid[r][c] = tmp 
                return True

        grid[r][c] = tmp
        return False

    for r in range(m):
        for c in range(n):
            if dfs(r, c, 0):
                return True
    return False

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (grid, word, expec) in enumerate(inputs, start=1):
    result = search(grid, word)
    if result == expec:
        print(f"example: {idx} => {word} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {word} => {RED}FAIL{RESET}")
