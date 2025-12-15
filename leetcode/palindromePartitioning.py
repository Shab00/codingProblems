from collections import Counter
inputs = [
        ("aab", [["a","a","b"],["aa","b"]]),
        ("a", [["a"]])
        ]

def palPart(s: str) -> list[list[str]]:
    res, part = [], []
    
    def dfs(j, i):
        depth = j
        print("  " * depth + f"dfs(j={j}, i={i}) part={part}")
        if i >= len(s):
            if i == j:
                res.append(part[:])
            return

        if isPal(s, j, i):
            part.append(s[j : i + 1])
            dfs(i + 1, i + 1)
            part.pop()

        dfs(j, i + 1)

    dfs(0, 0)
    return res

def isPal(s: str, l: int, r: int) -> bool:
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

PURPLE = "\033[95m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (s, expec) in enumerate(inputs, start=1):
    result = palPart(s)

    if not isinstance(result, list):
        print(f"example: {idx} => {s} => {PURPLE}ERROR{RESET}: palPart must return a list")
        continue

    bad = None
    for p in result:
        if not isinstance(p, (list, tuple)) or "".join(p) != s or any(x != x[::-1] for x in p):
            bad = p
            break
    if bad is not None:
        print(f"example: {idx} => {s} => FAIL - invalid partition returned: {bad}")
        continue

    if Counter(tuple(p) for p in result) == Counter(tuple(p) for p in expec):
        print(f"example: {idx} => {s} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {s} => {RED}FAIL{RESET}")
