def sum_digits(num: int) -> int:
    strNum = str(num)
    if len(strNum) == 1:
        return int(strNum[0])

    return int(strNum[0]) + sum_digits(int(strNum[1::]))

def math(num: int) -> int:
    if num < 10:
        return num
    return num % 10 + math(num // 10)

print(math(1234) )
print(math(5) )
print(math(0))
