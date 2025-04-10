from typing import List

def solve(rooms: List[List[int]]) -> int:
    count = 0
    for i in rooms:
        num = i[1] - i[0]
        if num >= 2:
            count += 1
    return count

l = [[2, 2], [1, 10], [3, 5], [0, 2]]

result = solve(l)

print(result)
