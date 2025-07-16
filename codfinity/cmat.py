from typing import List

def solve(n:int, bill_levels: List[int], bob_levels: List[int]) -> str:
    w = "I become the hero!"
    l = "Oh, no! The castle is locked!"

    levels = bill_levels + bob_levels
    for i in levels:
        if i != n:
            return w
    return l

n = 5

bill_levels = [3, 1, 2, 3]

bob_levels = [2, 2, 4, 5]

message = solve(n, bill_levels, bob_levels)
print(message)
