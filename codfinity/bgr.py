def solve(a,b):

    time = 0
    while a < b:

        a *= 3
        b *= 2
        time += 1

    return time

result = solve(4, 7)

print(result)
