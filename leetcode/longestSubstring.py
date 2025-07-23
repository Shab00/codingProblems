def lengthOfSubstring(s: str) -> int:

    setList = set(s)
    hashMap = dict.fromkeys(setList, 0)
    l, r = 0, 0
    result = []
    while r < len(s):
      if hashMap[s[r]] > 1:
           hashMap[s[r]] = 0
           result.remove(s[r])
           l += 1
      if s[r] in hashMap:
           hashMap[s[r]] += 1
           result.append(s[r])
           r += 1
      print(result)
    return len(s)

inputs = [("abcabcbb", 3), 
          ("bbbbb", 1), 
          ("pwwkew", 3)]

for i, e in inputs:
    result = lengthOfSubstring(i)
    print(f"Input is {i} || Output is {result} || expected is {e}")
