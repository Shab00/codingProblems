def rotate(matrix: list[list[int]]) -> None:
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()

import copy

GREEN, RED, RESET = "\033[92m", "\033[91m", "\033[0m"

tests = [
    # (matrix, expected)

    # 1. Empty matrix
    ([], []),

    # 2. 1x1
    ([[1]], [[1]]),

    # 3. 2x2
    ([[1, 2],
      [3, 4]],
     [[3, 1],
      [4, 2]]),

    # 4. 3x3 (odd size: has a centre)
    ([[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]],
     [[7, 4, 1],
      [8, 5, 2],
      [9, 6, 3]]),

    # 5. 4x4 (even size: two layers)
    ([[1,  2,  3,  4],
      [5,  6,  7,  8],
      [9,  10, 11, 12],
      [13, 14, 15, 16]],
     [[13, 9,  5, 1],
      [14, 10, 6, 2],
      [15, 11, 7, 3],
      [16, 12, 8, 4]]),

    # 6. 5x5 (odd size: two layers plus centre)
    ([[1,  2,  3,  4,  5],
      [6,  7,  8,  9,  10],
      [11, 12, 13, 14, 15],
      [16, 17, 18, 19, 20],
      [21, 22, 23, 24, 25]],
     [[21, 16, 11, 6,  1],
      [22, 17, 12, 7,  2],
      [23, 18, 13, 8,  3],
      [24, 19, 14, 9,  4],
      [25, 20, 15, 10, 5]]),

    # 7. All the same value
    ([[0, 0, 0],
      [0, 0, 0],
      [0, 0, 0]],
     [[0, 0, 0],
      [0, 0, 0],
      [0, 0, 0]]),

    # 8. Negative numbers
    ([[-1, -2],
      [-3, -4]],
     [[-3, -1],
      [-4, -2]]),

    # 9. Duplicate values
    ([[1, 1, 2],
      [1, 1, 2],
      [3, 3, 3]],
     [[3, 1, 1],
      [3, 1, 1],
      [3, 2, 2]]),
]

for i, (matrix, expected) in enumerate(tests, 1):
    m = copy.deepcopy(matrix)
    rotate(m)                       # should modify m in place
    if m == expected:
        print(f"Test {i}: {GREEN}PASS{RESET}")
    else:
        print(f"Test {i}: {RED}FAIL{RESET}  expected {expected}, got {m}")

# 10. Rotating four times should give back the original
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
original = copy.deepcopy(m)
for _ in range(4):
    rotate(m)
if m == original:
    print(f"Test 10: {GREEN}PASS{RESET}")
else:
    print(f"Test 10: {RED}FAIL{RESET}  expected {original}, got {m}")
