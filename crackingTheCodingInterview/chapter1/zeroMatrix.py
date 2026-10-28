def zero_matrix(matrix: list[list[int]]) -> None:

    zero_rows = set()
    zero_cols = set()

    for m in range(len(matrix)):
        for n in range(len(matrix[m])):
            if matrix[m][n] == 0:
                zero_rows.add(m)
                zero_cols.add(n)

    for m in range(len(matrix)):
        for n in range(len(matrix[m])):
            if m in zero_rows or n in zero_cols:
                matrix[m][n] = 0

import copy

GREEN, RED, RESET = "\033[92m", "\033[91m", "\033[0m"

tests = [
    # (matrix, expected)

    # 1. Empty matrix
    ([], []),

    # 2. Single zero
    ([[0]], [[0]]),

    # 3. Single non-zero
    ([[1]], [[1]]),

    # 4. No zeros: nothing changes
    ([[1, 2],
      [3, 4]],
     [[1, 2],
      [3, 4]]),

    # 5. Zero in the centre
    ([[1, 2, 3],
      [4, 0, 6],
      [7, 8, 9]],
     [[1, 0, 3],
      [0, 0, 0],
      [7, 0, 9]]),

    # 6. Zero in a corner
    ([[0, 2, 3],
      [4, 5, 6],
      [7, 8, 9]],
     [[0, 0, 0],
      [0, 5, 6],
      [0, 8, 9]]),

    # 7. Two zeros, different rows and columns
    ([[1, 0, 3],
      [4, 5, 6],
      [7, 8, 0]],
     [[0, 0, 0],
      [4, 0, 0],
      [0, 0, 0]]),

    # 8. Wide matrix (2x4)
    ([[1, 2, 3, 4],
      [5, 0, 7, 8]],
     [[1, 0, 3, 4],
      [0, 0, 0, 0]]),

    # 9. Tall matrix (3x2)
    ([[1, 2],
      [3, 4],
      [0, 6]],
     [[0, 2],
      [0, 4],
      [0, 0]]),

    # 10. Single row
    ([[1, 0, 3]],
     [[0, 0, 0]]),

    # 11. Single column
    ([[1],
      [0],
      [3]],
     [[0],
      [0],
      [0]]),

    # 12. All zeros
    ([[0, 0],
      [0, 0]],
     [[0, 0],
      [0, 0]]),

    # 13. Two zeros in the same row
    ([[0, 0, 3],
      [4, 5, 6]],
     [[0, 0, 0],
      [0, 0, 6]]),

    # 14. Negative numbers
    ([[-1, 0],
      [2, -3]],
     [[0, 0],
      [2, 0]]),
]

for i, (matrix, expected) in enumerate(tests, 1):
    m = copy.deepcopy(matrix)
    zero_matrix(m)                  # should modify m in place
    if m == expected:
        print(f"Test {i}: {GREEN}PASS{RESET}")
    else:
        print(f"Test {i}: {RED}FAIL{RESET}  expected {expected}, got {m}")
