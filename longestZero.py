from typing import List

def solve(a:List[int])->int:
    print(f"a: {a}")
    
    maxsum, cursum = 0, 0

    for i in a:
        if i == 0:
            cursum += 1

        elif i == 1:
            cursum = 0

        maxsum = max(maxsum, cursum)

    return maxsum



binArray = [1,0,0,1,0], [1,1,1]

for i in binArray:
    result = solve(i)
    print(result)
