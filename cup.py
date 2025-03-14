def solve(a: int, b: int) -> None:
    if a >= b:
        print("Error: 'a' must be less than 'b'")
    else:
        for i in range(a, b):
            print(i)

a = 100
b = 1000

solve(a, b)
