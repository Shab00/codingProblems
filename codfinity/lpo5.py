def solve(n:int)->int:
    
    result = 1
    for _ in range(n):
        result *= 5
    return result


n = 16
result = solve(n)

print(result)
