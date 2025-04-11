from typing import List
def solve(ops: List[str], target:int) -> int:

    for i in reversed(ops):

        if "-" in i:
            target += 1
        elif "+" in i:
            target -= 1
    return target

l, n = ["x++", "--x", "--x"], 12

result = solve(l, n)

print(result)
