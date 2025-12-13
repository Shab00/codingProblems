inputs = [
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
         "ABCCED", True),
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
         "SEE", True),
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
         "ABCB", False)
        ]

def search(grid: list[list[str]], word: str) -> bool:
    key = {}
    count = 0
    for char in word:
        if char not in key:
            key[char] = 0
        key[char] += 1
        count += 1
    print(count)
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if count == 0:
                return True
            elif grid[row][col] in key:
                count -= 1
    print(count)
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
