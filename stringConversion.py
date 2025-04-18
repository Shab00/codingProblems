def solve(s:str) -> str:
    print(f"s: {s}")

    string = s.lower()
    stringList = list(string)
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    new = []
    for i in stringList:

        if i not in vowels:
           new.append(i)
        
    newList = '.' + '.'.join(new)
    return newList

inputs = ["hello", "Codefinity", "beautiful", "PYTHON", 
          "abcdefghijklmnopqrstuvwxyz"]
outputs = [".h.l.l", ".c.d.f.n.t", "", "", ""]
for i, j in zip(inputs, outputs):
    result = solve(i)
    print("input: %s => %s" % (result, j))
