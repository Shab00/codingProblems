def lengthOfSubstring(s: str) -> int:

    l, r = 0, 0
    length = set()
    maxL = 0
    while r < len(s):
        if s[r] not in length:
            length.add(s[r])
            r += 1
        else:
            length.remove(s[l])
            l += 1
        maxL = max(maxL, len(length))
    return maxL

inputs = [("abcabcbb", 3), 
          ("bbbbb", 1), 
          ("pwwkew", 3)]

for i, e in inputs:
    result = lengthOfSubstring(i)
    print(f"Input is {i} || Output is {result} || expected is {e}")
