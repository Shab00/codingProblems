def romanToInt(s: str) -> int:

    romanDict = {"I": 1, "V": 5, "X": 10,
                 "L": 50, "C": 100, "D": 500,
                 "M": 1000}
    count = 0
    l, r = 0, 1
    while r < len(s):
        if romanDict[s[l]] < romanDict[s[r]]:
            subtract = romanDict[s[r]] - romanDict[s[l]]
            count += subtract
            l += 2
            r += 2
        else:
            count += romanDict[s[l]]
            l += 1
            r += 1
    if l < len(s):
        count += romanDict[s[l]]
    return count

inputs = [("III", 3), ("LVIII", 58), ("MCMXCIV", 1994)]

for roman, digits in inputs:
    result = romanToInt(roman)
    print(f"The input: {roman} || The ouput: {result}, || Expected: {digits}")
