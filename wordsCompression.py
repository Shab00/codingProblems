def solve(str: str) -> str:
    
    ls = str.split()
    result = [] 
    for word in ls:
        result.append(word)
    return result

inputs = ["cat attack", 
          "football ball alley", 
          "abc cde def ef",
          "power world",
          "red dragon gon gone"]

for i in inputs:
    results = solve(i)
    print(results)
