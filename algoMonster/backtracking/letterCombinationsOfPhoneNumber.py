def letter_combinations_of_phone_number(digits: str) -> list[str]:
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    res: list[str] = []

    if digits == '':
        return []

    def dfs(start_index: int, path: list[str]) -> None:
        if start_index == len(digits):
            res.append("".join(path))
            return

        for letter in phone_map[digits[start_index]]:
            path.append(letter)
            dfs(start_index + 1, path)
            path.pop()

    dfs(0, [])
    return res

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

inputs = [
    ("56", ["jm", "jn", "jo", "km", "kn", "ko", "lm", "ln", "lo"]),
    ("2", ["a", "b", "c"]),
    ("", []),
    ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
    ("79", ["pw", "px", "py", "pz", "qw", "qx", "qy", "qz", "rw", "rx", "ry", "rz", "sw", "sx", "sy", "sz"]),
]

for idx, (digits, expected) in enumerate(inputs, start=1):
    result = letter_combinations_of_phone_number(digits)
    if sorted(result) == sorted(expected):
        print(f"test {idx}: {result} == {expected} => {GREEN}PASS{RESET}")
    else:
        print(f"test {idx}: {result} != {expected} => {RED}FAIL{RESET}")
