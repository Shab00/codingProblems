from collections import defaultdict

inputs = [
    ("abccabcabcc", 3),
    ("aaaabaaa", 2)
]

def find(s: str) -> int:
    hmap = defaultdict(int)

    l = 0
    length = 0

    for r in range(len(s)):
        hmap[s[r]] += 1

        while hmap[s[r]] > 1:
            hmap[s[l]] -= 1
            if hmap[s[l]] == 0:
                del hmap[s[l]]
            l += 1 
        length = max(length, r - l + 1)
    return length

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (arr, expec) in enumerate(inputs, start=1):
    result = find(arr)
    if result == expec:
        print(f"example: {idx} => {result} == {expec} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} != {expec} => {RED}FAIL{RESET}")
