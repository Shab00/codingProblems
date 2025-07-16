def solve(x:int)->int:
        print(f"x: {x}")
        steps = [1, 2, 3, 4, 5]
        if x in steps:
            return x

        amountOfFives = x // 5
        
        return amountOfFives + (1 if x % 5 != 0 else 0)

inputs = [12, 41, 53, 97, 53404, 3, 200000]
for i in inputs:
    result = solve(i)
    print(result)
