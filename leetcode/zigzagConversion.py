def convert(s: str, n: int) -> str:
    if n <= 1:
        return s
    
    numRows = [""] * n
    down = True 
    curRow = 0

    for letter in s:
        numRows[curRow] += letter
        if down:
            curRow += 1
        else:
            curRow -= 1

        if curRow == n - 1:
            down = False
        elif curRow == 0:
            down = True

    return "".join(numRows)

inputs = [("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
          ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
          ("A", 1, "A")]

for i, j, z in inputs:
    result = convert(i, j)
    print(f"Input: {i, j} || Output: {result} || Expected: {z}")
