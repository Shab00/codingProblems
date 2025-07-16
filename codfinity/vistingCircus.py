from typing import List

def solve(groups:List[int]) -> int:
    ones = twos = threes = fours = 0
    for g in groups:
        if g == 1:
            ones += 1
        elif g == 2:
            twos += 1
        elif g == 3:
            threes += 1
        elif g == 4:
            fours += 1

    taxis = fours

    pair_3_1 = min(threes, ones)
    taxis += pair_3_1
    threes -= pair_3_1
    ones -= pair_3_1

    taxis += threes

    taxis += twos // 2
    twos = twos % 2

    if twos:
        taxis += 1
        ones -= min(2, ones)

    if ones > 0:
        taxis += (ones + 3) // 4

    return taxis               

inputs = [1, 2, 4, 3, 3]

result = solve(inputs)

print(result)
