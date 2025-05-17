from collections import deque

def solve(maze: list) -> list:
    start = None
    end = None
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == "S":
                start = (row, col)
            if maze[row][col] == "E":
                end = (row, col)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    path = deque()
    path.append((start, [start]))
    visted = set()
    visted.add(start)
    while path:
       (curRow, curCol) , pathSoFar = path.popleft()
       if (curRow, curCol) == end:
           return pathSoFar
       for dr, dc in directions:
           nr, nc = curRow + dr, curCol + dc
           if (0 <= nr < len(maze) and
               0 <= nc < len(maze[0]) and
               maze[nr][nc] != 1 and
               (nr, nc) not in visted):
               path.append(((nr, nc), pathSoFar + [(nr, nc)]))
               visted.add((nr, nc))
    return None

maze = [
    ["S", 0, 1, 0, "E"],
    [0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1]
]

result = solve(maze)
print(result)
