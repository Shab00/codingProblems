def isValid(s: str) -> bool:
    pass

inputs = [("()", True),
          ("()[]{}", True),
          ("(]", False),
          ("([])", True),
          ("([)]", False)]

for i, e in inputs:
    result = isValid(i)
    print(
            f"inputs:\n{i}\n"
            f"outputs:\n{result}\n"
            f"expected:\n{e}\n"
            f"{'-' * 50}"
            )
