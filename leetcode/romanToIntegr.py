def romanToInt(s: str) -> int:
    pass

inputs = [("III", 3), ("LVIII", 58), ("MCMXCIV", 1994)]

for roman, digits in inputs:
    result = romanToInt(roman)
    print(f"The input: {roman} || The ouput: {result}, || Expected: {digits}")
