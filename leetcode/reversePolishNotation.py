def eval(tokens: list[str]) -> int:
    pass

inputs = [(["2","1","+","3","*"], 9), 
          (["4","13","5","/","+"], 6),
          (["10","6","9","3","+","-11","*","/","*","17","+","5","+"], 22)]

for i, e in inputs:
    result = eval(i)
    print(
            f"inputs:\n{i}\n"
            f"outputs:\n{result}\n"
            f"expected:\n{e}\n"
            f"{'-'*50}"
            )
