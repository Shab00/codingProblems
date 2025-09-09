def letterCombo(digits: str) -> list[str]:
    

    if not digits:
        return []

    keypad = {'2': ['a', 'b', 'c'],
              '3': ['d', 'e', 'f'],
              '4': ['g', 'h', 'i'],
              '5': ['j', 'k', 'l'],
              '6': ['m', 'n', 'o'],
              '7': ['p', 'q', 'r', 's'],
              '8': ['t', 'u', 'v'],
              '9': ['w', 'x', 'y', 'z']}

    sol = []
    ret = []
    n = len(digits)

    def backtrack(i, path):
        if i == n:
            ret.append("".join(sol))
            return

        for letter in keypad[digits[i]]:
            sol.append(letter)
            backtrack(i+1, path)
            sol.pop()
    backtrack(0, [])
    return ret
            



inputs = [("23", ["ad","ae","af","bd","be","bf","cd","ce","cf"]),
          ("", []),
          ("2", ["a","b","c"])]

for i, e in inputs:
    result = letterCombo(i)
    print(f"inputs: {i} || outputs: {result} || expected: {e}")
