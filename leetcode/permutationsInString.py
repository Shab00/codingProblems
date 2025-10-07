def check(s1: str, s2: str) -> bool:
    pass

inputs = [("ab", "eidbaooo", True),
          ("ab", "eidboaoo", False)]

for s1, s2, e in inputs:
    result = check(s1, s2)
    print(
            f"inputs:\n{s1, s2}\n"
            f"outputs:\n{result}\n"
            f"expected:\n{e}\n"
            f"{'-'*50}"
            )
