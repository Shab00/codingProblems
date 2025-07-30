def myAtoi(s: str) -> int:
    pass

inputs = [("42", 42), (" -042", -42), 
          ("1337c0d3", 1337),
          ("0-1", 0), ("words and 987", 0)]

for string, expected in inputs:
    result = myAtoi(string)
    print(f"input: {string} || output: {result} || expected: {expected}")
