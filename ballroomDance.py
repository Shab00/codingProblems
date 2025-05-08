from typing import List

def solve(boys:List[int], girls:List[int]) -> int:
    print(f"boys:{repr(boys)}, girls:{repr(girls)}")
    count = 0
    while boys:
        for i in girls:
            partners = abs(boys[0] - i)
            if partners == 1:
                count += 1
        boys.pop(0)

    return count





boys, girls = [1, 4, 6, 2], [5, 1, 5, 7, 9]

result = solve(boys, girls)

print(result)
