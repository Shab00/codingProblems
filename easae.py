def solve(expression:str)->int:
    parts = expression.split("+", 1)
    result = int(parts[0]) + int(parts[1])
    return result

a = "455+289"

result = solve(a)
print(result)
