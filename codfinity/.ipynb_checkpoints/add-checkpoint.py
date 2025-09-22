def sum(lst: list[int]) -> int:
    total = 0
    for i in lst:
        total += i
    return total

def resum(lst: list[int]) -> int:
    if not lst:
        return 0
    return lst[0] + resum(lst[1:])
    
def recount(lst: list[int]) -> int:
    if not lst:
        return 0
    return 1 + recount(lst[1:])

def mnum(lst: list[int]) -> int:
    if len(lst) == 2:
        return lst[0] if lst[0] > lst[1] else lst[1]
    submax = max(lst[1:])
    return lst[0] if lst[0] > submax else submax

l = [1, 2, 3, 4, 5]
res = resum(l)
result = sum(l)
r = recount(l)
m = mnum(l)
print(m)
print(r)
print(res)
print(result)
