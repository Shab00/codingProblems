def solve(a:int, b:int, c:int) -> int:
    nums = [a, b, c]
    dic = {}
    for i in nums:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    mink = min(dic, key=dic.get)

    return mink

    
a, b, c = 7, 5, 5

result = solve(a, b, c)

print(result)
