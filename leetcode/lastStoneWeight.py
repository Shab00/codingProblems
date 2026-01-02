import heapq

inputs = [
        ([2,7,4,1,8,1], 1),
        ([1], 1),
        ([2,2], 0)
        ]

def stoneW(stones: list[int]) -> int:
    max_heap = [-x for x in stones]
    heapq.heapify(max_heap)
    while len(max_heap) > 1:
        if len(max_heap) == 1:
            return -max_heap[0]

       
        first = -heapq.heappop(max_heap)
        second = -heapq.heappop(max_heap)
        if first == second:
            continue

        else:
            cur = first - second
            heapq.heappush(max_heap, -cur)
    if not max_heap:
        return 0
    else:
        return -max_heap[0]

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (stone, expec) in enumerate(inputs, start=1):
    result = stoneW(stone)
    if result == expec:
        print(f"example: {idx} => {result} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} => {RED}FAIL{RESET}")
