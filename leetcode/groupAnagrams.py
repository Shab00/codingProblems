def group(strs: list[str]) -> list[list[str]]:
    result = []
    hMap = {}
    for word in strs:
        sorteds = ''.join(sorted(word))
        if sorteds not in hMap:
            hMap[sorteds] = [] 
        hMap[sorteds].append(word)

    for keys in hMap:
        result.append(hMap[keys])

    return result

inputs = [(["eat","tea","tan","ate","nat","bat"],
           [["bat"],["nat","tan"],["ate","eat","tea"]]),
          ([""], [[""]]),
          (["a"], [["a"]])]
for i, e in inputs:
    result = group(i)
    print(f"input:\n{i}\noutput:\n{result}\nexpected:\n{e}\n{'-'*40}\n")
