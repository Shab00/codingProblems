def isValid(s: str) -> bool:
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for char in s:
        if char == "(" or char == "[" or char == "{":
            stack.append(char)
        
        elif char == ")" or char == "]" or char == "}":
            if stack and stack[-1] == pairs[char]:
                stack.pop()
            else:
                return False
    return not stack    



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
