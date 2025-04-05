def solve(s:str) -> str:
    
    result = {'Liam': 0, 'Noah': 0}

    for i in s:
        if i == 'L':
            result['Liam'] += 1
        elif i == 'N':
            result['Noah'] += 1

    if result['Liam'] == result['Noah']:
        return 'Friendship'
    elif max(result.values()) == result['Liam']:
        return "Liam"
    elif max(result.values()) == result['Noah']:
        return "Noah"

inputs = ["LNLLLL", "NLNLNL", "NNLNLN"]

for i in inputs:
    result = solve(i)
    print(result)
