from collections import defaultdict
from collections import Counter

inputs = [
    ([3, 4, 2, 3, 4, 7], 4),
    ([1, 0, 5, 3], -1)
]

def find(cards: list[int]) -> int:
    window: Counter[int] = Counter()
    left = 0
    shortest = len(cards) + 1
    for right in range(len(cards)):
        window[cards[right]] += 1
        while window[cards[right]] == 2:
            shortest = min(shortest, right - left + 1)
            window[cards[left]] -= 1
            left += 1
    return shortest if shortest != len(cards) + 1 else -1

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (arr, expec) in enumerate(inputs, start=1):
    result = find(arr)
    if result == expec:
        print(f"example: {idx} => {result} == {expec} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} != {expec} => {RED}FAIL{RESET}")
