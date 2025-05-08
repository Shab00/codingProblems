from typing import List

def solve(boys:List[int], girls:List[int]) -> int:
    boys.sort()
    girls.sort()
    print(f"boys:{repr(boys)}, girls:{repr(girls)}")
    count = 0
    i = boys[0]
    j = girls[0]
    while i < j:
        
    return count





boys, girls = [4,5,4,4], [5,3,4,2,4]

result = solve(boys, girls)

print(result)
