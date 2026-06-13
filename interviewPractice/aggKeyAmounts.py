from collections import defaultdict

inputs = [(["a:1", "b:4", "a:2", "c:3", "b:1"], {"a": 3, "b": 5, "c": 3}),
          (["a:1", "bad", ":3", "b:x", "a:2"], {"a": 3})]

def find(arr: list[str]) -> dict[str: int]:
    result = defaultdict(int)

    for amount in arr:
        try:
            key, value = amount.split(":")
            num = int(value)
            if not key:
                continue
            result[key] += num
        except(ValueError, TypeError, NameError):
            continue

    return dict(result)

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (n, expec) in enumerate(inputs, start=1):
    result = find(n)
    if result == expec:
        print(f"example: {idx} => {result} == {expec} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} != {expec} => {RED}FAIL{RESET}")

