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

l = [1, 2, 3, 4, 5]
res = resum(l)
result = sum(l)
r = recount(l)
print(r)
print(res)
print(result)
