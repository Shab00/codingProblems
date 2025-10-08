def check(s1: str, s2: str) -> bool:

    hmap = {}
    for i in s1:
        if i not in hmap:
            hmap[i] = 0
        hmap[i] += 1

    smap = {}
    l = 0
    for r in range(len(s2)):
        char = s2[r]
        if char not in smap:
            smap[char] = 0
        smap[char] += 1

    
        if r - l + 1 > len(s1):
            lchar = s2[l]
            smap[lchar] -= 1
            if smap[lchar] == 0:
                del smap[lchar]
            l += 1

        if r - l + 1 == len(s1):
            if hmap == smap:
                return True
    return False
       
inputs = [("ab", "eidbaooo", True),
          ("ab", "eidboaoo", False)]

for s1, s2, e in inputs:
    result = check(s1, s2)
    print(
            f"inputs:\n{s1, s2}\n"
            f"outputs:\n{result}\n"
            f"expected:\n{e}\n"
            f"{'-'*50}"
            )
