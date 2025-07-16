def solve(s:str) -> str:
    if len(s) < 7:
        return s
    l = []
    slit = list(s)
    for i, char in enumerate(slit):
        if i == 0 or i == len(slit) - 1:
            l.append(char)
    l.insert(1, len(slit) - 2)
    result = "".join([str(x) for x in l])
    return result

def op(s:str) -> str:
    if len(s) < 7:
        return s
    return f"{s[0]}{len(s) - 2}{s[-1]}"

s = "optimization"
w = "word"
resultTwo = solve(w)
result = solve(s)
opr = op(w)
oprt = op(s)
print(resultTwo)
print(result)
print(opr)
print(oprt)
