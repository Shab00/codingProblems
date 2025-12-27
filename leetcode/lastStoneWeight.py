import heapq

inputs = [
        ([2,7,4,1,8,1], 1),
        ([1], 1)
        ]

def stoneW(stones: list[int]) -> int:
    max_heap = [-x for x in stones]
    heapq.heapify(max_heap)
    print(max_heap)
    print("as positives (heap order):", [-x for x in max_heap])

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (stone, expec) in enumerate(inputs, start=1):
    result = stoneW(stone)
    if result == expec:
        print(f"example: {idx} => {result} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} => {RED}FAIL{RESET}")
