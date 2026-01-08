import heapq
from collections import Counter

inputs = [
        ([[1,3],[-2,2]], 1, [[-2,2]]),
        ([[3,3],[5,-1],[-2,4]], 2, [[3,3],[-2,4]])
        ]

def kClosest(points: list[list[int]], k: int) -> list[list[int]]:
    heap = []
    result = []
    for point in points:
        priority = point[0]*point[0] + point[1]*point[1]
        heapq.heappush(heap, (priority, point))
    for _ in range(min(k, len(heap))):
        result.append(heapq.heappop(heap)[1])
    return result   

GREEN = "\033[92m"
PURPLE = "\033[95m"
RED = "\033[91m"
RESET = "\033[0m"

def same_multiset(a: list[list[int]], b: list[list[int]]) -> bool:
    return Counter(tuple(p) for p in a) == Counter(tuple(p) for p in b)

for idx, (points, k, expec) in enumerate(inputs, start=1):
    result = kClosest(points, k)
    if result is None:
        print(f"example: {idx} => {result} => {PURPLE}ERROR: kClosest returned None{RESET}")
        continue
    if same_multiset(result, expec):
        print(f"example: {idx} => {result} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} => {RED}FAIL{RESET}")
