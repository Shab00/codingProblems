def letterCombo(digits: str) -> list[str]:
    pass

inputs = [("23", ["ad","ae","af","bd","be","bf","cd","ce","cf"]),
          ("", []),
          ("2", ["a","b","c"])]

for i, e in inputs:
    result = letterCombo(i)
    print(f"inputs: {i} || outputs: {result} || expected: {e}")
