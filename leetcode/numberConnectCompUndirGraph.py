inputs = [(5, [[0,1],[1,2],[3,4]], 2),
          (5, [[0,1],[1,2],[2,3],[3,4]], 1)]

def count(n, edges):
    parent = list(range(n))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py 

    for a, b in edges:
        union(a, b)

    roots = set(find(x) for x in range(n))
    return len(roots)

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (n, edges, expec) in enumerate(inputs, start=1):
    result = count(n, edges)
    if result == expec:
        print(f"example: {idx} => {result} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} => {RED}FAIL{RESET}")
