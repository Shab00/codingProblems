from typing import List

def solve(boys:List[int], girls:List[int]) -> int:
    boys.sort()
    girls.sort()
    print(f"boys:{repr(boys)}, girls:{repr(girls)}")
    count = 0
    i = 0
    j = 0
    while i < len(boys) and j < len(girls):

        comp = abs(boys[i] - girls[j])

        if comp <= 1:
            count += 1
            i += 1
            j += 1
        elif comp > 1:
            if boys[i] < girls[j]:
                i += 1
            else:
                j += 1
    return count





boys, girls = [4,5,4,4], [5,3,4,2,4]

result = solve(boys, girls)

print(result)
