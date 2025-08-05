def intToRoman(num: int) -> str:

    pairs = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
            ]
    result = ""
    for value, char in pairs:
        while num >= value:
            result += char
            num -= value

    return result


inputs = [(3749, "MMMDCCXLIX"), (58, "LVIII"), 
          (1994, "MCMXCIV")]

for nums, e in inputs:
    result = intToRoman(nums)
    print(f"input: {nums} || output: {result} || expected: {e}")
