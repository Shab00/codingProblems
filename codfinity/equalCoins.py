def solve(a:int,b:int,c:int,n:int)->str:
    print(f"a: {a}, b: {b}, c: {c}, n: {n}")
   

    max_coins = max(a, b, c)
    
    required = (max_coins - a) + (max_coins - b) + (max_coins - c)
    
    if n >= required and (n - required) % 3 == 0:
        return "YES"
    else:
        return "NO"

a, b, c, n = 5, 3, 2, 8

result = solve(a, b, c, n)

print(result)
