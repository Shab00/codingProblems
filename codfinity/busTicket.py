def solve(n:int, m:int, a:int, b:int)->int:
    print(f"n: {n} m: {m}, a: {a}, b: {b}")

    totalCost = n * a
    fullSp = n // m
    totalSp = fullSp * b
    
    leftOver = n % m
    
    totalSp += min(b, leftOver * a)
    
    return min(totalCost, totalSp)

n, m, a, b, = 10, 3, 5, 1

result = solve(n, m, a, b)

print(result)
