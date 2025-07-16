def flatten(ls: list[list[int]]) -> list:

    if not ls:
        return []
    if isinstance(ls[0], int):
        
        return [ls[0]] +  flatten(ls[1:])

    if isinstance(ls[0], list):

        return flatten(ls[0]) + flatten(ls[1:]) 

print(flatten([1, 2, [3, 4], 5]))
print(flatten([1, [2, [3, 4]], 5]))
print(flatten([[1, 2], [[3], 4], 5]))
print(flatten([]))
print(flatten([[[[42]]]]))
