def contains(ls: list, n: int) -> bool:

    if not ls:
        return False

    if ls[0] == n:
        return True

    return contains(ls[1:], n)


print(contains([1, 2, 3], 2))
print(contains([7, 8, 9, 10], 5))
print(contains([], 100))
print(contains([42], 42)  )
