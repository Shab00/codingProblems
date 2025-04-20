def solve(a:int, b:int)->int:
        print(f"a: {a}, b: {b}")

        count = 0

        while b > a:
            a *=  3
            b *= 2
            count += 1
        return count

a, b = 17, 100
result = solve(a, b)
print(result)
