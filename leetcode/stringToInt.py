def myAtoi(s: str) -> int:

    Int_Max = 2**31 - 1
    Int_Min = - 2**31
    result = 0
    sign = 1
    for char in s:
        if not char.isdigit():
            break
        elif char.isdigit():
            digit = ord(char) - ord('0')
            result = result * 10 + digit
    return result * sign

inputs = [("42", 42), (" -042", -42), 
          ("1337c0d3", 1337),
          ("0-1", 0), ("words and 987", 0)]

for string, expected in inputs:
    result = myAtoi(string)
    print(f"input: {string} || output: {result} || expected: {expected}")
