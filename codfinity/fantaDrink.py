from typing import List

def solve(prices:List[int], coins:List[int])->List[int]:

    pl, lp = 0, len(prices) - 1 
    pc, lc = 0, len(coins) - 1
    count = 0 
    output = []

    while pl <= lp and pc <= lc:
        
        if pl == lp:
            if coins[pc] >= prices[pl]:
                count += 1
            output.append(count)
            count = 0
            pl = 0
            pc += 1

        elif coins[pc] >= prices[pl]:
            count += 1
            pl += 1

        else:
            pl += 1

    return output

prices, coins = [3, 10, 8, 6, 11], [1, 10, 3, 11]

result = solve(prices, coins)
print(result)
