def solve(n:int) -> int:
        print(f"n: {n}")
        count = 0
        for i in range(n + 1):
            if i % 10 == 9:
                count += 1

        return count 

inputs = [9, 19, 1, 99, 100]

for i in inputs:
    result = solve(i)
    print(result)
