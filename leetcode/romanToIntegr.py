def romanToInt(s: str) -> int:

    romanDict = {"I": 1, "V": 5, "X": 10,
                 "L": 50, "C": 100, "D": 500,
                 "M": 1000}
    count = 0
    l, r = 0, 1 
    for i in range(len(s) - 1):
        if romanDict[s[i]] < romanDict[s[i + 1]]:
            print(s[i], print(s[i]))
            l += 1
            r += 1
            count += romanDict[s[l]]
        else:
            count += romanDict[s[l]]
            l += 1
            r += 1

    return count

inputs = [("III", 3), ("LVIII", 58), ("MCMXCIV", 1994)]

for roman, digits in inputs:
    result = romanToInt(roman)
    print(f"The input: {roman} || The ouput: {result}, || Expected: {digits}")
