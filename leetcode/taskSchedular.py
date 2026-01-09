import heapq

inputs = [
        (["A","A","A","B","B","B"], 2, 8),
        (["A","C","A","B","D","B"], 1, 6),
        (["A","A","A","B","B","B"], 3, 10)
        ]

def least(task: list[str], n: int) -> int:
    if n == 0:
        return len(task)
    hmap = {}
    for letters in task:
        if letters not in hmap:
            hmap[letters] = 0
        hmap[letters] += 1
    heap = [(-v, k) for k, v in  hmap.items()]
    heapq.heapify(heap) 
    t = 0
    while heap:
        temp = []
        ex = 0
        for _ in range(n + 1):
            if not heap:
                break
            val, key = heapq.heappop(heap)
            val += 1
            if val < 0:
                temp.append((val, key))
            ex += 1
        for item in temp:
            heapq.heappush(heap, item)
        t += (n + 1) if heap else ex
    return t

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (task, n, expec) in enumerate(inputs, start=1):
    result = least(task, n)
    if result == expec:
        print(f"example: {idx} => {result} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} => {RED}FAIL{RESET}")
