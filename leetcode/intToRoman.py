def intToRoman(num: int) -> str:
    pass

inputs = [(3749, "MMMDCCXLIX"), (58, "LVIII"), 
          (1994, "MCMXCIV")]

for nums, e in inputs:
    result = intToRoman(nums)
    print(f"input: {nums} || output: {result} || expected: {e}")
