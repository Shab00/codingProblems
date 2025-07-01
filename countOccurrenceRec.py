def count_occurrences(ls: list, num: int) -> int:

    if not ls:
        return 0
    if num == ls[0]:
        return 1 + count_occurrences(ls[1:], num)
    else:
        return count_occurrences(ls[1:], num)


print(count_occurrences([1, 2, 1, 3, 1], 1))
print(count_occurrences([4, 5, 6], 2))
