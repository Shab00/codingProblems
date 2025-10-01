def charRep(s: str, k: int) -> int:
    pass

inputs = [("ABAB", 2, 4),
          ("AABABBA", 1, 4)]

for s, k, e in inputs:
    result = charRep(s, k)
    print(
            f"inputs:\n{s, k}\n"
            f"outputs:\n{result}\n"
            f"expexted:\n{e}\n"
            f"{'-'*50}"
            )
