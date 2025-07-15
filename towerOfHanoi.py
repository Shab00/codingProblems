def solve(n: int) -> list[list]:
    
    def move(num: int, sou: int, dest: int, aux: int, ml: list):

        if num == 1:
            ml.append([sou, dest])
            return
        else:
            move(num - 1, sou, aux, dest, ml)
            ml.append([sou, dest])
            move(num - 1, aux, dest, sou, ml)

    ml = []
    move(n, 0, 2, 1, ml)
    return ml

inputs = [1, 2, 3, 8]
for i in inputs:
    result = solve(i)
    print(result)
