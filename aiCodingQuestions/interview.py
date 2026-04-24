from collections import defaultdict

inputs = [
    (["x:1", "x:-1", "d:3"], "d: 3"),
    (["a:2", "a:-2"], ""),
    (["a:1", "b:2", "a:3", "b:-1"], "a: 4, b: 1"),
    (["y: 5 ", "y:-5", "z:7"], "z: 7"),
    (["p:10", "q:20", "p:-5", "q:-10"], "p: 5, q: 10"),
    (["m:0", "n:2"], "n: 2"),
    (["r:5", "s:-5", "r:-5", "s:5"], ""),
    (["x:1"], "x: 1"),
    ([], ""),
    (["a: 1", "a:1", "a:-2"], ""),
    (["b:1000", "b:-999", "c:999"], "b: 1, c: 999"),
]

def add(s: str) -> str:
    hmap = defaultdict(int)
    for i in s:
        key, value = i.split(":")
        hmap[key] += int(value)

    for key in list(hmap):
        if hmap[key] == 0:
            del hmap[key]

    result = ', '.join([f"{k}: {v}" for k, v in hmap.items()])

    return result

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (n, expec) in enumerate(inputs, start=1):
    result = add(n)
    if result == expec:
        print(f"example: {idx} => {result} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} => {RED}FAIL{RESET}")
