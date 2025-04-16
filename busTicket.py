def solve(n:int, m:int, a:int, b:int)->int:
    print(f"n: {n} m: {m}, a: {a}, b: {b}")
    totalCost = n * a
    fullSp = n // m
    totalSp = fullSp * b

    remain = fullSp * m



n, m, a, b, = 10, 3, 1, 2

result = solve(n, m, a, b)

print(result)
