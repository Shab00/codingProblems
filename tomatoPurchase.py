def solve(n:int, a:int, b:int) -> int:
    promotion_cost = (n // 2) * b + (n % 2) * a

    normal_cost = n * a

    return min(promotion_cost, normal_cost)

values = [
    (2, 5, 9),
    (3, 7, 11),
    (4, 7, 6),
    (1, 2, 10),
    (5, 8, 7)
]
for n, a, b in values:
    result = solve(n, a, b)
    print(f"For n={n}, a={a}, b={b}, result={result}")

