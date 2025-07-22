def lengthOfSubstring(s: str) -> int:

    setList = set(s)
    hashMap = dict.fromkeys(setList, 0)
    l, r = 0, 1
    while r < len(s):
                    
        l += 1
        r += 1

    return len(s)

inputs = [("abcabcbb", 3), 
          ("bbbbb", 1), 
          ("pwwkew", 3)]

for i, e in inputs:
    result = lengthOfSubstring(i)
    print(f"Input is {i} || Output is {result} || expected is {e}")
