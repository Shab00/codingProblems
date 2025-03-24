def solve(s:str) -> str:
    if len(s) < 7:
        return s
    l = []
    count = 0
    slit = list(s)
    for i in range(len(slit)):
        if i == slit[0] or i == slit[-1]:
            print(slit[count])
            count += 1

s = "optimization"
w = "word"
resultTwo = solve(w)
result = solve(s)

print(resultTwo)
print(result)
