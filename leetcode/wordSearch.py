inputs = [
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
         "ABCCED", True),
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
         "SEE", True),
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
         "ABCB", False)
        ]

def search(grid: list[list[str]], word: str) -> bool:
    pass


GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (grid, word, expec) in enumerate(inputs, start=1):
    result = search(grid, word)
    if result == expec:
        print(f"example: {idx} => {word} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {word} => {RED}FAIL{RESET}")
