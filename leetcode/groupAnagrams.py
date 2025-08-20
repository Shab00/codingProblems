def group(strs: str) -> list[list[str]]:
    pass

inputs = [(["eat","tea","tan","ate","nat","bat"],
           [["bat"],["nat","tan"],["ate","eat","tea"]]),
          ([""], [[""]]),
          (["a"], [["a"]])]
for i, e in inputs:
    result = group(i)
    print(f"input:\n{i}\noutput:\n{result}\nexpected:\n{e}\n{'-'*40}\n")
