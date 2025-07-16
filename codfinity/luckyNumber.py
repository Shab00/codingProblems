def solve(n:int) -> str:

    r = str(n)
    maps = {'4': 0, '7': 0, 'other': 0}
    for i in r:
        if i == '4':
            maps['4'] += 1
        elif i == '7':
            maps['7'] += 1
        else:
            maps['other'] += 1
    if maps['other'] > 0:
        return "No"
    return "Yes"

def solved(n: int) -> str:
    if all(d in {'4', '7'} for d in str(n)):
        return "YES"
    return "NO"



l = [47, 5, 8, 744, 123, 4, 4747]

for i in l:
    result = solve(i)
    print(result)
