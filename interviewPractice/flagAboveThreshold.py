from collections import defaultdict

inputs = [
([
    {"entity": "BankA", "exposure": 120},
    {"entity": "BankB", "exposure": 80},
    {"entity": "BankA", "exposure": 50},
    {"entity": "BankC", "exposure": 200}], 150, ["BankA", "BankC"]),
([
    {"entity": "BankA", "exposure": 120},
    {"entity": "", "exposure": 90},
    {"entity": "BankB"},
    {"exposure": 100},
    {"entity": "BankA", "exposure": "x"},
    {"entity": "BankC", "exposure": 200},
    {"entity": "BankA", "exposure": 50}], 150, ["BankA", "BankC"])
]

def find(records: list[dict], thresh: int) -> list[str]:
    result = []
    dic = defaultdict(int)

    for record in records:
        try:
            name = record["entity"]
            if not name:
                continue
            value = int(record["exposure"])
            dic[name] += value

        except(ValueError, KeyError):
            continue

    for name, value in dic.items():
        if value > thresh:
            result.append(name)

    return sorted(result)


GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (n, t, expec) in enumerate(inputs, start=1):
    result = find(n, t)
    if result == expec:
        print(f"example: {idx} => {result} == {expec} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} != {expec} => {RED}FAIL{RESET}")

