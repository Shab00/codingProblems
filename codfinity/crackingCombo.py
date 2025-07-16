def solve(original:int, target:int) -> int:
    print(f"priginal: {original}, target: {target}")
    if original == 00000:
        sori = '00000'
        star = str(target)
    else:
        sori = str(original)
        star = str(target)
    spins = 0
    for i, j in zip(sori, star):
        diff = abs(int(i) - int(j))
        maximum = 10 - diff

        spins += min(diff, maximum)

    return spins

original, target = 00000, 93199

result = solve(original, target)
print(result)
