def isPal(x: int) -> bool:
    strNum = str(x)
    mid = len(strNum) // 2
    result = []
    if len(strNum) % 2 == 0:
        l, r = mid, mid - 1
    else:
        l, r = mid, mid

    while l >= 0 and r <= len(strNum):
        if strNum[l] != strNum[r]:
            return False
        elif strNum[l] == strNum[r]:
            result.append(strNum[l])
        l -= 1
        r += 1
    if result:
        return True

def math(x: int) -> bool:
    if x < 0:
        return False
    opp = 0
    copy = x
    while x != 0:
        digit = x % 10
        opp = opp * 10 + digit
        x //= 10
    if opp == copy:
        return True
    else:
        return False

inputs = [(121, True), (-121, False), (10, False), 
          (123321, True), (-10, False)]

for nums, b in inputs:
    result = isPal(nums)
    print(f"input: {nums} || output: {result} || expected: {b}")

for nums, b in inputs:
    result = math(nums)
    print(f"input: {nums} || output: {result} || expected: {b}")
