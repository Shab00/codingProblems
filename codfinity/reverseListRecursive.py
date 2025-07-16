def reverse_list(ls: list[int]) -> list[int]:

    if not ls:
        return []

    return [ls[-1]] + reverse_list(ls[:-1])

print(reverse_list([1, 2, 3]))
print(reverse_list([7, 8, 9, 10]))
print(reverse_list([]))
