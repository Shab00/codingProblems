def solve(s:str) -> str:
    l = list(s)
    l.reverse()
    result = []
    for i in l:
        if i == "d":
            result.append("b")
        if i == "b":
            result.append("d")
        if i == "w":
            result.append("w")   
    r = "".join(result)
    return r

def op(s:str) -> str:
    charmap = {"d": "b", "b": "d", "w": "w"}

    result = [charmap.get(char, "") for char in reversed(s)]
    return "".join(result)

s = "dwddddwbbb"
result = solve(s)
new = op(s)
print(new)
print(result)
