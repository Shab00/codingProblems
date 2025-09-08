def evalP(tokens: list[str]) -> int:
    stack = []
    for i in range(len(tokens)):
        if tokens[i] == '+':
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
            continue
        if tokens[i] == '-':
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)
            continue
        if tokens[i] == '*':
            b = stack.pop()
            a = stack.pop()
            stack.append(a * b)
            continue
        if tokens[i] == '/':
            b = stack.pop()
            a = stack.pop()
            stack.append(int(a / b))
            continue
        else:
            stack.append(int(tokens[i]))
    return stack[0]

inputs = [(["2","1","+","3","*"], 9), 
          (["4","13","5","/","+"], 6),
          (["10","6","9","3","+","-11","*","/","*","17","+","5","+"], 22)]

for i, e in inputs:
    result = evalP(i)
    print(
            f"inputs:\n{i}\n"
            f"outputs:\n{result}\n"
            f"expected:\n{e}\n"
            f"{'-'*50}"
            )
