def solve(x:int, y:int)->list[int]:
    result = []
    if x > y:
        result.append(y)
        result.append(x)
        return result
    else:
        result.append(x)
        result.append(y)
        return result


x = 200
y = 150

r  = solve(x, y)

print(r)
