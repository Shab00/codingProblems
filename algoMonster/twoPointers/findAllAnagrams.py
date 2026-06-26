from collections import defaultdict

inputs = [
    ("cbaebabacd", "abc", [0, 6]),
    ("abab", "ab", [0, 1, 2])
]

def find(arr: str, k: str) -> list[int]:
    token = defaultdict(int)
    check = defaultdict(int)
    result = []
    l = 0
    for char in k:
        token[char] += 1

    for r in range(len(arr)):
        check[arr[r]] += 1
        if (r - l + 1) > len(k):
            check[arr[l]] -= 1
            if check[arr[l]] == 0:
                del check[arr[l]] 
            l += 1
        if check == token:
            result.append(l)

    return result

         

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (arr, k, expec) in enumerate(inputs, start=1):
    result = find(arr, k)
    if result == expec:
        print(f"example: {idx} => {result} == {expec} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} != {expec} => {RED}FAIL{RESET}")
