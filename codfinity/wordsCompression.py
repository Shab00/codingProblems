def solve(str: str) -> str:
    
    ls = str.split()
    result = []


    for i in range(len(ls) - 1):
        k = min(len(ls[i]), len(ls[i + 1]))
        first = ls[i]
        second = ls[i + 1]
        max_overlap = 0
        for i in range(k + 1):
            if first[-i:] == second[:i]:
                max_overlap = i
        result.append(second[max_overlap:])

    return ls[0] + ''.join(result)

inputs = ["cat attack", 
          "football ball alley", 
          "abc cde def ef",
          "power world",
          "red dragon gon gone"]

for i in inputs:
    results = solve(i)
    print(results)
