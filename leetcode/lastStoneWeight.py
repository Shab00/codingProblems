import heapq

inputs = [
        ([2,7,4,1,8,1], 1),
        ([1], 1)
        ]

def stoneW(stones: list[int]) -> int:

    result = 0
    max_heap = [-x for x in stones]
    heapq.heapify(max_heap)
    while max_heap:
        
        cur = -heapq.heappop(max_heap)
        result -= cur

    return result

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (stone, expec) in enumerate(inputs, start=1):
    result = stoneW(stone)
    if result == expec:
        print(f"example: {idx} => {result} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} => {RED}FAIL{RESET}")
