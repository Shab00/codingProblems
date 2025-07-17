def romanToInt(s: str) -> int:

    romanDict = {"I": 1, "V": 5, "X": 10,
                 "L": 50, "C": 100, "D": 500,
                 "M": 1000}
    count = 0
    for i in range(len(s) - 1):
        print("look %i" % romanDict[s[i]])
        if romanDict[s[i]] < romanDict[s[i + 1]]:
            print(s[i])
            count += romanDict[s[i]]
        else:
            count += romanDict[s[i]]

    return count

inputs = [("III", 3), ("LVIII", 58), ("MCMXCIV", 1994)]

for roman, digits in inputs:
    result = romanToInt(roman)
    print(f"The input: {roman} || The ouput: {result}, || Expected: {digits}")
