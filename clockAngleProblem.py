from typing import List

def solve(target_angle: int) -> List:
    
    result = []
    for i in range(1, 13):
        for pn in (target_angle * 2, (360 - target_angle) * 2): 
            M1 = ((60 * i) + pn) / 11
            M2 = ((60 * i) - pn) / 11
            if isinstance(M1, (int, float)) and 59 >= M1 >= 0 and M1 == int(M1):
                result.append(i)
                result.append(int(M1))
            if isinstance(M2, (int, float)) and 59 >= M2 >= 0 and M2 == int(M2):
                result.append(i)
                result.append(int(M2))
                break
    return result[0:2]

inputs = [(120,[4, 0]), (90,[3,0]), (200,[2,40]), (54, [4, 12]), (236, [1, 28])]

for i, expected in inputs:
    result = solve(i)
    print(f"Inputs: {i} | Output: {result} | Expected: {expected}")
