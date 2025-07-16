from typing import List

def solve(oranges: List[int], candies: List[int]) -> int:

    minCandy = min(candies)
    minOrange = min(oranges)
    moves = 0
    for i, j in zip(candies, oranges):
        extraCandy = i - minCandy
        extraOrange = j - minOrange
        moves += max(extraCandy, extraOrange)
    return moves

oranges, candies = [3, 2, 3], [3, 5, 6]

result = solve(oranges, candies)

print(result)
