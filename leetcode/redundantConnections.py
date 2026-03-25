from collections import defaultdict

inputs = [([[1,2],[1,3],[2,3]], [2,3]),
          ([[1,2],[2,3],[3,4],[1,4],[1,5]], [1,4])]

def find(edges: list[list[int]]) -> list[int]:
    nodeMap = defaultdict(list)
    reault = []
    def dfs(node, target, vis):
        if node == target:
            return True

        vis.add(node)
        for neig in nodeMap[node]:
            if neig not in vis:
                if dfs(neig, target, vis):
                    return True
        return False
    for a, b in edges:
        vis = set()
        if a in nodeMap and b in nodeMap:
            if dfs(a, b, vis):
                result = [a, b]
        nodeMap[a].append(b)
        nodeMap[b].append(a)
    return result

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (edges, expec) in enumerate(inputs, start=1):
    result = find(edges)
    if result == expec:
        print(f"example: {idx} => {result} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} => {RED}FAIL{RESET}")
