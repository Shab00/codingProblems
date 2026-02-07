from collections import deque

inputs = [([[2,1,1],
            [1,1,0],
            [0,1,1]], 4),
          ([[2,1,1],
            [0,1,1],
            [1,0,1]], -1),
          ([[0,2]], 0)]

def ornages(grid: list[list[int]]) -> int:
    pass


GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (grid, expec) in enumerate(inputs, start=1):
    result = ornages(grid)
    if result == expec:
        print(f"example: {idx} => {result} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} => {RED}FAIL{RESET}")
