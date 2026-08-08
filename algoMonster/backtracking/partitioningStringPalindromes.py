def partition(s: str) -> list[list[str]]:
    res: list[list[str]] = []
    def dfs(start_index: int, path: list[str]) -> None:
        if start_index == len(s):
            res.append(path[:])
            return
        for end in range(start_index + 1, len(s) + 1):
            substring = s[start_index:end]
            if is_palindrome(substring):
                path.append(substring)
                dfs(end, path)
                path.pop()

    dfs(0, [])
    return res

def is_palindrome(sub: str) -> bool:
    return sub == sub[::-1]


GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

inputs = [
    ("aab", [["a", "a", "b"], ["aa", "b"]]),
    ("a", [["a"]]),
    ("", [[]]),
    ("aaa", [["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]]),
    ("ab", [["a", "b"]]),
]

def normalize(partitions):
    return sorted([sorted(p) for p in partitions])

for idx, (s, expected) in enumerate(inputs, start=1):
    result = partition(s)
    if normalize(result) == normalize(expected):
        print(f"test {idx}: {result} == {expected} => {GREEN}PASS{RESET}")
    else:
        print(f"test {idx}: {result} != {expected} => {RED}FAIL{RESET}")
