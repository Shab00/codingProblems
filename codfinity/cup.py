def solve(a: int, b: int) -> None:
    
    result = 0
    if a >= b:
        a, b = b, a

    for i in range(a, b):
        num_str = str(i)
        if len(num_str) == len(set(num_str)):
            result += 1
    return result

a = 100
b = 1000 

result = solve(a, b)
print(result)
