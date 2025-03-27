from typing import List
def solve(l:List[int])->int:
    dic = {}
    for i in l:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    mdic = max(dic.values())
    return mdic



l = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

result = solve(l)

print(result)
