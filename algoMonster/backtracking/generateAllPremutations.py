def permutations(letters: str) -> list[str]:
    res: list[str] = []
    n = len(letters)
    used = [False] * n

    def dfs(depth: int, path: list[str]) -> None:
        if depth == n:
            res.append(''.join(path))
            return
        for i in range(n):
            if not used[i]:
                used[i] = True
                path.append(letters[i])
                dfs(depth + 1, path)
                path.pop()
                used[i] = False

    dfs(0, [])
    return res

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

inputs = [
    ("a", ["a"]),
    ("ab", ["ab", "ba"]),
    ("abc", ["abc", "acb", "bac", "bca", "cab", "cba"]),
    ("", [""]),
]

for idx, (letters, expected) in enumerate(inputs, start=1):
    result = permutations(letters)
    if sorted(result) == sorted(expected):
        print(f"test {idx}: {result} == {expected} => {GREEN}PASS{RESET}")
    else:
        print(f"test {idx}: {result} != {expected} => {RED}FAIL{RESET}")
