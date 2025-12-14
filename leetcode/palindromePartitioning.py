from collections import Counter
inputs = [
        ("aab", [["a","a","b"],["aa","b"]]),
        ("a", [["a"]])
        ]

def isPal(s: str) -> list[list[str]]:
    pass

PURPLE = "\033[95m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (s, expec) in enumerate(inputs, start=1):
    result = isPal(s)

    if not isinstance(result, list):
        print(f"example: {idx} => {s} => {PURPLE}ERROR{RESET}: isPal must return a list")
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
