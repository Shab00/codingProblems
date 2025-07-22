def lengthOfSubstring(s: str) -> int:
    pass

inputs = [("abcabcbb", 3), 
          ("bbbbb", 1), 
          ("pwwkew", 3)]

for i, e in inputs:
    result = lengthOfSubstring(i)
    print(f"Input is {i} || Output is {result} || expected is {e}")
