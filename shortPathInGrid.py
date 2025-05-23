from collections import deque

def solve(maze: list, start: tuple, end: tuple) -> int:
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    path = deque()
    path.append((start, [start]))
    visted = set()
    visted.add(start)
    while path:
        (curRow, curCol), pathSoFar = path.popleft()
        if (curRow, curCol) == end:
            return len(pathSoFar) - 1
        for dr, dc in directions:
            nr, nc = curRow + dr, curCol + dc
            if (0 <= nr < len(maze) and
                0 <= nc < len(maze[0]) and 
                maze[nr][nc] != 1 and 
                (nr, nc) not in visted):
                path.append(((nr, nc), pathSoFar + [(nr, nc)]))
                visted.add((nr, nc))

    return -1

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
