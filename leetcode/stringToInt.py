def myAtoi(s: str) -> int:

    Int_Max = 2**31 - 1
    Int_Min = - 2**31
    result = 0
    sign = 1
    p = 0
    while p < len(s) and s[p] == " ":
        p += 1

    if p < len(s):
        if s[p] == "-":
            sign = -1
            p += 1
        elif s[p] == "+":
            sign = 1
            p += 1

    while p < len(s) and s[p].isdigit():
        digit = ord(s[p]) - ord('0')
        if result > (Int_Max - digit) // 10:
            return Int_Max if sign == 1 else Int_Min
        result = result * 10 + digit
        p += 1

    return sign * result
#     while p < len(s):
        # if s[p] == " ":
            # p += 1
        # if s[p] == "-":
            # sign = -1
            # p += 1
        # elif s[p] == "+":
            # sign = 1
            # p += 1
        # if s[p].isdigit():
            # digit = ord(s[p]) - ord('0')
            # result = result * 10 + digit
        # elif s[p].isdigit():
            # break
        # p += 1
    # return result * sign
#     for char in s:
        # if not char.isdigit():
            # break
        # elif char.isdigit():
            # digit = ord(char) - ord('0')
            # result = result * 10 + digit
    # return result * sign

inputs = [("42", 42), (" -042", -42), 
          ("1337c0d3", 1337),
          ("0-1", 0), ("words and 987", 0)]

for string, expected in inputs:
    result = myAtoi(string)
    print(f"input: {string} || output: {result} || expected: {expected}")
