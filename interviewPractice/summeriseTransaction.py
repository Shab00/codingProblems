from collections import defaultdict

inputs = [
    (
        [
            {"account": "ACC1", "amount": 100},
            {"account": "ACC2", "amount": 50},
            {"account": "ACC1", "amount": -20},
            {"account": "ACC3", "amount": 200},
            {"account": "ACC2", "amount": 25}
        ],
        {
            "ACC1": 80,
            "ACC2": 75,
            "ACC3": 200
        }
    ),
    (

[
    {"account": "ACC1", "amount": 100},
    {"amount": 50},
    {"account": "ACC2"},
    {"account": "ACC3", "amount": "x"},
    {"account": "ACC1", "amount": -20}
],

{
    "ACC1": 80
}
        )
]

def find(records: dict[str, str, str, int]) -> dict[str, int]:
    result = defaultdict(int)

    for record in records:
        try:
            amount = int(record["amount"])
            result[record["account"]] += amount
        except(KeyError, ValueError):
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

