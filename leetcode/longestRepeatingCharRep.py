def charRep(s: str, k: int) -> int:

    l, r = 0, 1
    chars = 0
    while r < len(s):
        hMap = {}
        for i in range(len(s[l:r + 1])):
            if s[i] not in hMap:
                hMap[s[i]] = 1
            else:
                hMap[s[i]] += 1
        print(s[l], s[r])
        print(hMap)

        l += 1
        r += 1

inputs = [("ABAB", 2, 4),
          ("AABABBA", 1, 4)]

for s, k, e in inputs:
    result = charRep(s, k)
    print(
            f"inputs:\n{s, k}\n"
            f"outputs:\n{result}\n"
            f"expected:\n{e}\n"
            f"{'-'*50}"
            )
