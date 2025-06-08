def solve(code: str) -> str:
    
    tick_dict = {".": "0", "-.": "1", "--": "2"}
    decoded = [] 
    i = 0
    while i < len(code):

        if i < len(code) - 1 and code[i] == ".":
            decoded.append(tick_dict[code[i]])
            i += 1
        elif i < len(code) - 1 and code[i] == "-" and code[i + 1] == ".":
            decoded.append(tick_dict[code[i] + code[i + 1]])
            i += 2
        elif i < len(code) - 1 and code[i] == "-" and code[i + 1] == "-":
            decoded.append(tick_dict[code[i] + code[i + 1]])
            i += 2
        else:
            i += 1

    return ''.join(decoded)

inputs = [".-.--", ".-.--.--.", "-.--.--."]

for i in inputs:

    result = solve(i)
    print(result)
