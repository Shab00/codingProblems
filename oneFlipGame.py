from typing import List
def solve(l:List[int])->int:
    maxsum, orione, cursum = 0, 0, 0

    if l.count(1) == len(l) and 0 not in l:
        return len(l) - 1
    elif l.count(0) == len(l) and 1 not in l:
        return len(l)

    for i in l:
        if i == 1:
            cursum -= 1
            orione += 1
        elif i == 0:
            cursum += 1
        
        if cursum < 0:
            cursum = 0

        maxsum = max(maxsum, cursum)
       
    return orione + maxsum

lsts =[ 
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 
       [1,0,0,1,0],
       [1, 0, 0, 0, 1, 0, 0, 0], 
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,1,0,1,0,1,0,1,0,1,1,0,1,1,0,1,1,0]
]

r = [22, 4, 7, 18, 11]

for i, j in zip(lsts, r):
    result = solve(i)
    print("%d : %d*" % (result, j))
