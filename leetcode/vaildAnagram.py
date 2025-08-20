def valid(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    hMap = {}
    hMap2 = {}
    for i in t:
        if i not in hMap:
            hMap[i] = 0
        hMap[i] += 1
    for j in s:
        if j not in hMap2:
            hMap2[j] = 0
        hMap2[j] += 1
    print(hMap, hMap2)

    if hMap2 != hMap:
        return False
    else:
        return True

inputs = [("anagram", "nagaram", True),
          ("rat", "car", False),
          ("aabbbb", "aaaabb", False)]

for s, t, e in inputs:
    result = valid(s, t)
    print(f"input: {s} || output: {result} || expected: {e}")
