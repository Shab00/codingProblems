def solve(ls: list) -> int:
    l, r = 0, 1
    profit = 0
    while r < len(ls):

        if ls[l] > ls[r]:
            l += 1
            r += 1
        elif ls[l] < ls[r]:
            profit += ls[r] - ls[l]
            l += 1
            r += 1
        else:
            l += 1
            r += 1
    return profit

def greedy(ls: list) -> int:
    profit = 0
    stack = []
    for day in range(len(ls) - 1): 
        if ls[day] < ls[day + 1]:
            stack.append(ls[day])
        if ls[day] > ls[day + 1] and stack:
            profit += ls[day] - stack.pop(0)
    if stack:
        for p in stack:
            profit += ls[-1] - p
    return profit

inputs = [
        [10, 5, 4, 7, 9, 12, 6, 2, 10],
        [1,2,10,11],
        [64,32,64,16,64,0],
        [1,1,1,1],
        [4,2,5,7,7,0,7],
        [4,9,0,2,2,9,6,2,4,7]
        ]

for i in inputs:
    result = greedy(i)
    print(result)
