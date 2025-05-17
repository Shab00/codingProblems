from collections import deque

def solve(maze: list, start: tuple, end: tuple) -> int:
    pass

maze = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
          ]

start = (0, 0)
end = (4, 4)

result = solve(maze, start, end)
print(result)
