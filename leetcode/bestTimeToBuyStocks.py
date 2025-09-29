#mine first go very slow
# def maxProfit(prices: list[int]) -> int:
    # l, r = 0, 0
    # maxP = 0

    # while r < len(prices):
        # if prices[l] <= prices[r]:
            # print(prices[l], prices[r])
            # maxP = max(maxP, (prices[r] - prices[l]))
            # r += 1
        # elif prices[l] >= prices[r]:
            # l = r
    # return maxP

def maxProfit(prices: list[int]) -> int:
    l, r = 0, 1
    maxP = 0

    while r < len(prices):
        if prices[r] > prices[l]:
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
        else:
            l = r 
        r += 1
    return maxP

inputs = [([7,1,5,3,6,4], 5),
          ([7,6,4,3,1], 0),
          ([2,1,2,1,0,1,2], 2)]

for i, e in inputs:
    result = maxProfit(i)
    print(
            f"inputs:\n{i}\n"
            f"outputs:\n{result}\n"
            f"expected:\n{e}\n"
            f"{'-'*50}"
            )
