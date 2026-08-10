def generate_parentheses(n: int) -> list[str]:

    res: list[str] = []

    def dfs(open_count, close_count, path):
        if open_count == close_count == n:
            res.append(''.join(path))
            return
        if open_count < n:
            path.append('(')
            dfs(open_count + 1, close_count, path)
            path.pop()
        if close_count < open_count:
            path.append(')')
            dfs(open_count, close_count + 1, path)
            path.pop()
    
    dfs(0, 0, [])
    return res

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

inputs = [
    (1, ["()"]),
    (2, ["(())", "()()"]),
    (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
    (0, [""]),
]

for idx, (n, expected) in enumerate(inputs, start=1):
    result = generate_parentheses(n)
    if sorted(result) == sorted(expected):
        print(f"test {idx}: {result} == {expected} => {GREEN}PASS{RESET}")
    else:
        print(f"test {idx}: {result} != {expected} => {RED}FAIL{RESET}")
