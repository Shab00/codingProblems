def minWindow(s: str, t: str) -> str:
    if not t or not s:
        return ""
    
    need = {}
    for c in t:
        need[c] = need.get(c, 0) + 1
    
    window = {}
    have = 0
    need_total = len(need)
    res = [float("inf"), 0, 0]  
    l = 0
    for r in range(len(s)):
        c = s[r]
        window[c] = window.get(c, 0) + 1

        if c in need and window[c] == need[c]:
            have += 1

        while have == need_total:
            if (r - l + 1) < res[0]:
                res = [r - l + 1, l, r]
            
            left_char = s[l]
            window[left_char] -= 1
            if left_char in need and window[left_char] < need[left_char]:
                have -= 1
            l += 1

    min_len, start, end = res
    if min_len == float("inf"):
        return ""
    else:
        return s[start:end+1]


inputs = [("OUZODYXAZV", "XYZ", "YXAZ"),
          ("xyz", "xyz", "xyz"),
          ("x", "xy", "")]

for i, o, e in inputs:
    result = minWindow(i, o)
    print(
            f"inputs:\n{i, o}\n"
            f"outputs:\n{result}\n"
            f"expected:\n{e}\n"
            f"{'-'*50}"
            )
