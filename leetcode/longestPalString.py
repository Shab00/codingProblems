def longestPalString(s: str) -> str:

    mid = len(s) // 2
    if len(s) % 2 == 0:
        l, r = mid, mid - 1
    else:
        l, r = mid, mid
    result = []
    while l >= 0 and r <= len(s):
        tempList = s[l:r + 1]
        tempResult = []
        for i in tempList:
            tempResult.append(i)
            result.append(''.join(tempResult))
        l -= 1
        r += 1
    new = []
    for i in result:
        if i[0] == i[len(i) - 1] and len(i) > 1:
            new.append(i)
    return new[0]

inputs = [("babad", "bab"), ("cbbd", "bb")]
for i, o in inputs:
    results = longestPalString(i)
    print(f"Inputs is {i} || Outputs is {results} || Expected {o}")
