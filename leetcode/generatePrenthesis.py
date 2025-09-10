def generate(n: int) -> list[str]:

    sol = []
    ret = []
    def backtrack(left_count, right_count):
        if len(sol) == 2 * n:
            ret.append("".join(sol))
            return
        if left_count < n:
            sol.append('(')
            backtrack(left_count + 1, right_count)
            sol.pop()
        if right_count < left_count:
            sol.append(')')
            backtrack(left_count, right_count + 1)
            sol.pop()
    backtrack(0, 0)
    return ret

inputs = [(3, ["((()))","(()())","(())()","()(())","()()()"]),
          (1, ["()"])]

for i, e in inputs:
    result = generate(i)
    print(
            f"inputs:\n{i}\n"
            f"backtracking function outputs:\n{result}\n"
            f"expected:\n{e}\n"
            f"{'-'*50}"
            )
