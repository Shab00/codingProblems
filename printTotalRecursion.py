def sum_digits(num: int) -> int:
    strNum = str(num)
    if len(strNum) == 1:
        return int(strNum[0])

    return int(strNum[0]) + sum_digits(int(strNum[1::]))

print(sum_digits(1234) )
print(sum_digits(5) )
print(sum_digits(0))
