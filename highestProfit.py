def solve(ls: list) -> int:
    l, r = 0, 1
    maxP = 0
    profit = 0
    while r < len(ls):

        if ls[l] < ls[r]:
            profit = ls[r] - ls[l]
            maxP = max(maxP, profit)
        else:
            l = r
        r += 1

    return maxP

def greedy(ls: list) -> int:

    profit = 0
    stack = []
    n = len(ls)
    for i in range(n - 1):
        if ls[i] < ls[i + 1]:
            stack.append(ls[i])  
        if ls[i] > ls[i + 1] and stack:
            profit += ls[i] - stack.pop(0)  
    for buy_price in stack:
        profit += ls[-1] - buy_price
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
