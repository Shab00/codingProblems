inputs = [
    ([1, -20, -3, 30, 5, 4], 7, [1, 4]),
    ([3, 4, 7, 2, -3, 1, 4, 2], 7, [0, 2]),
]

def find(arr: list[int], target: int) -> list[int]:
    l = 0

    for r in range(len(arr)):
        total += r
    

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (arr, target, expec) in enumerate(inputs, start=1):
    result = find(arr, target)

    if result == expec:
        print(f"example: {idx} => {result} == {expec} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} != {expec} => {RED}FAIL{RESET}")
