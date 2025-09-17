def search(matrix: list[list[int]], target: int) -> bool:
    l = []
    for rows in range(len(matrix)):
        for cols in range(len(matrix[rows])):
            l.append(matrix[rows][cols])  
    print(l)
    s, r = 0, len(l) - 1
    while s <= r:
        m = (s + r) // 2
        if l[m] == target:
            return True
        elif l[m] > target:
            r = m - 1
        elif l[m] < target:
            s = m + 1
    return False


inputs = [([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3, True),
          ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13, False),
          ([[1]], 0, False)]

for i, t, e in inputs:
    result = search(i, t)
    print(
            f"inputs:\n{i}\n"
            f"outputs:\n{result}\n"
            f"expected:\n{e}\n"
            f"{'-'*50}"
            )
