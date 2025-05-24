def solve(n:int)->str:

    b = n // 2021

    for i in range(b + 1):

        dif = n - (2021 * i)
        if dif % 2020 == 0:
            return "YES"
    return "NO"
inputs = [4041, 4042, 8081, 2019, 4053, 3031]

for i in inputs:
    result = solve(i)
    print(result)
