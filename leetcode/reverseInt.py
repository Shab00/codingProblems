def reverse(x: int) -> int:
    neg = False
    result = []
    r = 0
    if x < 0:
        x = x * -1
        neg = True

    while x > 0:
        result.append(x % 10)
        x //= 10
    length = len(result) - 1
    for num in result:
        r += (num * (10 ** length))
        print(r, num, length)
        length -=  1


    if neg == True:
        r = r * - 1

    if r > 2147483647 or r < -2147483647:
        return 0
    else:
        return r

inputs = [(123, 321), (-123, -321), (120, 21)]

for nums, expec in inputs:
    result = reverse(nums)
    print(f"input: {nums} || output: {result} || expected: {expec}")
