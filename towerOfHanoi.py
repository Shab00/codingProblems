def solve(n: int) -> list[list]:
    def move(num: int, sou: int, dest: int, aux: int, ml: list):

        if num == 1:
            ml.append([sou, dest])
            return


    ml = []
    move(n, 0, 2, 1, ml)
    return ml

inputs = [1, 2, 3]
for i in inputs:
    result = solve(i)
    print(result)
