def solve(a:int, b:int, c:int)->str:

    plus = a + b
    minus = a - b

    if plus == c:
        return "+"
    elif minus == c:
        return "-"

    

a, b, c = 1, 2, 3

d, e, f = 2, 9, -7

ex1 = solve(a, b, c)
ex2 = solve(d, e, f)
print(ex1)
print(ex2)
