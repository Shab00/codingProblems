def generate(n: int) -> list[str]:
    
    leftBrace = '('
    rightBrace = ')'

    sol = []
    ret = []

    def backtrack(i):
        if i == n:
            ret.append("".join(sol))
            return

        sol.append(leftBrace)
        backtrack(i+1)
        sol.pop()
    backtrack(0)
    return ret

inputs = [(3, ["((()))","(()())","(())()","()(())","()()()"]),
          (1, ["()"])]

for i, e in inputs:
    result = generate(i)
    print(
            f"inputs:\n{i}\n"
            f"outputs:\n{result}\n"
            f"expected:\n{e}\n"
            f"{'-'*50}"
            )
