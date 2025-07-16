def solve(n:int)->str:

    luckyNumbers = []
    for i in range(1, n + 1):
        if all(d in {'4', '7'} for d in str(i)):
            luckyNumbers.append(i)
    for i in luckyNumbers:
        if n % i == 0:
            return "YES"
    return"NO"

inputs = [47, 16, 78, 28, 444, 50, 74, 99]
for i in inputs:
    result = solve(i)
    print(result)
