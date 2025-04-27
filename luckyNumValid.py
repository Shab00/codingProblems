def solve(ticket: str)->str:
    print(f"ticket: {ticket}")
    mid = len(ticket) // 2

    first = ticket[:mid]
    second = ticket[mid:]
    f, s = 0, 0
    for i, j in zip(first, second):
        f += int(i)
        s += int(j)
    if f == s:
        return 'YES' 
    return 'NO'
        

inputs = ['213132', '973894']
for i in inputs:
    result = solve(i)
    print(result)
