from typing import List

def solve(boys:List[int], girls:List[int]) -> int:
    print(f"boys:{repr(boys)}, girls:{repr(girls)}")
    pass

boys, girls = [1, 4, 6, 2], [5, 1, 5, 7, 9]

result = solve(boys, girls)

print(result)
