import heapq

inputs = [
        ([3,2,1,5,6,4], 2, 5),
        ([3,2,3,1,2,4,5,5,6], 4, 4)
        ]

def kthLarge(nums: list[int], k: int) -> int:
    result = []
    max_heap = [-x for x in nums]
    heapq.heapify(max_heap)
    for _ in range(k):
        result.append(heapq.heappop(max_heap))

    return -result[k - 1]


GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (nums, k, expec) in enumerate(inputs, start=1):
    result = kthLarge(nums, k)
    if result == expec:
        print(f"example: {idx} => {result} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} => {RED}FAIL{RESET}")
