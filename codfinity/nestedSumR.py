def nested_sum(ls: list[list[int]]) -> int:
    if not ls:
        return 0

    if isinstance(ls[0], int):
        return ls[0] + nested_sum(ls[1:])
    elif isinstance(ls[0], list):

        return nested_sum(ls[0]) + nested_sum(ls[1:])

print(nested_sum([1, 2, [3, 4], 5]))
print(nested_sum([1, [2, [3, 4]], 5]))
print(nested_sum([[1, 2], [[3], 4], 5]))
print(nested_sum([]))
print(nested_sum([[[[42]]]]))
