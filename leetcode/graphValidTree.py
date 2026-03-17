from collections import defaultdict 

inputs = [(5, [[0, 1], [0, 2], [0, 3], [1, 4]], True),
          (5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], False)]

def valid(n: int, edges: list[list[int]]) -> bool:
    
    if n - 1 != len(edges):
        return False

    nodeMap = defaultdict(list)    
    for node, link in edges:
        nodeMap[node].append(link)
        nodeMap[link].append(node)
    visited = set()
    def dfs(node, parent):
        if node in visited:
            return False
        visited.add(node)
        for neighbor in nodeMap[node]:
            if neighbor == parent:
                continue
            if not dfs(neighbor, node):
                return False
        return True

    if not dfs(0, -1):
        return False

    if len(visited) != n:
        return False

    return True

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (n, edges, expected) in enumerate(inputs, start=1):
    result = valid(n, edges)
    if result == expected:
        print(f"example: {idx} => {result} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} => {RED}FAIL{RESET}")
