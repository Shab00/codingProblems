from typing import List

def solve(nums:List[List[int]]) -> List[int]:
    print(f"nums: {nums}")
    # Write your code here
    f, s, t = 0, 0, 0
    new = []
    for lists in nums:
        f += lists[0]
        s += lists[1]
        t += lists[2]
    new = [- f, - s, - t]

    return new

inputs = [[1, 2, 3], [9, -2, 8], [17, 2, 50]]

result = solve(inputs)

print(result)
