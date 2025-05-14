def solve(n:int)->int:
    count = 0
    while n > 1:
        if n % 6 == 0:
            n //= 6
        elif n % 2 == 0:
            return -1
        else:
            n *= 2
        count += 1
    return count

inputs = [1, 2, 48, 108, 216, 36, 18]

for i in inputs:
    result = solve(i)
    print(result)
